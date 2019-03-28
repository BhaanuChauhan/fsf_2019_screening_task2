# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 23:00:54 2019

@author: BHANU
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAction

class Fossee(QtWidgets.QMainWindow):

    def __init__(self):
        super(Fossee, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Graph Plot")
        mainMenu = self.menuBar()
        fileMenu=mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")
        loadData = fileMenu.addMenu("Load")
        editData= editMenu.addMenu("Edit Data")
        addData=fileMenu.addMenu("Add Data")
        saveData=fileMenu.addMenu("Save as png")
        exitButton= QAction("Exit",self)
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
        self.show()

app = QtWidgets.QApplication(sys.argv)
GUI = Fossee()
sys.exit(app.exec_())
