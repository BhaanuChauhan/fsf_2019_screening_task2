# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 23:00:54 2019

@author: BHANU
"""

import sys
from PyQt4 import QtGui

class Fossee(QtGui.QMainWindow):

    def __init__(self):
        super(Fossee, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.show()

app = QtGui.QApplication(sys.argv)
GUI = Fossee()
sys.exit(app.exec_())