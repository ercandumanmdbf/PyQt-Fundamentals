#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 22:07:39 2024

@author: ercan
"""

import sys
from PyQt5 import QtWidgets

def source():
    object=QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QWidget()
    
    window.setWindowTitle("PyQt5 Study Window") #window title
    window.setGeometry(250,300,600,300) #(xpos,ypos,width,height)
    
    button=QtWidgets.QPushButton(window) #adding button on window
    button.setText("Push") #button text
    button.setGeometry(40,50,100,20) #(xpos,ypos,lenght,height) (button geometry,both move and size)
    
    window.show()   
    sys.exit(object.exec_())
source()