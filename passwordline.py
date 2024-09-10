#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 22:04:55 2024

@author: ercan
"""

import sys
from PyQt5 import QtWidgets

def source():
    object=QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QWidget()
    
    window.setWindowTitle("PyQt5 Study Window") #window title
    window.setGeometry(250,300,600,300) #(xpos,ypos,width,height)
    
    password=QtWidgets.QLineEdit(window) #adding line 
    password.setEchoMode(QtWidgets.QLineEdit.Password) #disable line with password protection
    password.move(100,100) #move element desirable position
    
    window.show()   
    sys.exit(object.exec_())
source()