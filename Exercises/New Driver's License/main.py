import math
 
myName = input()
 
availableAgents = int(input())

otherNames = input()
 
timeNeeded = 20
 
otherNames += " " + myName
namesSplit = otherNames.split(" ")
 
namesSorted = sorted(namesSplit)
 
if myName in namesSplit:
    place = namesSorted.index(myName)+1
 
result = math.ceil(place/availableAgents) * timeNeeded
 
print(result)
