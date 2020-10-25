"""
This is a simple test file for working out how to use PyQt5 for our Schrodinger's Hack project.

This file simply creates a window application with a status bar (with a message).

Author: Kondapuram Aditya Seshadri
Date: October 24, 2020
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget

# A class for the application window inheriting QMainWindow
class MainWindow(QMainWindow):
    # run at initialization, runs initialization of QMainWindow and calls initUI()
    def __init__(self):
        super().__init__()
        self.initUI()

    # initUI alters the UI elements on screen
    def initUI(self):
        # Creates bottom text status bar
        self.statusBar().showMessage('Ready')

        # changes the windows size and displays the window
        self.setGeometry(0, 0, 1440, 1080)
        self.show()

# Runs at initialization of file
def main():
    app = QApplication(sys.argv)
    win = MainWindow()

    # exits safely
    sys.exit(app.exec_())

# runs main() at initialization
if __name__ == '__main__':
    main()
