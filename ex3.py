# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 19:11:36 2018

@author: Administrator
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication)


class Ex3(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        okButton = QPushButton('OK')
        
        #cancelButton = QPushButton("Cancle")
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        #hbox.addWidget(cancelButton)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')    
        self.show()        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Ex3()
    sys.exit(app.exec_())