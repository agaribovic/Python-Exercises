import re
#your code goes here

a = input()

start=r"^[189]"

if re.match(start,a) and len(a) ==8:
	print("Valid")
else:
	print("Invalid")
