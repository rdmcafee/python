# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 23:12:43 2021

@author: Mcrye
"""

import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        button = QPushButton("Press Me")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        
        self.setFixedSize(QSize(400,300))
        
        self.setCentralWidget(button)
    def the_button_was_clicked(self):
        print("Clicked")
        
    def the_button_was_toggled(self, checked):
        print("Checked?", checked)
        
app = QApplication(sys.argv)
    
window = MainWindow()
window.show()
    
app.exec_()