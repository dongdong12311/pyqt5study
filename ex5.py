# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 19:25:58 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 19:20:58 2018

@author: Administrator
"""

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, 
    QPushButton, QApplication)
 
 
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        rows = 10
        columns = 10
        names = [''] *(columns*rows)
        
        positions = [(i,j) for i in range(rows) for j in range(columns)]
        for position ,name in zip(positions,names):
            button = QPushButton(name)
            grid.addWidget(button,*position)
        self.move(500, 500)
        self.setWindowTitle('Calculator')
        self.show()
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())