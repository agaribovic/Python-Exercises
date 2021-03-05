numberOfHovercrafts = int(input())
 
oneHovercraftBuild = 2000000
oneHovercraftSell = 3000000
oneHovercraftInsurance = 1000000
 
cost = 10 * oneHovercraftBuild + oneHovercraftInsurance
profit = numberOfHovercrafts * oneHovercraftSell
 
if profit > cost:
    print("Profit")
elif profit < cost:
    print("Loss")
elif profit == cost:
    print("Broke Even")
