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
    
    label1=QtWidgets.QLabel(window)
    label2=QtWidgets.QLabel(window)
    
    label1.setText("X:")
    label2.setText("Y:")
    
    line1=QtWidgets.QLineEdit(window)
    line2=QtWidgets.QLineEdit(window)
    
    qform=QtWidgets.QFormLayout()
    
    qform.addRow(label1,line1)
    qform.addRow(label2,line2)
    
    window.setLayout(qform)
    
    window.show()   
    sys.exit(object.exec_())
source()