import time
import sys
import win32api
	
def Retry():
	Continue = raw_input("\nagain (Y/N)? \n >")
	if Continue == "Y":
		main()
	elif Continue == "N":
		print Continue
		sys.exit(0)
	else:
		print "\nERROR: invalid input"
		sys.exit(0)
	
def main():
	
	setdate = 0
	now = ""
	x = str(raw_input("What message do you want to appear? \n > "))
	hours = int(raw_input("\nwhat time do you want your message to appear (hours)? \n > "))
	minutes = int(raw_input("\nwhat time do you want your message to appear (minuets)? \n > "))
	morningNight = raw_input("\nAM or PM? \n > ")
	

	
	if morningNight == "AM" or "am" or "Am" or "aM":
		setdate = str(hours) + ":" + str(minutes)
	elif morningNight == "PM" or "pm" or "Pm" or "pM":
		hours += 12
		setdate = str(hours) + ":" + str(minutes)
	else:
		print "ERROR: Incorrect TimeStamp input..."
	
	Message = x + " " + setdate

	while True:
		now = time.strftime("%H:%M")
		if setdate == now:
			win32api.MessageBox(0, Message , "Alert")
			Retry()
		else: 
			continue
		time.sleep(1)
	
		
	
	
main()