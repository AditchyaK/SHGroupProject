"""
This is a simple test file for working out how to use PyQt5 for our Schrodinger's Hack project.

This file simply creates a window application with a label.

Author: Kondapuram Aditya Seshadri
Date: October 24, 2020
"""

# Importing all required dependencies
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel

# This class creates and modifies the window
class Example(QWidget):
    # This is run at the initialization of a new instance of Eaxmple()
    def __init__(self):
        super().__init__()
        self.initUI()

        # Modifies the properties of the window
    def initUI(self):
        # Creates a label (test) inside the window
        lbl1 = QLabel('Hello', self)
        # Moves the label to the appropriate position
        lbl1.move(15, 10)

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
