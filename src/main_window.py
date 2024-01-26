from PySide6 import QtGui, QtCore, QtWidgets

# from PySide6.QtUiTools import QUiLoader
from pyqtgraph import GraphicsLayout
from pyqtgraph.exporters import ImageExporter

from auxfiles.signal_names import SIGNAL_NAMES
from .qt_workers import Worker
from . import plotting
from . import signal_arrays
from .ui_mainwindow import Ui_MainWindow
from .window_info import WindowInfo
import os


locale = QtCore.QLocale("en_US")
doubleValidator = QtGui.QDoubleValidator()
doubleValidator.setLocale(locale)
intValidator = QtGui.QIntValidator()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        #   UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.populate_boxes()

        #   Threading
        self.threadpool = QtCore.QThreadPool()
        self.threadpool.setMaxThreadCount(5)

        self.info = WindowInfo(self.ui)
        self.show()

    def init_ui(self):
        self.ui.figLayout.setBackground("w")
        self.ui.lowerTLim.setValidator(doubleValidator)
        self.ui.upperTLim.setValidator(doubleValidator)
        self.ui.shotNumberInput.setValidator(intValidator)
        self.ui.shotNumberInput.returnPressed.connect(self.loadData)
        self.ui.refreshButton.clicked.connect(self.refresh)
        self.ui.lastShotButton.clicked.connect(
            lambda: plotting.getLastShot(self.ui.shotNumberInput, self.ui.statusbar)
        )
        self.ui.loadDataButton.clicked.connect(self.loadData)
        self.ui.seeAloneButton.clicked.connect(self.seeAlone)
        self.ui.saveButton.clicked.connect(self.savefig)
        self.ui.spectrogramsButton.clicked.connect(self.makeSpectrograms)
        self.ui.fftButton.clicked.connect(self.makeFfts)
        self.ui.integrateDataButton.clicked.connect(self.integrateData)

    def populate_boxes(self):
        self.ui.signalArraySelector.addItems(list(SIGNAL_NAMES.keys()))
        plotting.getLastShot(self.ui.shotNumberInput, self.ui.statusbar)

    def savefig(self):
        os.makedirs("./figs", exist_ok=True)
        exporter = ImageExporter(self.ui.figLayout)
        exporter.parameters()["width"] = 3000
        exporter.export("figs/tmp.png")

    def seeAlone(self):
        info_changed = self.refreshInfo()
        plotting.plot_coil(self.ui.figLayout, self.info, self.array)

    def make_array(self):
        info_changed = self.refreshInfo()
        if hasattr(self, "array"):
            if self.array.info == self.info:
                return
        self.array = signal_arrays.SignalArray(
            shot=self.info.shot,
            names=SIGNAL_NAMES[self.info.array],
            fig=self.ui.figLayout,
            threadpool=self.threadpool,
            info=self.info,
        )

    def loadData(self):
        self.make_array()
        self.array.read_parallel(printer=self.ui.statusbar.showMessage)
        self.refresh()

    def integrateData(self):
        self.plots = plotting.plot_integrated_array(
            self.ui.figLayout, self.info, self.array
        )

    def refresh(self):
        self.refreshInfo()
        self.plots = plotting.plot_array(self.ui.figLayout, self.info, self.array)
        self.ui.coilDataRetrievalSelector.clear()
        self.ui.coilDataRetrievalSelector.addItems(
            [coil.name for coil in self.array.signals]
        )

    def refreshInfo(self):
        try:
            info = WindowInfo(self.ui)
            self.ui.statusbar.clearMessage()
            equal = info != self.info
            self.info = info
            return equal
        except Exception as e:
            print(repr(e))
            self.ui.statusbar.showMessage(f"Error: {e}")
        return None

    def makeSpectrograms(self):
        tlim = float(self.ui.lowerTLim.text()), float(self.ui.upperTLim.text())
        nx, ny = plotting.layout_size[len(self.array.signals)]
        plots = plotting.make_plots(self.ui.figLayout, nx, ny, sharex=True, sharey=True)
        print(plots)
        workers = []
        for idx, pltidx in enumerate(plots):
            # print(idx, pltidx, plots[pltidx])
            workers.append(
                Worker(
                    self.array.signals[idx].spectrogram,
                    tlim=tlim,
                )
            )
            self.threadpool.start(workers[-1])
        workers[-1].signaler.finished.connect(
            lambda: [
                sig.plot_spec(plots[pltidx], plotting.COLORMAP, tlim)
                for sig in self.array.signals
            ]
        )
        self.ui.statusbar.showMessage("Done")
        # array.signals[idx].plot_spec(plots[pltidx], colormap=COLORMAP, tlim=tlim)
        # plotting.spectrograms_array(self.ui.figLayout, self.info, self.array, tlim=tlim)

    def makeFfts(self):
        self.refresh()
        for key in self.plots:
            self.plots[key].ctrl.fftCheck.setChecked(True)
            self.plots[key].ctrl.logXCheck.setChecked(True)
            self.plots[key].ctrl.logYCheck.setChecked(True)
