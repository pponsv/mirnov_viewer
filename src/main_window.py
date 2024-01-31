import os
from PySide6 import QtGui, QtCore, QtWidgets

from pyqtgraph.exporters import ImageExporter

from auxfiles.signal_names import SIGNAL_NAMES
from .daq_window import DAQ_dialog
from . import utils
from . import class_signal_arrays
from .ui.ui_mainwindow import Ui_MainWindow
from .class_window_info import WindowInfo


DOUBLE_VALIDATOR = QtGui.QRegularExpressionValidator(
    "^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)$"
)
INT_VALIDATOR = QtGui.QRegularExpressionValidator("[1-9][0-9]*")


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

        #   Window info
        self.info = WindowInfo(self.ui)

        #   DAQ dialog
        self.daq_dialog = QtWidgets.QDialog()
        self.show()

    def init_ui(self):
        #   Figure Widget
        self.ui.figLayout.setBackground("w")

        #   Validators
        self.ui.lowerTLim.setValidator(DOUBLE_VALIDATOR)
        self.ui.upperTLim.setValidator(DOUBLE_VALIDATOR)
        self.ui.filterFMax.setValidator(DOUBLE_VALIDATOR)
        self.ui.filterFMin.setValidator(DOUBLE_VALIDATOR)
        self.ui.shotNumberInput.setValidator(INT_VALIDATOR)
        self.ui.spgramNperseg.setValidator(INT_VALIDATOR)
        self.ui.spgramNoverlap.setValidator(INT_VALIDATOR)
        self.ui.downsampleFactorBox.setValidator(INT_VALIDATOR)

        #   Connections
        self.ui.shotNumberInput.returnPressed.connect(self.loadData)
        self.ui.refreshButton.clicked.connect(self.refresh_plots)
        self.ui.lastShotButton.clicked.connect(
            lambda: utils.getLastShot(
                self.ui.shotNumberInput, self.ui.statusbar.showMessage
            )
        )
        self.ui.loadDataButton.clicked.connect(self.loadData)
        self.ui.seeAloneButton.clicked.connect(self.seeAlone)
        self.ui.spectrogramsButton.clicked.connect(self.makeSpectrograms)
        self.ui.fftButton.clicked.connect(self.makeFfts)
        self.ui.integrateDataButton.clicked.connect(self.integrateData)
        self.ui.singleSpectrogramButton.clicked.connect(self.specAlone)

        #   Menu bar
        self.ui.actionCheck_DAQ.triggered.connect(self.showDAQ)
        self.ui.actionSave_figure.triggered.connect(self.savefig)

    def showDAQ(self):
        self.daq_dialog.close()
        self.info.refresh()
        self.daq_dialog = DAQ_dialog(self.info.shot, SIGNAL_NAMES[self.info.array])

    def populate_boxes(self):
        self.ui.signalArraySelector.addItems(list(SIGNAL_NAMES.keys()))
        utils.getLastShot(self.ui.shotNumberInput, self.ui.statusbar.showMessage)

    def savefig(self):
        os.makedirs("./figs", exist_ok=True)
        exporter = ImageExporter(self.ui.figLayout.scene())
        exporter.parameters()["width"] = 3000
        exporter.export("figs/tmp.png")

    def specAlone(self):
        self.info.refresh()
        self.array.plot_spec_alone(self.info.selectedCoil)

    def seeAlone(self):
        self.info.refresh()
        self.array.plot_alone(self.info.selectedCoil)

    def make_array(self):
        self.info.refresh()
        if hasattr(self, "array"):
            if self.info.shot == self.array.shot:
                if SIGNAL_NAMES[self.info.array] == [sig for sig in self.array.signals]:
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
        self.refresh_plots()

    def integrateData(self):
        self.array.plot_integrated()

    def refresh_plots(self):
        self.info.refresh()
        self.array.plot_signals()
        self.ui.coilDataRetrievalSelector.clear()
        self.ui.coilDataRetrievalSelector.addItems(
            [sig_name for sig_name in self.array.signals]
        )

    def makeSpectrograms(self):
        self.info.refresh()
        self.array.make_spectrograms(printer=self.ui.statusbar.showMessage)
        self.array.plot_spectrograms()
        self.ui.statusbar.showMessage("Done")

    def makeFfts(self):
        self.refresh_plots()
        for key in self.array.ax:
            self.array.ax[key].ctrl.fftCheck.setChecked(True)
            self.array.ax[key].ctrl.logXCheck.setChecked(True)
            self.array.ax[key].ctrl.logYCheck.setChecked(True)
