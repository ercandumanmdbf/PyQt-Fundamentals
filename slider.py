#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:08:29 2024

@author: ercan
"""

import sys
from PyQt5 import QtWidgets,QtCore

def source():
    object=QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QWidget()
    
    window.setWindowTitle("PyQt5 Study Window") #window title
    window.setGeometry(250,300,600,300) #(xpos,ypos,width,height)
    
    slider1=QtWidgets.QSlider(QtCore.Qt.Horizontal,window) #horizontal slider
    slider1.move(220,20)
    slider1.setMinimum(0)
    slider1.setMaximum(100)
    slider1.setTickPosition(QtWidgets.QSlider.TicksBelow) #adding ticks below
    slider1.setTickInterval(10) #adding ticks per 10 interval
    slider1.setValue(50) #preset value of the slider
    
    slider2=QtWidgets.QSlider(QtCore.Qt.Vertical,window) #vertical slider
    slider2.move(220,50)
    slider2.setMaximum(10)
    slider2.setMinimum(0)
    slider2.setValue(9)
    
    window.show()   
    sys.exit(object.exec_())
source()