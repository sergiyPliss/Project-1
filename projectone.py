#Sergiy Pliss
#Project 1 Timeboxed Coding
#ST-CIS-3296-001-38591-202403
import math as m

population = 1000
budone = 0
budtwo = 0
birth = 0
death = 0
migration = 0
years = 0

print("Enter number of years.")
years = int(input())
 
for x in range(years):

	print("Input birth rate.")	
	birth = float(input())
	while  birth > 2.0 or birth < 1:
		birth = float(input())
	population = population + population*(birth/100)

	print("Input death rate.")	
	death = float(input())
	while death > 1.5 or death < .5:
		death = float(input())
	population = population - population*(death/100)

	print("Input migration rate.")	
	while  migration > 4 or migration < -3:
		migration = float(input())
	population = population + population*(migration/100)

	print("Year : " + str(2023 +x+1) + " Population : " + str(m.ceil(population)) + " Budget: " + str(population*2350))
	if x == 0:
		budone = population*2350
	if x == years:
		budtwo = population*2350

print("Average difference in budget: " +str((budone-budtwo)/years))
