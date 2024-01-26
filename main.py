from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from pyqtgraph import PlotWidget, plot
import sys  # We need sys so that we can pass argv to QApplication
from src.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
