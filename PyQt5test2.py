"""
This is a simple test file for working out how to use PyQt5 for our Schrodinger's Hack project.

This file creates a simple window application and centers it on the screen.

Author: Kondapuram Aditya Seshadri
Date: October 24, 2020
"""

# importing the required modules from PyQt5 as well as sys for exit functionality
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtGui import QIcon

# This class "Example" inherits its constructors/functions from the QWidget module
class Example(QWidget):

    # This is called at the initialization of a new instance of the "Example" class
    # "self" returns the method/attribute with its associated INSTANCE, not the overall CLASS
    def __init__(self):
        # This accesses the __init__() method inside the QWidget superclass (hence super())
        super().__init__()

        # This calls the following method inside the "Example"
        # In this case, this calls the initUI() method inside the given instance of this class
        self.initUI()

    def initUI(self):
        # changes the properties of the window by accessing the self attributes
        self.setGeometry(300, 300, 1900, 1080)
        self.setWindowTitle('Icon')

        # centers the spplciation window
        self.center()

        # changes the icon in the top bar of the window
        self.setWindowIcon(QIcon('web.png'))

        # displays the application window
        self.show()

    def center(self):
        # qr is a rectange specifying the geometry of the main window including window frame
        qr = self.frameGeometry()

        # This accesses the screen resolution of the monitor and then the returns the center point
        cp = QDesktopWidget().availableGeometry().center()

        # moves the rectangle to the center of the SCREEN (not the WINDOW)
        qr.moveCenter(cp)

        # moves the window to the top left corner of the screen
        self.move(qr.topLeft())

# The main function is called at the run time of the program
def main():
    # the application is initialized
    app = QApplication(sys.argv)

    # an instance of the Example class is initialized
    ex = Example()

    # starts the main loop and exits safely
    sys.exit(app.exec_())

# Python has special variables that are initialized at the beginning of a program, one of which is __init__
# It is assigned to equal '__main__' because this is the main file for the program being used
if __name__ == '__main__':
    # main() is run at the beginning of the program iff this is the main file of the program
    main()
