import sys

file = open("fall2019.txt", "r")


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


	

