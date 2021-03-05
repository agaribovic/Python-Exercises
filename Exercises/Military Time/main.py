inputTime = input()
 
if 'PM' in inputTime:
    splitTime = inputTime.split(':')
    if splitTime[0] != "12":
        splitTime[0] = int(splitTime[0]) + 12 
    string = str(splitTime[0]) + ":" + splitTime[1]
    time = string.replace("PM","")
 
 
if 'AM' in inputTime:
    splitTime = inputTime.split(':')
    if splitTime[0] == "12":
       splitTime[0] = "00"
       string = splitTime[0] + ":" + splitTime[1]
    elif int(splitTime[0]) < 10:
       string = splitTime[0].zfill(2) + ":" + splitTime[1]
    else:
       string = splitTime[0] + ":" + splitTime[1]
    time = string.replace("AM","")
 
print(time)

