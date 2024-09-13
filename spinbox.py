#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:43:45 2024

@author: ercan
"""

import sys
from PyQt5 import QtWidgets

def source():
    object=QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QWidget()
    
    window.setWindowTitle("PyQt5 Study Window") #window title
    window.setGeometry(250,300,600,300) #(xpos,ypos,width,height)
    
    spinint=QtWidgets.QSpinBox(window) #adding spinbox on window
    spinint.setRange(100,200) #giving spinbox a max and min value
    spinint.setSingleStep(7) #value change at one spin click
    spinint.move(250,100)
    
    spinfloat=QtWidgets.QDoubleSpinBox(window)
    spinfloat.setRange(0,1)
    #spinfloat.setMaximum(250) #setting maximum value
    #spinfloat.setMinimum(10) #setting minimum value
    spinfloat.setSingleStep(0.04)
    spinfloat.move(250,130)
    
    label1=QtWidgets.QLabel(window)
    label1.setText("Int spinbox +7/-7") #adding text on window
    label1.move(320,105)
    
    label2=QtWidgets.QLabel(window)
    label2.setText("float spinbox +0.04/-0.04") #adding text on window
    label2.move(320,135)
    
    window.show()   
    sys.exit(object.exec_())
source()