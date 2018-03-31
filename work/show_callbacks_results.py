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
from PyQt5.QtWidgets import QAbstractItemView, QTableView, QApplication, QWidget
from PyQt5.QtGui import QIcon, QStandardItemModel



class Result_window(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
		
		# TODO Create callback results table
		self.table = QTableView(self)
		self.table.setGeometry(0, 0, 400, 300)
		self.model = QStandardItemModel(self)
		self.table.setModel(self.model)
		self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
		# self.populate()

		# self.table.doubleClicked.connect(self.on_click)		

 
	def initUI(self):
		self.setGeometry(0, 500, 640, 480) #TODO calibrate coordinates
		self.setWindowTitle( "Result of SQL callbacks" )
		self.setWindowIcon( QIcon('result.png') )
		self.show()
		



if __name__ == '__main__':
	result_app = QApplication(sys.argv)
	result_window = Result_window()

	sys.exit(result_app.exec_())
