"""
This is a simple test file for working out how to use PyQt5 for our Schrodinger's Hack project.

This file creates a simple window application.

Author: Kondapuram Aditya Seshadri
Date: October 24, 2020
"""

# importing the required modules from PyQt5 as well as sys for exit functionality
import sys
from PyQt5.QtWidgets import QApplication, QWidget

# The main constructor is called at the run time of the program, it creates the
# application window and it's widgets as objects
def main():
    # instances of the application window (with arguments from the console as parameters) and widget are declared
    app = QApplication(sys.argv)
    w = QWidget()

    # alters the application window
    w.resize(1080, 900)
    w.move(0, 0)
    w.setWindowTitle('Interactive Scattering Program')

    # displays the application window
    w.show()

    # calls app.exec_() which runs the main loop of the application
    # The main loop receives events from the window system, relays them to application widgets
    # The main loop ends if exit() is called or the main widget is stopped
    # sys.exit() ensures a clean exit of the application
    sys.exit(app.exec_())

# Python has special variables that are initialized at the beginning of a program, one of which is __init__
# It is assigned to equal '__main__' because this is the main file for the program being used
if __name__ == '__main__':
    # main() is run at the beginning of the program iff this is the main file of the program
    main()
