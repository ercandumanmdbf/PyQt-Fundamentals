#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:19:45 2024

@author: ercan
"""


import sys
from PyQt5 import QtWidgets

def source():
    object=QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QWidget()
    
    window.setWindowTitle("PyQt5 Study Window") #window title
    window.setGeometry(250,300,600,300) #(xpos,ypos,width,height)
    
    checkbox1=QtWidgets.QCheckBox(window) # adding checkbox button on window
    checkbox2=QtWidgets.QCheckBox(window)
    checkbox3=QtWidgets.QCheckBox(window)
    
    checkbox1.setText("Check1")
    checkbox2.setText("Check2")
    checkbox3.setText("Check3")
    
    checkbox1.move(250,100)
    checkbox2.move(250,120)
    checkbox3.move(250,140)
    
    window.show()   
    sys.exit(object.exec_())
source()