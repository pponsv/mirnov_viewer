import PyQt5 as qt
import pyqtgraph as pg
from pyqtgraph.exporters import ImageExporter

from auxfiles.mirnov_names import COIL_NAMES
import plotting
import os

uiMainWindowFile = "./ui/windowLayout.ui"  # Enter file here.
ui_MainWindow, QtBaseClass = qt.uic.loadUiType(uiMainWindowFile)

locale = qt.QtCore.QLocale("en_US")
doubleValidator = qt.QtGui.QDoubleValidator()
doubleValidator.setLocale(locale)
intValidator = qt.QtGui.QIntValidator()


class WindowInfo:
    def __init__(self, window):
        self.array = window.signalArraySelector.currentText()
        # self.subarray = window.coilSubarraySelector.currentText()
        # self.orientation = window.coilOrientationSelector.currentText()
        try:
            self.shot = int(window.shotNumberInput.text())
        except:
            self.shot = window.shotNumberInput.text()
        try:
            self.downsampleFactor = int(window.downsampleFactorBox.text())
        except:
            self.downsampleFactor = None
        self.downsample = window.downsampleBox.isChecked()
        self.selectedCoil = window.coilDataRetrievalSelector.currentText()
        # print(self.shot, self.array, self.subarray, self.orientation, self.downsample)
        print(self.shot, self.array, self.downsample)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


class MainWindow(qt.QtWidgets.QMainWindow, ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

        self.info = WindowInfo(self)
        self.populate_boxes()

        self.graphwidget.setBackground("w")
        self.figLayout = pg.GraphicsLayout()
        self.graphwidget.setCentralItem(self.figLayout)
        self.lowerTLim.setValidator(doubleValidator)
        self.upperTLim.setValidator(doubleValidator)
        self.shotNumberInput.setValidator(intValidator)

        # self.loadButton.clicked.connect(self.refreshInfo)
        self.refreshButton.clicked.connect(self.refresh)
        # self.signalArraySelector.currentIndexChanged.connect(self.comboboxLogic)
        self.lastShotButton.clicked.connect(lambda: plotting.getLastShot(self))
        self.loadDataButton.clicked.connect(self.loadData)
        self.seeAloneButton.clicked.connect(self.seeAlone)
        self.saveButton.clicked.connect(self.savefig)
        self.spectrogramsButton.clicked.connect(self.makeSpectrograms)
        self.fftButton.clicked.connect(self.makeFfts)
        self.integrateDataButton.clicked.connect(self.integrateData)

    def populate_boxes(self):
        self.signalArraySelector.addItems(COIL_NAMES.keys())

    def savefig(self):
        os.makedirs("./figs", exist_ok=True)
        exporter = ImageExporter(self.figLayout)
        exporter.parameters()["width"] = 3000
        exporter.export("figs/tmp.png")

    def seeAlone(self):
        info_changed = self.refreshInfo()
        plotting.plot_coil(self.figLayout, self.info, self.array)

    def loadData(self):
        info_changed = self.refreshInfo()
        # if info_changed:
        self.array = plotting.make_array(self.info)
        self.array.read_multi(printer=self.statusbar.showMessage)
        self.statusbar.showMessage("Done")
        self.refresh()

    def integrateData(self):
        self.plots = plotting.plot_integrated_array(
            self.figLayout, self.info, self.array
        )

    def refresh(self):
        self.refreshInfo()
        self.plots = plotting.plot_array(self.figLayout, self.info, self.array)
        self.coilDataRetrievalSelector.clear()
        self.coilDataRetrievalSelector.addItems(
            [coil.name for coil in self.array.signals]
        )

    def refreshInfo(self):
        try:
            info = WindowInfo(self)
            self.statusbar.clearMessage()
            equal = info != self.info
            self.info = info
            return equal
        except Exception as e:
            print(repr(e))
            self.statusbar.showMessage(f"Error: {e}")
        return None

    # def comboboxLogic(self):
    #     if self.signalArraySelector.currentText() == "Helical":
    #         self.coilOrientationSelector.setDisabled(False)
    #         self.coilSubarraySelector.setDisabled(False)
    #     else:
    #         self.coilSubarraySelector.setDisabled(True)
    #         self.coilOrientationSelector.setDisabled(True)

    def makeSpectrograms(self):
        tlim = float(self.lowerTLim.text()), float(self.upperTLim.text())
        plotting.spectrograms_array(self.figLayout, self.info, self.array, tlim=tlim)

    def makeFfts(self):
        self.refresh()
        for key in self.plots:
            self.plots[key].ctrl.fftCheck.setChecked(True)
            self.plots[key].ctrl.logXCheck.setChecked(True)
            self.plots[key].ctrl.logYCheck.setChecked(True)
