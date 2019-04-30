import sys

class classInfo:
    def __init__(self, day, start, end, room):
        self.day = day
        self.start = start
        self.end = end
        self.room = room


def createList():


	file = open("fall2019.txt", "r")

	LIV = []
	CAC = []
	BUS = []
	CookDug = []


	for line in file:

		word = line.split()

		day = word[0]

		startTime = word[1].split(":")
		startHour = int(startTime[0])
		startMinutes = int(startTime[1])

		if word[2] == "AM":
			startPair = [startHour, startMinutes]
		else:
			startHour = startHour + 12
			startPair = [startHour, startMinutes]


		endTime = word[4].split(":")
		endHour = int(endTime[0])
		endMinutes = int(endTime[1])


		if word[5] == "AM":
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
			CookDug.append(classInfo(day, startPair, endPair, room))

	finalList = [LIV,CAC,BUS,CookDug]

	return finalList




		

