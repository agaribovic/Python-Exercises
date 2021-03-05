word = input()
isDuplicate = False 
      
for i in word: 
   if word.count(i) > 1: 
     isDuplicate = True 
     
if isDuplicate: 
   print("Deja Vu")
else: 
   print("Unique")
