#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 22:10:10 2024

@author: ercan
"""

import sys
from PyQt5 import QtWidgets

def source():
    object=QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QWidget()
    
    window.setWindowTitle("PyQt5 Study Window") #window title
    window.setGeometry(250,300,600,300) #(xpos,ypos,width,height)
    
    radio1=QtWidgets.QRadioButton(pencere) #adding radio button on window
    radio2=QtWidgets.QRadioButton(pencere)
    
    radio1.setText("On")
    radio2.setText("Off")
    
    radio1.move(200,200) #move a element to desired coordinate on window
    radio2.move(200,220)
    
    radio2.setCheckable(False) #make radio button uncheckable
    
    window.show()   
    sys.exit(object.exec_())
source()