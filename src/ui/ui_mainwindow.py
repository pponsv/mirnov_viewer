# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QWidget)

from pyqtgraph import GraphicsLayoutWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QSize(1200, 800))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.topwidget = QWidget(self.centralwidget)
        self.topwidget.setObjectName(u"topwidget")
        self.gridLayout_2 = QGridLayout(self.topwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 7, 1, 1)

        self.refreshButton = QPushButton(self.topwidget)
        self.refreshButton.setObjectName(u"refreshButton")

        self.gridLayout_2.addWidget(self.refreshButton, 0, 13, 1, 1)

        self.lastShotButton = QPushButton(self.topwidget)
        self.lastShotButton.setObjectName(u"lastShotButton")

        self.gridLayout_2.addWidget(self.lastShotButton, 0, 3, 1, 1)

        self.label_2 = QLabel(self.topwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 10, 1, 1)

        self.label = QLabel(self.topwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.downsampleFactorBox = QLineEdit(self.topwidget)
        self.downsampleFactorBox.setObjectName(u"downsampleFactorBox")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downsampleFactorBox.sizePolicy().hasHeightForWidth())
        self.downsampleFactorBox.setSizePolicy(sizePolicy)
        self.downsampleFactorBox.setMinimumSize(QSize(80, 22))
        self.downsampleFactorBox.setMaximumSize(QSize(80, 22))
        self.downsampleFactorBox.setBaseSize(QSize(20, 0))
        self.downsampleFactorBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.downsampleFactorBox.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.downsampleFactorBox, 0, 6, 1, 1)

        self.loadDataButton = QPushButton(self.topwidget)
        self.loadDataButton.setObjectName(u"loadDataButton")

        self.gridLayout_2.addWidget(self.loadDataButton, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.shotNumberInput = QLineEdit(self.topwidget)
        self.shotNumberInput.setObjectName(u"shotNumberInput")
        self.shotNumberInput.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.shotNumberInput, 0, 1, 1, 1)

        self.downsampleBox = QCheckBox(self.topwidget)
        self.downsampleBox.setObjectName(u"downsampleBox")
        self.downsampleBox.setChecked(True)

        self.gridLayout_2.addWidget(self.downsampleBox, 0, 5, 1, 1)

        self.signalArraySelector = QComboBox(self.topwidget)
        self.signalArraySelector.setObjectName(u"signalArraySelector")
        self.signalArraySelector.setEditable(False)

        self.gridLayout_2.addWidget(self.signalArraySelector, 0, 11, 1, 1)

        self.DAQButton = QPushButton(self.topwidget)
        self.DAQButton.setObjectName(u"DAQButton")

        self.gridLayout_2.addWidget(self.DAQButton, 0, 8, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 0, 9, 1, 1)


        self.gridLayout.addWidget(self.topwidget, 0, 0, 1, 1)

        self.bottomwidget = QWidget(self.centralwidget)
        self.bottomwidget.setObjectName(u"bottomwidget")
        self.gridLayout_3 = QGridLayout(self.bottomwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.coilDataRetrievalSelector = QComboBox(self.bottomwidget)
        self.coilDataRetrievalSelector.setObjectName(u"coilDataRetrievalSelector")

        self.gridLayout_3.addWidget(self.coilDataRetrievalSelector, 1, 10, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 1, 6, 1, 1)

        self.lowerTLim = QLineEdit(self.bottomwidget)
        self.lowerTLim.setObjectName(u"lowerTLim")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lowerTLim.sizePolicy().hasHeightForWidth())
        self.lowerTLim.setSizePolicy(sizePolicy1)
        self.lowerTLim.setMinimumSize(QSize(90, 22))
        self.lowerTLim.setMaximumSize(QSize(90, 22))
        self.lowerTLim.setBaseSize(QSize(100, 22))

        self.gridLayout_3.addWidget(self.lowerTLim, 1, 4, 1, 1)

        self.integrateDataButton = QPushButton(self.bottomwidget)
        self.integrateDataButton.setObjectName(u"integrateDataButton")

        self.gridLayout_3.addWidget(self.integrateDataButton, 1, 0, 1, 1)

        self.spectrogramsButton = QPushButton(self.bottomwidget)
        self.spectrogramsButton.setObjectName(u"spectrogramsButton")

        self.gridLayout_3.addWidget(self.spectrogramsButton, 1, 3, 1, 1)

        self.upperTLim = QLineEdit(self.bottomwidget)
        self.upperTLim.setObjectName(u"upperTLim")
        self.upperTLim.setMinimumSize(QSize(90, 22))
        self.upperTLim.setMaximumSize(QSize(90, 22))
        self.upperTLim.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.upperTLim, 1, 5, 1, 1)

        self.saveButton = QPushButton(self.bottomwidget)
        self.saveButton.setObjectName(u"saveButton")

        self.gridLayout_3.addWidget(self.saveButton, 1, 13, 1, 1)

        self.fftButton = QPushButton(self.bottomwidget)
        self.fftButton.setObjectName(u"fftButton")

        self.gridLayout_3.addWidget(self.fftButton, 1, 1, 1, 1)

        self.seeAloneButton = QPushButton(self.bottomwidget)
        self.seeAloneButton.setObjectName(u"seeAloneButton")

        self.gridLayout_3.addWidget(self.seeAloneButton, 1, 11, 1, 1)

        self.label_4 = QLabel(self.bottomwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 1, 9, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 12, 1, 1)


        self.gridLayout.addWidget(self.bottomwidget, 2, 0, 1, 1)

        self.figLayout = GraphicsLayoutWidget(self.centralwidget)
        self.figLayout.setObjectName(u"figLayout")
        self.figLayout.setAutoFillBackground(False)
        self.gridLayout_4 = QGridLayout(self.figLayout)
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        self.gridLayout.addWidget(self.figLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 19))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Figures - Mirnov Coil Data Acqusition", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.lastShotButton.setText(QCoreApplication.translate("MainWindow", u"Last shot", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Signals: ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Descarga:", None))
        self.downsampleFactorBox.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.downsampleFactorBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Factor", None))
        self.loadDataButton.setText(QCoreApplication.translate("MainWindow", u"Load data", None))
        self.downsampleBox.setText(QCoreApplication.translate("MainWindow", u"Downsample:", None))
        self.DAQButton.setText(QCoreApplication.translate("MainWindow", u"Check DAQ", None))
        self.lowerTLim.setText(QCoreApplication.translate("MainWindow", u"1050", None))
        self.lowerTLim.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Lower limit [ms]", None))
        self.integrateDataButton.setText(QCoreApplication.translate("MainWindow", u"Integrate", None))
        self.spectrogramsButton.setText(QCoreApplication.translate("MainWindow", u"Spectrograms", None))
        self.upperTLim.setText(QCoreApplication.translate("MainWindow", u"1250", None))
        self.upperTLim.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Upper limit [ms]", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save figure", None))
        self.fftButton.setText(QCoreApplication.translate("MainWindow", u"FFT", None))
        self.seeAloneButton.setText(QCoreApplication.translate("MainWindow", u"See alone", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Signal:", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

