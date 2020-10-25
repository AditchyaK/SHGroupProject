"""
This is a simple test file for working out how to use PyQt5 for our Schrodinger's Hack project.

This file simply creates a window application with a menu bar and a status bar.

Author: Kondapuram Aditya Seshadri
Date: October 24, 2020
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    # this is run at initialization of a new instance and also initializes QMainWindow
    # and initUI
    def __init__(self):
        super().__init__()
        self.initUI()

    # initUI initializes all UI elements in the scene/window view
    def initUI(self):
        # QAction is an abstraction of actions performed by menus, toolbars, or with
        # a keyboard shortcut. This exitAct QAction has an Exit label
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)

        # This defines the keyboard shortcut Ctrl+Q (Cmd+Q for Mac) to the exit action and
        # sets it to give the hint that it exits the applciation when you hover hover
        # over the corresponding UI element
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit Application')

        # When this action is triggered, this call will kill the application using qApp
        exitAct.triggered.connect(qApp.quit)

        # creates a status bar
        self.statusBar()

        # Creates a menubar element in the scene
        menubar = self.menuBar()

        # Does not allow the menubar to be the native menubar in MacOS (when an application is
        # selected)
        menubar.setNativeMenuBar(False)

        # creates a file menu option. When clicked, the exit button will appear which will
        # perform the exitAct QAction
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        # Fits the window to my screen
        self.setGeometry(0, 0, 1440, 1080)
        self.setWindowTitle('Menu Bar')

        # Displays the window
        self.show()

# main() is run at initialization
def main():
    app = QApplication(sys.argv)
    win = Example()
    sys.exit(app.exec_())

# this runs main() at initialization from this file only
if __name__ == '__main__':
    main()
