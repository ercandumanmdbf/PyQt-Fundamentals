#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 21:58:55 2024

@author: ercan
"""

import sys
from PyQt5 import QtWidgets

def source():
    object=QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QWidget()
    
    window.setWindowTitle("PyQt5 Study Window") #window title
    window.setGeometry(250,300,600,300) #(xpos,ypos,width,height)
    
    line=QtWidgets.QLineEdit(pencere) #Q Line Edit
    line.setText("Default") #default line text
    line.setReadOnly(False) #Disable to change parameter inside Pyqt Window
    line.move(200,10)
    
    window.show()   
    sys.exit(object.exec_())
source()