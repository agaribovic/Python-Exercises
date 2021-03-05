n = int(input())
sum = 0
array = [n]

for i in range(1, n+1):
    ele = int(input())
    if ele % 2 == 0: 
       sum += ele
       array.append(ele)
       
print(sum)
