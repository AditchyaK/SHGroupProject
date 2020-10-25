"""
This is a simple test file for working out how to use PyQt5 for our Schrodinger's Hack project.

This file simply creates a window application with a menu bar with additional submenus.

Author: Kondapuram Aditya Seshadri
Date: October 24, 2020
"""

# Importing all required dependencies
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication

# This class creates and modifies the window
class Example(QMainWindow):
    # This is run at the initialization of a new instance of Eaxmple()
    def __init__(self):
        super().__init__()
        self.initUI()

        # Modifies the properties of the window
    def initUI(self):
        # menuBar element is created and is not part of the native Mac menubar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        # A 'File' option is created in menubar
        fileMenu = menubar.addMenu('File')

        # An 'Import' option is created and attached to a QAction
        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        # A new action is created
        newAct = QAction('New', self)

        # Both the action and import option are attached to the 'File' option
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        # Modifies the size of the window
        self.setGeometry(0, 0, 1440, 1080)
        self.setWindowTitle('Menu Test')

        # Displays the window
        self.show()

# main() is run at initialization
def main():
    app = QApplication(sys.argv)
    win = Example()
    sys.exit(app.exec_())

# runs main() at initialization of this file
if __name__ == '__main__':
    main()
