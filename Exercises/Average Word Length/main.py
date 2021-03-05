import math

punctuations = '''!()-[]{};:':\,<>./?@#$%^&*_~'''

string = input()

newString = ""

numberOfLetters = 0

for i in string: 
    if i not in punctuations: 
       newString += i
       if i != " ": 
          numberOfLetters += 1 

splitString = newString.split()
numberOfWords = len(splitString)

average = math.ceil(numberOfLetters/numberOfWords)

print(average)
