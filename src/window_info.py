from .ui_mainwindow import Ui_MainWindow


class WindowInfo:
    def __init__(self, UiClass: Ui_MainWindow):
        self.array = UiClass.signalArraySelector.currentText()
        # self.subarray = window.coilSubarraySelector.currentText()
        # self.orientation = window.coilOrientationSelector.currentText()
        try:
            self.shot = int(UiClass.shotNumberInput.text())
        except:
            self.shot = UiClass.shotNumberInput.text()
        try:
            self.downsampleFactor = int(UiClass.downsampleFactorBox.text())
        except:
            self.downsampleFactor = None
        self.downsample = UiClass.downsampleBox.isChecked()
        self.selectedCoil = UiClass.coilDataRetrievalSelector.currentText()
        # print(self.shot, self.array, self.subarray, self.orientation, self.downsample)
        print(self.shot, self.array, self.downsample)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
