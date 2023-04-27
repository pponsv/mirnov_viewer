from PyQt6 import QtWidgets
from pyqtgraph import PlotWidget, plot
import sys  # We need sys so that we can pass argv to QApplication
from main_window import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
