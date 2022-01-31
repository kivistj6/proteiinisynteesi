import sys
from PyQt5.QtWidgets import QApplication
from gui import UI

def main():

    gui = QApplication(sys.argv)
    ui_view = UI()
    sys.exit(gui.exec())


main()
