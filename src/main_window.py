from PySide6 import QtGui, QtCore, QtWidgets

from pyqtgraph import GraphicsLayoutWidget
from pyqtgraph.exporters import ImageExporter

from auxfiles.signal_names import SIGNAL_NAMES
from .qt_workers import Worker
from . import utils
from . import class_signal_arrays
from .ui.ui_mainwindow import Ui_MainWindow
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
            lambda: utils.getLastShot(self.ui.shotNumberInput, self.ui.statusbar)
        )
        self.ui.loadDataButton.clicked.connect(self.loadData)
        self.ui.seeAloneButton.clicked.connect(self.seeAlone)
        self.ui.saveButton.clicked.connect(self.savefig)
        self.ui.spectrogramsButton.clicked.connect(self.makeSpectrograms)
        self.ui.fftButton.clicked.connect(self.makeFfts)
        self.ui.integrateDataButton.clicked.connect(self.integrateData)

    def populate_boxes(self):
        self.ui.signalArraySelector.addItems(list(SIGNAL_NAMES.keys()))
        utils.getLastShot(self.ui.shotNumberInput, self.ui.statusbar)

    def savefig(self):
        os.makedirs("./figs", exist_ok=True)
        exporter = ImageExporter(self.ui.figLayout)
        exporter.parameters()["width"] = 3000
        exporter.export("figs/tmp.png")

    def seeAlone(self):
        info_changed = self.info.refresh()
        self.array.plot_alone(self.info.selectedCoil)
        # plotting.plot_coil(self.ui.figLayout, self.info, self.array)

    def make_array(self):
        self.info.refresh()
        if hasattr(self, "array"):
            if self.info.has_changed is False:
                return
        self.array = class_signal_arrays.SignalArray(
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
        self.array.plot_integrated()

    def refresh(self):
        self.info.refresh()
        self.array.plot_signals()
        self.ui.coilDataRetrievalSelector.clear()
        self.ui.coilDataRetrievalSelector.addItems(
            [sig_name for sig_name in self.array.signals]
        )

    def makeSpectrograms(self):
        tlim = float(self.ui.lowerTLim.text()), float(self.ui.upperTLim.text())
        self.array.make_spectrograms(tlim=tlim, printer=self.ui.statusbar.showMessage)
        self.array.plot_spectrograms(tlim=tlim)
        self.ui.statusbar.showMessage("Done")
        # array.signals[idx].plot_spec(plots[pltidx], colormap=COLORMAP, tlim=tlim)
        # plotting.spectrograms_array(self.ui.figLayout, self.info, self.array, tlim=tlim)

    def makeFfts(self):
        self.refresh()
        for key in self.array.ax:
            self.array.ax[key].ctrl.fftCheck.setChecked(True)
            self.array.ax[key].ctrl.logXCheck.setChecked(True)
            self.array.ax[key].ctrl.logYCheck.setChecked(True)
