import PyQt6 as qt

# from PyQt6 import QtCore, QtWidgets
from pyqtgraph import PlotWidget, plot
import sys  # We need sys so that we can pass argv to QApplication
from main_window import MainWindow


def main():
    app = qt.QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
