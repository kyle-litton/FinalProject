import sys

lines = sys.stdin.readlines()

i = 0	

line = lines[i].split(' ')
print(line)

while line:

	curr = (line[0]).rstrip("\n")
   
	

	i = i + 1
	

	try:
		
		line = lines[i].split(' ')

	except:

		break
