#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""

Mainteiner: Pavel Liferenko (https://t.me/Liferenko)

Description:
This module collect SQL callbacks and show results in small window. 

Project progress you can see here - https://github.com/Liferenko/pyqt_test_task/projects/

Last edited: March 2018
"""
import random
import sys
from PyQt5.QtWidgets import QAbstractItemView, QTableView, QApplication, QWidget
from PyQt5.QtGui import QStandardItem, QIcon, QStandardItemModel



class Result_window(QWidget):
	def __init__(self):
		super().__init__()
		# OLD self.initUI()
		
		self.table = QTableView(self)
		self.table.setGeometry(0, 0, 400, 300)
		self.model = QStandardItemModel(self)
		self.table.setModel(self.model)
		self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.populate()

		self.table.doubleClicked.connect(self.on_click)		

	def on_click(self, signal):
		row = signal.row()
		column = signal.column()
		cell_dict = self.model.itemData(signal)
		cell_value = cell_dict.get(0)

		index = signal.sibling(row, 0)
		index_dict = self.model.itemData(index)
		index_value = index_dict.get(0)
		print( "Row {}, \nColumn {}, \n clicked - value: {} \nColumn 1 contents: {} \n \n ---- \n \n".format(row, \
				column, \
				cell_value, \
				index_value) )
		
	def populate(self):
		values = []
		for i in range(10):
			sub_values = []
			for i in range(4):
				value = random.randrange(1, 100)
				sub_values.append(value)
			values.append(sub_values)
		for value in values:
			row = []
			for item in value:
				cell = QStandardItem( str(item) )
				row.append(cell)
			self.model.appendRow(row)

		self.show()	



	def initUI(self):
		self.setGeometry(0, 500, 640, 480) #TODO calibrate coordinates
		self.setWindowTitle( "Result of SQL callbacks" )
		self.setWindowIcon( QIcon('result.png') )
		self.show()
		



if __name__ == '__main__':
	result_app = QApplication(sys.argv)
	result_window = Result_window()

	sys.exit(result_app.exec_())
