from gui.main_gui import create_main_window
from PyQt6.QtWidgets import QApplication
import sys

def main():
    app = QApplication(sys.argv)
    window = create_main_window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
