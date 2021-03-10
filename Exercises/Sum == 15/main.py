list = [2, 1, 3, 5, 4, 7, 6, 9, 8, 10]

for index,value in enumerate(list):
    for index2, value2 in enumerate(list):
        if list[index] + list[index2] == 15:
            print(list[index], "+", list[index2], "=", list[index]+list[index2])