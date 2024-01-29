from PySide6 import QtGui, QtCore, QtWidgets

from .ui.ui_listdialog import Ui_Dialog
from lib import TJII_data_acquisition as da


class DAQ_dialog(QtWidgets.QDialog):
    def __init__(self, shot, names):
        super(DAQ_dialog, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.daqTableWidget.setColumnCount(4)
        self.ui.daqTableWidget.setHorizontalHeaderLabels(
            ["SHOT", "SIGNAL", "NDAT", "IERR"]
        )
        # self.ui.daqTableWidget.setEditTriggers(QtWidgets.QTableWidgetItem.setFlags)

        self.ui.okButton.clicked.connect(self.close)

        self.shot = shot
        self.names = names
        self.show()
        self.get_info()
        self.disp_info()

    def get_info_str(self):
        self.daq_list = []
        for name in self.names:
            ndat, nvent, ierr = da.py_dimens(self.shot, name)

            self.daq_list.append(f"{self.shot}\t{name}\t{ndat}\t{ierr}")
        print(self.daq_list)

    def get_info(self):
        self.daq_list = []
        for name in self.names:
            ndat, nvent, ierr = da.py_dimens(self.shot, name)
            self.daq_list.append([self.shot, name, ndat, ierr])

    # def disp_info_listwidget(self):
    #     self.ui.daqListWidget.addItems(self.items)

    def disp_info(self):
        self.ui.daqTableWidget.setRowCount(len(self.names))
        for ridx, daq_item in enumerate(self.daq_list):
            for cidx, item in enumerate(daq_item):
                self.ui.daqTableWidget.setItem(
                    ridx, cidx, QtWidgets.QTableWidgetItem(str(item))
                )
