# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
        self.actionSave_figure = QAction(MainWindow)
        self.actionSave_figure.setObjectName(u"actionSave_figure")
        self.actionCheck_DAQ = QAction(MainWindow)
        self.actionCheck_DAQ.setObjectName(u"actionCheck_DAQ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.figLayout = GraphicsLayoutWidget(self.centralwidget)
        self.figLayout.setObjectName(u"figLayout")
        self.figLayout.setAutoFillBackground(False)
        self.gridLayout_4 = QGridLayout(self.figLayout)
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        self.gridLayout.addWidget(self.figLayout, 1, 0, 1, 1)

        self.topwidget = QWidget(self.centralwidget)
        self.topwidget.setObjectName(u"topwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topwidget.sizePolicy().hasHeightForWidth())
        self.topwidget.setSizePolicy(sizePolicy)
        self.topwidget.setMaximumSize(QSize(16777215, 40))
        self.gridLayout_2 = QGridLayout(self.topwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.signalsLabel = QLabel(self.topwidget)
        self.signalsLabel.setObjectName(u"signalsLabel")

        self.gridLayout_2.addWidget(self.signalsLabel, 0, 15, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 14, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.filterCheckbox = QCheckBox(self.topwidget)
        self.filterCheckbox.setObjectName(u"filterCheckbox")

        self.gridLayout_2.addWidget(self.filterCheckbox, 0, 8, 1, 1)

        self.downsampleBox = QCheckBox(self.topwidget)
        self.downsampleBox.setObjectName(u"downsampleBox")
        self.downsampleBox.setChecked(True)

        self.gridLayout_2.addWidget(self.downsampleBox, 0, 5, 1, 1)

        self.label_8 = QLabel(self.topwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 0, 9, 1, 1)

        self.lastShotButton = QPushButton(self.topwidget)
        self.lastShotButton.setObjectName(u"lastShotButton")

        self.gridLayout_2.addWidget(self.lastShotButton, 0, 3, 1, 1)

        self.refreshButton = QPushButton(self.topwidget)
        self.refreshButton.setObjectName(u"refreshButton")

        self.gridLayout_2.addWidget(self.refreshButton, 0, 18, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 7, 1, 1)

        self.loadDataButton = QPushButton(self.topwidget)
        self.loadDataButton.setObjectName(u"loadDataButton")

        self.gridLayout_2.addWidget(self.loadDataButton, 0, 2, 1, 1)

        self.downsampleFactorBox = QLineEdit(self.topwidget)
        self.downsampleFactorBox.setObjectName(u"downsampleFactorBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.downsampleFactorBox.sizePolicy().hasHeightForWidth())
        self.downsampleFactorBox.setSizePolicy(sizePolicy1)
        self.downsampleFactorBox.setMinimumSize(QSize(50, 22))
        self.downsampleFactorBox.setMaximumSize(QSize(50, 22))
        self.downsampleFactorBox.setBaseSize(QSize(20, 0))
        self.downsampleFactorBox.setAlignment(Qt.AlignCenter)
        self.downsampleFactorBox.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.downsampleFactorBox, 0, 6, 1, 1)

        self.filterFMin = QLineEdit(self.topwidget)
        self.filterFMin.setObjectName(u"filterFMin")
        sizePolicy1.setHeightForWidth(self.filterFMin.sizePolicy().hasHeightForWidth())
        self.filterFMin.setSizePolicy(sizePolicy1)
        self.filterFMin.setMinimumSize(QSize(20, 0))
        self.filterFMin.setMaximumSize(QSize(40, 16777215))
        self.filterFMin.setBaseSize(QSize(40, 0))

        self.gridLayout_2.addWidget(self.filterFMin, 0, 10, 1, 1)

        self.label = QLabel(self.topwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.filterFMax = QLineEdit(self.topwidget)
        self.filterFMax.setObjectName(u"filterFMax")
        sizePolicy1.setHeightForWidth(self.filterFMax.sizePolicy().hasHeightForWidth())
        self.filterFMax.setSizePolicy(sizePolicy1)
        self.filterFMax.setMinimumSize(QSize(20, 0))
        self.filterFMax.setMaximumSize(QSize(40, 16777215))
        self.filterFMax.setBaseSize(QSize(40, 0))

        self.gridLayout_2.addWidget(self.filterFMax, 0, 12, 1, 1)

        self.signalArraySelector = QComboBox(self.topwidget)
        self.signalArraySelector.setObjectName(u"signalArraySelector")
        self.signalArraySelector.setEditable(True)
        self.signalArraySelector.setMaxVisibleItems(20)
        self.signalArraySelector.setInsertPolicy(QComboBox.NoInsert)

        self.gridLayout_2.addWidget(self.signalArraySelector, 0, 16, 1, 1)

        self.label_9 = QLabel(self.topwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 0, 11, 1, 1)

        self.label_10 = QLabel(self.topwidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 0, 13, 1, 1)

        self.shotNumberInput = QLineEdit(self.topwidget)
        self.shotNumberInput.setObjectName(u"shotNumberInput")
        self.shotNumberInput.setMaximumSize(QSize(80, 22))

        self.gridLayout_2.addWidget(self.shotNumberInput, 0, 1, 1, 1)

        self.checkDAQButton = QPushButton(self.topwidget)
        self.checkDAQButton.setObjectName(u"checkDAQButton")
        self.checkDAQButton.setMinimumSize(QSize(40, 0))
        self.checkDAQButton.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_2.addWidget(self.checkDAQButton, 0, 19, 1, 1)


        self.gridLayout.addWidget(self.topwidget, 0, 0, 1, 1)

        self.bottomwidget = QWidget(self.centralwidget)
        self.bottomwidget.setObjectName(u"bottomwidget")
        sizePolicy.setHeightForWidth(self.bottomwidget.sizePolicy().hasHeightForWidth())
        self.bottomwidget.setSizePolicy(sizePolicy)
        self.bottomwidget.setMaximumSize(QSize(16777215, 40))
        self.gridLayout_3 = QGridLayout(self.bottomwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_5 = QLabel(self.bottomwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_5, 1, 6, 1, 1)

        self.lowerTLim = QLineEdit(self.bottomwidget)
        self.lowerTLim.setObjectName(u"lowerTLim")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lowerTLim.sizePolicy().hasHeightForWidth())
        self.lowerTLim.setSizePolicy(sizePolicy2)
        self.lowerTLim.setMinimumSize(QSize(70, 22))
        self.lowerTLim.setMaximumSize(QSize(70, 22))
        self.lowerTLim.setBaseSize(QSize(70, 22))
        self.lowerTLim.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lowerTLim, 1, 5, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.integrateDataButton = QPushButton(self.bottomwidget)
        self.integrateDataButton.setObjectName(u"integrateDataButton")

        self.gridLayout_3.addWidget(self.integrateDataButton, 1, 0, 1, 1)

        self.label_3 = QLabel(self.bottomwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_3, 1, 4, 1, 1)

        self.seeAloneButton = QPushButton(self.bottomwidget)
        self.seeAloneButton.setObjectName(u"seeAloneButton")

        self.gridLayout_3.addWidget(self.seeAloneButton, 1, 15, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 1, 12, 1, 1)

        self.upperTLim = QLineEdit(self.bottomwidget)
        self.upperTLim.setObjectName(u"upperTLim")
        self.upperTLim.setMinimumSize(QSize(70, 22))
        self.upperTLim.setMaximumSize(QSize(70, 22))
        self.upperTLim.setBaseSize(QSize(70, 22))
        self.upperTLim.setAlignment(Qt.AlignCenter)
        self.upperTLim.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.upperTLim, 1, 7, 1, 1)

        self.fftButton = QPushButton(self.bottomwidget)
        self.fftButton.setObjectName(u"fftButton")
        self.fftButton.setMinimumSize(QSize(50, 0))
        self.fftButton.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_3.addWidget(self.fftButton, 1, 1, 1, 1)

        self.coilDataRetrievalSelector = QComboBox(self.bottomwidget)
        self.coilDataRetrievalSelector.setObjectName(u"coilDataRetrievalSelector")

        self.gridLayout_3.addWidget(self.coilDataRetrievalSelector, 1, 14, 1, 1)

        self.spectrogramsButton = QPushButton(self.bottomwidget)
        self.spectrogramsButton.setObjectName(u"spectrogramsButton")

        self.gridLayout_3.addWidget(self.spectrogramsButton, 1, 3, 1, 1)

        self.singleSpectrogramButton = QPushButton(self.bottomwidget)
        self.singleSpectrogramButton.setObjectName(u"singleSpectrogramButton")

        self.gridLayout_3.addWidget(self.singleSpectrogramButton, 1, 16, 1, 1)

        self.spgramNperseg = QLineEdit(self.bottomwidget)
        self.spgramNperseg.setObjectName(u"spgramNperseg")
        self.spgramNperseg.setMaximumSize(QSize(70, 22))
        self.spgramNperseg.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.spgramNperseg, 1, 9, 1, 1)

        self.label_6 = QLabel(self.bottomwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 8, 1, 1)

        self.spgramNoverlap = QLineEdit(self.bottomwidget)
        self.spgramNoverlap.setObjectName(u"spgramNoverlap")
        sizePolicy2.setHeightForWidth(self.spgramNoverlap.sizePolicy().hasHeightForWidth())
        self.spgramNoverlap.setSizePolicy(sizePolicy2)
        self.spgramNoverlap.setMinimumSize(QSize(70, 22))
        self.spgramNoverlap.setMaximumSize(QSize(70, 22))
        self.spgramNoverlap.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.spgramNoverlap, 1, 11, 1, 1)

        self.label_7 = QLabel(self.bottomwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 1, 10, 1, 1)

        self.label_4 = QLabel(self.bottomwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_4, 1, 13, 1, 1)


        self.gridLayout.addWidget(self.bottomwidget, 2, 0, 1, 1)

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
        self.menuArchivo.addAction(self.actionCheck_DAQ)
        self.menuArchivo.addAction(self.actionSave_figure)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TJII Data Explorer", None))
        self.actionSave_figure.setText(QCoreApplication.translate("MainWindow", u"Save figure", None))
        self.actionCheck_DAQ.setText(QCoreApplication.translate("MainWindow", u"Check DAQ", None))
        self.signalsLabel.setText(QCoreApplication.translate("MainWindow", u"Signals: ", None))
        self.filterCheckbox.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.downsampleBox.setText(QCoreApplication.translate("MainWindow", u"Downsample:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>f<span style=\" vertical-align:sub;\">min</span></p></body></html>", None))
        self.lastShotButton.setText(QCoreApplication.translate("MainWindow", u"Last shot", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.loadDataButton.setText(QCoreApplication.translate("MainWindow", u"Load data", None))
        self.downsampleFactorBox.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.downsampleFactorBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Factor", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Shot:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>f<span style=\" vertical-align:sub;\">max</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>[kHz]</p></body></html>", None))
        self.checkDAQButton.setText(QCoreApplication.translate("MainWindow", u"DAQ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"t<sub>1</sub>:", None))
        self.lowerTLim.setText(QCoreApplication.translate("MainWindow", u"1050", None))
        self.lowerTLim.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Lower limit [ms]", None))
        self.integrateDataButton.setText(QCoreApplication.translate("MainWindow", u"Integrate", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"t<sub>0</sub>:", None))
        self.seeAloneButton.setText(QCoreApplication.translate("MainWindow", u"See alone", None))
        self.upperTLim.setText(QCoreApplication.translate("MainWindow", u"1250", None))
        self.upperTLim.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Upper limit [ms]", None))
        self.fftButton.setText(QCoreApplication.translate("MainWindow", u"FFT", None))
        self.spectrogramsButton.setText(QCoreApplication.translate("MainWindow", u"Spectrograms", None))
        self.singleSpectrogramButton.setText(QCoreApplication.translate("MainWindow", u"Spectrogram", None))
        self.spgramNperseg.setText(QCoreApplication.translate("MainWindow", u"512", None))
        self.spgramNperseg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"nperseg", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"nperseg:", None))
        self.spgramNoverlap.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.spgramNoverlap.setPlaceholderText(QCoreApplication.translate("MainWindow", u"noverlap", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"noverlap:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Signal:", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Actions", None))
    # retranslateUi

