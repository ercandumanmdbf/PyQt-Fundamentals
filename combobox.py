#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:22:54 2024

@author: ercan
"""

import sys
from PyQt5 import QtWidgets

def source():
    object=QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QWidget()
    
    window.setWindowTitle("PyQt5 Study Window") #window title
    window.setGeometry(250,300,600,300) #(xpos,ypos,width,height)
    
    combo=QtWidgets.QComboBox(window) #adding combobox on window
    combo.addItem("Option1") # add option on combobox
    combo.addItem("Option2")
    combo.addItem("Option3")
    combo.addItem("Option4")
    combo.move(200,100)
    
    window.show()   
    sys.exit(object.exec_())
source()