#Sergiy Pliss
#Project 1 Timeboxed Coding
#ST-CIS-3296-001-38591-202403
import random

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
	while 1.0 >= birth >= 2.0 :
		birth = float(input())
	population = population + population*(birth/100)

	print("Input death rate.")	
	death = float(input())
	while .5 >= death >= 1.5:
		death = float(input())
	population = population - population*(death/100)

	print("Input migration rate.")	
	while -3 > death > 4:
		migration = float(input())
	population = population + population*(migration/100)

	print("Year :" + str(2023 +x) + "Population :" + str(population) + "Budget: " + str(population*2347))
	if x == 0:
		budone = population*2347
	if x == years:
		budtwo = population*2347

print("Average difference in budget: " +str((budtwo-budone)/years))
