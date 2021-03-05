numOfcolors = int(input())
colorPrice = 5.00
cost = 40.00
tax = 0.1

total = numOfcolors * colorPrice + cost 

totalWithTax= total + (tax * total)

print(round(totalWithTax))
