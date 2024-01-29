from .ui.ui_mainwindow import Ui_MainWindow


class WindowInfo:
    def __init__(self, UiClass: Ui_MainWindow):
        self.UI_CLASS = UiClass
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

        self.array = self.UI_CLASS.signalArraySelector.currentText()
        try:
            self.shot = int(self.UI_CLASS.shotNumberInput.text())
        except:
            self.shot = self.UI_CLASS.shotNumberInput.text()
        try:
            self.downsampleFactor = int(self.UI_CLASS.downsampleFactorBox.text())
        except:
            self.downsampleFactor = None
        self.downsample = self.UI_CLASS.downsampleBox.isChecked()
        self.selectedCoil = self.UI_CLASS.coilDataRetrievalSelector.currentText()
        self.has_changed = not (self.__dict__ == old_info)

        # print(self.shot, self.array, self.downsample)

        # print("INFO CHANGED", self.has_changed)
