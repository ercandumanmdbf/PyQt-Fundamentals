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
    
    qgridlayout=QtWidgets.QGridLayout() #creating a grid object
    
    
    qgridlayout.addWidget(button1,1,1)   #making widget arrangable by layout (object,row,column)
    qgridlayout.addWidget(button2,1,2)
    qgridlayout.addWidget(button3,2,1)
    qgridlayout.addWidget(button4,2,2)
    
    
    
    window.setLayout(qgridlayout) #give window a min scale, order pushbuttons, scale the window when user resize it
    
    window.show()   
    sys.exit(object.exec_())
source()