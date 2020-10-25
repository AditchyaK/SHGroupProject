"""
This is a simple test file for working out how to use PyQt5 for our Schrodinger's Hack project.

This file simply creates a window application with a menu bar with additional submenus.

Author: Kondapuram Aditya Seshadri
Date: October 24, 2020
"""

# Importing all required dependencies
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout

# This class creates and modifies the window
class Example(QWidget):
    # This is run at the initialization of a new instance of Eaxmple()
    def __init__(self):
        super().__init__()
        self.initUI()

        # Modifies the properties of the window
    def initUI(self):
        # Creates instances of QPushButton with their own labels (these are buttons on the screen)
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")

        # Creates an instance of QHBoxLayout (horizonal box layout)
        hbox = QHBoxLayout()

        # Adds a strechable space before (to the left of) the two buttons
        hbox.addStretch(1)
        hbox.addWidget(button1)
        hbox.addWidget(button2)

        #
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

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
