#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:29:26 2024

@author: ercan
"""

import sys
from PyQt5 import QtWidgets

def source():
    object=QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QWidget()
    
    window.setWindowTitle("PyQt5 Study Window") #window title
    window.setGeometry(250,300,600,300) #(xpos,ypos,width,height)
    
    line=QtWidgets.QLineEdit(window) #Q Line Edit
    line.setText("Not Saved")
    line.setReadOnly(False) #Disable to change parameter inside Pyqt Window
    line.move(200,10)
    button=QtWidgets.QPushButton(window)
    button.move(200,40)
    button.setText("Save")
    
    def update():
        line.setText("Saved")
        
    button.clicked.connect(update)
    
    window.show()   
    sys.exit(object.exec_())
source()