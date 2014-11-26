#!/usr/bin/env python
# encoding: utf-8
"""
minusTide.py

Created by jorma on 2011-12-08.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
import random
import os.path
import urllib2
import smtplib
import email.utils
from email.mime.text import MIMEText
import sys, string, datetime
import os
from xml.etree import ElementTree as ET

#Grab quotes file as an array
f = open('quotes.txt')
quotes = f.readlines()
f.close()

tideHeightStringArray = []
lowestTideHeight = 0.0

def main():
	
	stationDict = {'Bolinas':'9414958'};
	
	
	#create a print option for testing
	#humanTideHeightLow = str(min(tideHeightFloatArray))
	#print "The lowest tide of 2012 is a " + humanTideHeightLow
	
	
	for key, value in stationDict.items():
	
		stationName = key
		stationID = value
		
		#check to see if lowest
		# Create function here to check to see if lowest...
		
		
		#xmlFile = '/home/yosemit1/minustide_scripts/' + stationName + '.xml'
		xmlFile = '/Users/jorma/Code/minustide_python/' + stationName + '.xml'
		
		# --- run main check
		tideCheck(xmlFile,stationName)
		
	
	
	# testing finding the lowest tide
	#print tideHeightStringArray
	print nowMonth
	print "============ End Main ================="
	# turn list from strings into floats
	tideHeightFloatArray = [float(i) for i in tideHeightStringArray]
	

# function to download xml file if it does not exist
def getXmlFile(stationID,stationName):
	u = urllib2.urlopen('http://tidesandcurrents.noaa.gov/noaatidepredictions/NOAATidesFacade.jsp?datatype=Annual+XML&Stationid=' + stationID)
	localFile = open(stationName + '.xml', 'w')
	localFile.write(u.read())
	localFile.close()
	return
	
# function to loop thru tide info
def tideCheck(xmlFile,station):
	
	# --- get tomorrow's date
	tomorrowDate = datetime.date.today() + datetime.timedelta(days=1)
	nowYear = tomorrowDate.year
	nowMonth = tomorrowDate.month
	nowDay = tomorrowDate.day			
	tomorrow = str(nowYear) + "/" + str(nowMonth) + "/" + str(nowDay)
	
	# --- parse xml file
	tree = ET.parse(xmlFile)
	root = tree.getroot().find("data")
	
	# --- loop thru each record
	print "=== " + station + " Minus Tides in 2012 ==="
	print "(Tomorrow is " + tomorrow + ")"
	print "=== "	
	
	for subelement in root:

			lowestTideHeight = 1.0
			tideHeight = subelement.find("predictions_in_ft").text
			tideDate = subelement.find("date").text # ex. 2012/01/20
			tideDay = subelement.find("day").text
			
			tideDateArray = string.split(tideDate,"/")
			
			year = str(tideDateArray[0])
			day = str(tideDateArray[2])
			month = str(tideDateArray[1])
			
			# testing... creating array of 2012 tide heights
			tideHeightStringArray.append(tideHeight)			
			
			tideHeightFloat = float(tideHeight)
			
			if tideHeightFloat < lowestTideHeight:
				lowestTideHeight = tideHeightFloat
				print "The lowest tide is now " + str(lowestTideHeight)
			else:
				pass
				
			
			# testing... 
			#if float(tideHeight) < lowestTideHeight
			#	print "Scooby Doobie Do"
			#else:
			#	pass
			
			
			# ------ Convert tideDay to one digit if it has a zero in front -----
			if day == "01":
				day = "1"
			elif day == "02":
				day = "2"
			elif day == "03":
				day = "3"
			elif day == "04":
				day = "4"
			elif day == "05":
				day = "5"
			elif day == "06":
				day = "6"
			elif day == "07":
				day = "7"
			elif day == "08":
				day = "8"
			elif day == "09":
				day = "9"
			else:
				pass
			
			# ------ Convert tideMonth to one digit if it has a zero in front -----
			if month == "01":
				month = "1"
			elif month == "02":
				month = "2"
			elif month == "03":
				month = "3"
			elif month == "04":
				month = "4"
			elif month == "05":
				month = "5"
			elif month == "06":
				month = "6"
			elif month == "07":
				month = "7"
			elif month == "08":
				month = "8"
			elif month == "09":
				month = "9"
			else:
				pass			
			
			formattedTideDate = year + "/" + month + "/" + day			
			human_tideDate = month + "/" + day + "/" + year
			
			# get tide hour	
			tideTime = subelement.find("time").text
			tideTimeList = string.split(tideTime,":")
			tideTime12hrClockList = string.split(tideTime)
			tideHourList = string.split(tideTimeList[0])
			tide12hrClock = string.split(tideTime12hrClockList[1])
			
			tideHour = int(tideHourList[0])
			
			# ---- Turn hour into 24
			if ((tide12hrClock[0] == "PM") and (tideHour == 12)):
				tideHour = 12
				
			elif ((tide12hrClock[0] == "AM") and (tideHour == 12)):
				tideHour = 0
				
			elif (tide12hrClock[0] == "PM"):
				tideHour = tideHour + 12
				

			# --- find all tides that are lower than -.2 and between 5am and 7pm
			# --------------- change tide height argument
			
			
			# uncomment below for testing
			#print "Compare tideDate vs tomorrow: " + formattedTideDate + " " + tomorrow
			if (float(tideHeight) < 0) & (5 < tideHour < 19):
				print tideHeight + " " + tideDay + ", " + tideDate + " at " + tideTime
				
				
				if formattedTideDate == tomorrow:
					
					emailFolks = {'Jorma': 'aloha@jorma.com'};

					# loop through each subscriber
					for key, value in emailFolks.items():
						print "********Send Email*********"
						#msg = MIMEText('Aloha -\n\n'  + 'There will be a ' + tideHeight + 'ft minus tide on ' + human_tideDate + " at " + tideTime + " in " + station +  "\n\n -Jorma" + "\n\n----\n\n" + random.choice(quotes)) 
						#msg['To'] = email.utils.formataddr((key, value))
						#msg['From'] = email.utils.formataddr(('Jorma', 'jorma@minustide.net'))
						#msg['Subject'] = 'Minus Tide Alert for tomorrow in ' + station + ": " + tideHeight

						#conn = smtplib.SMTP('mail.minustide.net')
						#conn.login('jorma@minustide.net', 'xxxxxxx')
						#conn.sendmail(msg['From'], msg['To'], msg.as_string())
						#conn.quit()
					return
					

	print " "
	
	return

if __name__ == '__main__':
	main()

