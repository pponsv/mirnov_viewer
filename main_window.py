import PyQt6 as qt
import pyqtgraph as pg
import pyqtgraph.exporters

# import database
import plotting

uiMainWindowFile = "./ui/windowLayout.ui"  # Enter file here.
ui_MainWindow, QtBaseClass = qt.uic.loadUiType(uiMainWindowFile)


class WindowInfo:
    def __init__(self, window):
        self.array = window.coilArraySelector.currentText()
        self.subarray = window.coilSubarraySelector.currentText()
        self.orientation = window.coilOrientationSelector.currentText()
        try:
            self.shot = int(window.shotNumberInput.text())
            self.downsampleFactor = int(window.downsampleFactorBox.text())
        except:
            self.shot = window.shotNumberInput.text()
            self.downsampleFactor = None
        self.downsample = window.downsampleBox.isChecked()
        self.selectedCoil = window.coilDataRetrievalSelector.currentText()
        print(self.shot, self.array, self.subarray, self.orientation, self.downsample)

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

        self.graphwidget.setBackground("w")
        self.figLayout = pg.GraphicsLayout()
        self.graphwidget.setCentralItem(self.figLayout)

        # self.loadButton.clicked.connect(self.refreshInfo)
        self.refreshButton.clicked.connect(self.refresh)
        self.coilArraySelector.currentIndexChanged.connect(self.comboboxLogic)
        self.lastShotButton.clicked.connect(lambda: plotting.getLastShot(self))
        self.loadDataButton.clicked.connect(self.loadData)
        self.seeAloneButton.clicked.connect(self.seeAlone)
        self.saveButton.clicked.connect(self.savefig)

    def savefig(self):
        exporter = pg.exporters.ImageExporter(self.figLayout)
        exporter.parameters()["width"] = 3000
        exporter.export("figs/tmp.png")

    def seeAlone(self):
        info_changed = self.refreshInfo()
        plotting.plot_coil(self.figLayout, self.info, self.array)

    def loadData(self):
        info_changed = self.refreshInfo()
        if info_changed:
            self.array = plotting.make_array(self.info)
            self.array.read_multi()
            self.statusbar.showMessage("Done")
        self.refresh()

    def refresh(self):
        self.refreshInfo()
        plotting.plot_array(self.figLayout, self.info, self.array)
        self.coilDataRetrievalSelector.clear()
        self.coilDataRetrievalSelector.addItems(
            [coil.name for coil in self.array.coils]
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

    def comboboxLogic(self):
        if self.coilArraySelector.currentText() == "Helical":
            self.coilOrientationSelector.setDisabled(False)
            self.coilSubarraySelector.setDisabled(False)
        else:
            self.coilSubarraySelector.setDisabled(True)
            self.coilOrientationSelector.setDisabled(True)
