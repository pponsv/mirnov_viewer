from PySide6 import QtGui, QtCore, QtWidgets

# from PySide6.QtUiTools import QUiLoader
from pyqtgraph import GraphicsLayout
from pyqtgraph.exporters import ImageExporter

from auxfiles.signal_names import SIGNAL_NAMES
from . import plotting
import os


locale = QtCore.QLocale("en_US")
doubleValidator = QtGui.QDoubleValidator()
doubleValidator.setLocale(locale)
intValidator = QtGui.QIntValidator()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, Ui_MainWindow):
        super(MainWindow, self).__init__()
        #   UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.populate_boxes()

        self.info = WindowInfo(self)
        self.show()

    def init_ui(self):
        self.ui.figLayout.setBackground("w")
        self.ui.lowerTLim.setValidator(doubleValidator)
        self.ui.upperTLim.setValidator(doubleValidator)
        self.ui.shotNumberInput.setValidator(intValidator)
        self.ui.shotNumberInput.returnPressed.connect(self.loadData)
        # self.ui.loadButton.clicked.connect(self.ui.refreshInfo)
        self.ui.refreshButton.clicked.connect(self.refresh)
        # self.signalArraySelector.currentIndexChanged.connect(self.comboboxLogic)
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

    def savefig(self):
        os.makedirs("./figs", exist_ok=True)
        exporter = ImageExporter(self.ui.figLayout)
        exporter.parameters()["width"] = 3000
        exporter.export("figs/tmp.png")

    def seeAlone(self):
        info_changed = self.refreshInfo()
        plotting.plot_coil(self.ui.figLayout, self.info, self.array)

    def loadData(self):
        info_changed = self.refreshInfo()
        # if info_changed:
        self.array = plotting.make_array(self.info)
        self.array.read_multi(printer=self.ui.statusbar.showMessage)
        self.ui.statusbar.showMessage("Done")
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
            info = WindowInfo(self)
            self.ui.statusbar.clearMessage()
            equal = info != self.info
            self.info = info
            return equal
        except Exception as e:
            print(repr(e))
            self.ui.statusbar.showMessage(f"Error: {e}")
        return None

    # def comboboxLogic(self):
    #     if self.signalArraySelector.currentText() == "Helical":
    #         self.coilOrientationSelector.setDisabled(False)
    #         self.coilSubarraySelector.setDisabled(False)
    #     else:
    #         self.coilSubarraySelector.setDisabled(True)
    #         self.coilOrientationSelector.setDisabled(True)

    def makeSpectrograms(self):
        tlim = float(self.ui.lowerTLim.text()), float(self.ui.upperTLim.text())
        plotting.spectrograms_array(self.ui.figLayout, self.info, self.array, tlim=tlim)

    def makeFfts(self):
        self.refresh()
        for key in self.plots:
            self.plots[key].ctrl.fftCheck.setChecked(True)
            self.plots[key].ctrl.logXCheck.setChecked(True)
            self.plots[key].ctrl.logYCheck.setChecked(True)


class WindowInfo:
    def __init__(self, window: MainWindow):
        self.array = window.ui.signalArraySelector.currentText()
        # self.subarray = window.coilSubarraySelector.currentText()
        # self.orientation = window.coilOrientationSelector.currentText()
        try:
            self.shot = int(window.ui.shotNumberInput.text())
        except:
            self.shot = window.ui.shotNumberInput.text()
        try:
            self.downsampleFactor = int(window.ui.downsampleFactorBox.text())
        except:
            self.downsampleFactor = None
        self.downsample = window.ui.downsampleBox.isChecked()
        self.selectedCoil = window.ui.coilDataRetrievalSelector.currentText()
        # print(self.shot, self.array, self.subarray, self.orientation, self.downsample)
        print(self.shot, self.array, self.downsample)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
