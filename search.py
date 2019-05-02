import sys

class classInfo:
    def __init__(self, day, start, end, room):
        self.day = day
        self.start = start
        self.end = end
        self.room = room


def compStart(startPair, targetHour, targetMinutes):
	
	if((startPair[0]>=targetHour) and int(startPair[1])>targetMinutes):
		
		return 0
		

	elif ((startPair[0]>targetHour) and int(startPair[1])>=targetMinutes):
		
		return 0
	
	else:
		return 1

def compEnd(endPair, targetHour, targetMinutes):


	if((endPair[0]<=targetHour) and int(endPair[1]) < targetMinutes):
		
		return 0

	elif((endPair[0]<targetHour) and int(endPair[1]) <= targetMinutes):
		
		return 0

	else:
		
		return 1


def vacant(startPair, endPair, targetHour, targerMinutes):
	#compEnd 
	#compstart 



def createList():


	file = open("fall2019.txt", "r")

	LIV = []
	CAC = []
	BUS = []
	CookDoug = []


	for line in file:

		word = line.split()

		day = word[0]

		startTime = word[1].split(":")
		startHour = int(startTime[0])
		startMinutes = startTime[1]

		if (word[2] == "AM" or startHour == 12):

			startPair = [startHour, startMinutes]
		else:
			startHour = startHour + 12
			startPair = [startHour, startMinutes]

	
		endTime = word[4].split(":")
		endHour = int(endTime[0])
		endMinutes = endTime[1]


		if (word[5] == "AM" or endHour == 12):
			endPair = [endHour, endMinutes]
		else:
			endHour = endHour + 12
			endPair = [endHour, endMinutes]

		
		campus = word[6]


		try:
			room = word[7]
		except:
			continue 

		if campus == "LIV":
			LIV.append(classInfo(day, startPair, endPair, room))
		elif campus == "CAC":
			CAC.append(classInfo(day, startPair, endPair, room))
		elif campus == "BUS":
			BUS.append(classInfo(day, startPair, endPair, room))
		elif campus == "D/C":
			CookDoug.append(classInfo(day, startPair, endPair, room))

	finalList = [LIV,CAC,BUS,CookDoug]

	return finalList


def checkTime(campus, day, hour, minutes):

	lst = createList()

	if campus == "College Ave":
		targetCampus = lst[1]
	elif campus == "Livingston":
		targetCampus = lst[0]
	elif campus == "Busch":
		targetCampus = lst[2]
	elif campus == "Cook/Douglass":
		targetCampus = lst[3]

	openRooms = []

	for x in targetCampus:

		if x.room not in openRooms:
			openRooms.append(x.room)


	for x in targetCampus:
		
		if (x.day == day and ( ((compStart(x.start, hour, minutes)==1) and (compEnd(x.end,hour,minutes)==1) ) )):
			if x.room in openRooms:
				openRooms.remove(x.room)			

		
	return openRooms















