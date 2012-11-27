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

quotes = [
    '"Sponges grow in the ocean. That just kills me. I wonder how much deeper the ocean would be if that didn\'t happen." ~ Steven Wright',
    '"There\'s a fine line between fishing and just standing on the shore like an idiot." ~ Steven Wright',
    '"If you are in a spaceship that is traveling at the speed of light, and you turn on the headlights, does anything happen?" ~ Steven Wright',
    '"I have the world\'s largest collection of seashells. I keep it on all the beaches of the world... perhaps you\'ve seen it." ~ Steven Wright',
    '"Right now I\'m having amnesia and deja-vue at the same time." ~ Steven Wright',
    '"I invented the cordless extension cord." ~ Steven Wright',
    '"I\'m writing an unauthorized autobiography." ~ Steven Wright',
    '"You know how it feels when you\'re leaning back on a chair, and you lean too far back, and you almost fall over backwards, but then you catch yourself at the last second? I feel like that all the time..." ~ Steven Wright',
    '"I bought some batteries, but they weren\'t included." ~ Steven Wright',
    '"Plan to be spontaneous tomorrow." ~ Steven Wright',
    '"I filled out an application that said, "In Case Of Emergency Notify". I wrote "Doctor"... What\'s my mother going to do?" ~ Steven Wright',
    '"What\'s another word for Thesaurus?" ~ Steven Wright',
    '"When I was a kid, we had a quicksand box in the backyard. I was an only child . . . eventually." ~ Steven Wright',
    '"I put instant coffee in a microwave and almost went back in time." ~ Steven Wright',
    '"I bought a house on a one-way dead-end road. I don\'t know how I got there." ~ Steven Wright',
    '"I just got skylights put in my place. The people who live above me are furious." ~ Steven Wright',
    '"Last year for Christmas, I got a humidifier and a dehumidifier... I thought I\'d put them in the same room and let them fight it out." ~ Steven Wright',
    '"If you were going to shoot a mime, would you use a silencer?" ~ Steven Wright',
    '"I was in the first submarine. Instead of a periscope, they had a kaleidoscope. "We\'re surrounded."" ~ Steven Wright',
    '"If toast always lands butter-side down, and cats always land on their feet, what happen if you strap toast on the back of a cat and drop it?" ~ Steven Wright',
    ]

def main():
	
	stationDict = {'Lahina': 'TPT2799', 'Kahului': '1615680', 'Makena': '1615202', 'Kihei':'TPT2797'};
	
	for key, value in stationDict.items():
	
		stationName = key
		stationID = value
		
		xmlFile = '/home/yosemit1/minustide_scripts/' + stationName + '.xml'
	
		# --- run main check
		tideCheck(xmlFile,stationName)


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
			tideHeight = subelement.find("predictions_in_ft").text
			tideDate = subelement.find("date").text # ex. 2012/01/20
			tideDay = subelement.find("day").text
			
			tideDateArray = string.split(tideDate,"/")
			
			year = str(tideDateArray[0])
			day = str(tideDateArray[2])
			month = str(tideDateArray[1])

			
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
					
					emailFolks = {'Jorma':'aloha@jorma.com','Jeff Fahey':'faheyjeffrey@gmail.com','Jim Dudla':'jdudla@iuetech.com','Joe Breman':'jbreman@iuetech.com','Meghan Gould':'mauka@meghangould.com','Bryan Berkowitz':'bryan.berkowitz@gmail.com','Mitch Sanders':'kukuyampira@hotmail.com'};
					#emailFolks = {'jorma': 'aloha@jorma.com','jorma rodieck': 'jorma@iuetech.com','Gmail Jorma': 'jormadotcom@gmail.com'};
					#emailFolks = {'Jorma': 'aloha@jorma.com'};

					# loop through each subscriber
					for key, value in emailFolks.items():
						
						print "********Send Email*********"
						msg = MIMEText('Aloha -\n\n'  + 'There will be a ' + tideHeight + 'ft minus tide on ' + human_tideDate + " at " + tideTime + " in " + station +  "\n\n -Jorma" + "\n\n----\n\n" + random.choice(quotes)) 
						msg['To'] = email.utils.formataddr((key, value))
						msg['From'] = email.utils.formataddr(('Jorma', 'jorma@minustide.net'))
						msg['Subject'] = 'Minus Tide Alert for tomorrow in ' + station + ": " + tideHeight

						conn = smtplib.SMTP('mail.minustide.net')
						conn.login('jorma@minustide.net', 'l0wtid3')
						conn.sendmail(msg['From'], msg['To'], msg.as_string())
						conn.quit()
					return

	print " "
	return

if __name__ == '__main__':
	main()

