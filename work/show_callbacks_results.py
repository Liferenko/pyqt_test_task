#!/usr/bin/python3

from PyQt5.QtCore import QDateTime, QTimeZone, Qt

now = QDateTime.currentDateTime()
print( "Time zone: {0}".format(now.timeZoneAbbreviation()) )

if now.isDaylightTime():
	print( "The date falls inte DST time" )
else:
	print( "The date does not fall into DST time" )
