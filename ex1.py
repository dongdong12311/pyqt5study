# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 16:02:31 2018

@author: Administrator
"""
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
class Ex1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
    def initUi(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("sadf")
        self.setWindowIcon(QIcon('1.png'))
        self.show()
        
app = QApplication(sys.argv)
ex = Ex1()
sys.exit(app.exec_())