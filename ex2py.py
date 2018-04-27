# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 19:05:24 2018

@author: Administrator
"""

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
class Ex2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
    def initUi(self):
        lbl1 = QLabel('zetcode',self)
        lbl1.move(250,10)
        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)
        
        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)            
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('绝度窗口')
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ex2()
    sys.exit(app.exec_())