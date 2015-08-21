import time

def gettoday():
	timeArray = time.localtime(int(time.time()))
	today = time.strftime("%Y-%m-%d", timeArray)
	return today