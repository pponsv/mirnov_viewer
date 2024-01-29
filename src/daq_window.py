from PySide6 import QtGui, QtCore, QtWidgets

from .ui.ui_listdialog import Ui_Dialog
from lib import TJII_data_acquisition as da


class DAQ_dialog(QtWidgets.QDialog):
    def __init__(self, shot, names):
        super(DAQ_dialog, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.okButton.clicked.connect(lambda: self.done(0))

        self.shot = shot
        self.names = names
        self.show()
        self.get_info()
        self.disp_info()

    def get_info(self):
        self.items = []
        for name in self.names:
            ndat, nvent, ierr = da.py_dimens(self.shot, name)

            self.items.append(f"{self.shot}\t{name}\t{ndat}\t{ierr}")
        print(self.items)

    def disp_info(self):
        self.ui.daqListWidget.addItems(self.items)
