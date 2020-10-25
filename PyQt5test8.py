"""
This is a simple test file for working out how to use PyQt5 for our Schrodinger's Hack project.

This file simply creates a window application with a menu bar with additional submenus.

Author: Kondapuram Aditya Seshadri
Date: October 24, 2020
"""

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QStackedLayout,
                             QWidget, QPalette, QColor)


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        # Comment
        stacklayout = QStackedLayout()

        stacklayout.addWidget(Color('red'))
        stacklayout.addWidget(Color('green'))
        stacklayout.addWidget(Color('blue'))
        stacklayout.addWidget(Color('yellow'))

        stacklayout.setCurrentIndex(3)

        widget = QWidget()
        widget.setLayout(stacklayout)

        self.setGeometry(0, 0, 1440, 1080)
        self.setWindowTitle('Stack Layout')
        self.show()

class Color(QWidget):

    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
