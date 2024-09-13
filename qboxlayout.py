#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:39:43 2024

@author: ercan
"""

import sys
from PyQt5 import QtWidgets

def source():
    object=QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QWidget()
    
    window.setWindowTitle("PyQt5 Study Window") #window title
    window.setGeometry(250,300,600,300) #(xpos,ypos,width,height)
    
    button1=QtWidgets.QPushButton(window) #adding a pushbutton
    button2=QtWidgets.QPushButton(window)
    button3=QtWidgets.QPushButton(window)
    button4=QtWidgets.QPushButton(window)
    
    button1.setText("Button 1") #name the pushbutton
    button2.setText("Button 2")
    button3.setText("Button 3")
    button4.setText("Button 4")
    
    vertical=QtWidgets.QVBoxLayout() # qbox vertical object
    horizontal=QtWidgets.QHBoxLayout() # qbox horizontal  object
    vertical.addWidget(button1)   #making widget arrangable by layout
    vertical.addWidget(button2)
    horizontal.addWidget(button3)
    horizontal.addWidget(button4)
    
    vertical.addLayout(horizontal) # adding a horizontal layout inside vertical layout
    
    window.setLayout(vertical) #give window a min scale, order pushbuttons, scale the window when user resize it
    
    window.show()   
    sys.exit(object.exec_())
source()