#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""

Mainteiner: Pavel Liferenko (https://t.me/Liferenko)

Description:
This module collect SQL callbacks and show results in small window. 

Project progress you can see here - https://github.com/Liferenko/pyqt_test_task/projects/

Last edited: March 2018
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Result_window(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):
		self.setGeometry(0, 500, 620, 240) #TODO calibrate coordinates
		self.setWindowTitle( "Result of SQL callbacks" )
		self.setWindowIcon( QIcon('result.png') )
		self.show()
		

if __name__ == '__main__':
	result_app = QApplication(sys.argv)
	result_window = Result_window()

	sys.exit(result_app.exec_())
	exit()
