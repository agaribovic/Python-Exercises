input = input()
space = " "
result = ""

for i in reversed(input):
    if i.isalpha() or i == space: 
       result += i
      
print(result)
