#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""

Mainteiner: Pavel Liferenko (https://t.me/Liferenko)

Description:
This module collect SQL callbacks and show results in small window. 

Project progress you can see here - https://github.com/Liferenko/pyqt_test_task/projects/

Last edited: March 2018
"""

from PyQt5.QtCore import QDateTime, QTimeZone, Qt

now = QDateTime.currentDateTime()
print( "Time zone: {0}".format(now.timeZoneAbbreviation()) )

if now.isDaylightTime():
	print( "The date falls inte DST time" )
else:
	print( "The date does not fall into DST time" )
