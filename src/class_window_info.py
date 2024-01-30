from .ui.ui_mainwindow import Ui_MainWindow


class WindowInfo:
    def __init__(self, UiClass: Ui_MainWindow):
        self.ui = UiClass
        self.has_changed = True
        self.refresh()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def refresh(self):
        old_info = self.__dict__.copy()  #   Necessary to be able to compare

        self.array = self.ui.signalArraySelector.currentText()
        try:
            self.shot = int(self.ui.shotNumberInput.text())
        except:
            self.shot = self.ui.shotNumberInput.text()
        try:
            self.downsampleFactor = int(self.ui.downsampleFactorBox.text())
        except:
            self.downsampleFactor = None

        self.downsample = self.ui.downsampleBox.isChecked()
        self.selectedCoil = self.ui.coilDataRetrievalSelector.currentText()
        self.has_changed = not (self.__dict__ == old_info)
        self.filter_info()
        self.spgram_info()

    def filter_info(self):
        self.filt = self.ui.filterCheckbox.isChecked()
        try:
            self.flim = float(self.ui.filterFMin.text()), float(
                self.ui.filterFMax.text()
            )
        except:
            self.flim = None

    def spgram_info(self):
        try:
            self.tlim = float(self.ui.lowerTLim.text()), float(self.ui.upperTLim.text())
        except:
            self.tlim = (None, None)
        try:
            self.nperseg = int(self.ui.spgramNperseg.text())
        except:
            self.nperseg = None
        try:
            self.noverlap = int(self.ui.spgramNoverlap.text())
        except:
            self.noverlap = None

        print(self.tlim, self.nperseg, self.noverlap)
