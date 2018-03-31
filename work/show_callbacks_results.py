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
from PyQt5.QtCore import QDateTime, QTimeZone, Qt
from PyQt5.QtWidgets import QApplication, QWidget

now = QDateTime.currentDateTime()
print( "Time zone: {0}".format(now.timeZoneAbbreviation()) )

if now.isDaylightTime():
	print( "The date falls inte DST time" )
else:
	print( "The date does not fall into DST time" )

if __name__ == '__main__':
	result_app = QApplication(sys.argv)

	main_window = QWidget()
	main_window.resize(250, 150)
	main_window.move(300, 300)
	main_window.setWindowTitle( "Result of SQL callbacks" )
	main_window.show()

	sys.exit(result_app.exec_())
