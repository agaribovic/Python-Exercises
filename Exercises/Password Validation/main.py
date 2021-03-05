password = input()

length = len(password)
   
symbols = ['!', '@', '#', '$', '%', '&', '*']

symbolCounter = 0

for i in symbols: 
    if password.count(i): 
        symbolCounter += password.count(i)
        
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

numCounter = 0

for j in numbers: 
    if password.count(j): 
        numCounter += password.count(j)

if(length > 6 and symbolCounter > 1 and numCounter > 1): 
    print("Strong")
else: 
    print("Weak")
