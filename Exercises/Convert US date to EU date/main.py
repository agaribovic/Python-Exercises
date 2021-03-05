inputDate = input()
 
dates = {
    "January": "1",
    "February": "2",
    "March": "3",
    "April": "4",
    "May": "5",
    "June": "6",
    "July": "7",
    "August": "8",
    "September": "9",
    "October": "10",
    "November": "11",
    "December": "12"
}
 
if ',' in inputDate:
    splitDate = inputDate.split(' ')
    if splitDate[0] in dates:
        month = str(list(dates).index(splitDate[0])+1)
        day = splitDate[1].replace(",","")
        EUdate = day + "/" + month + "/" + splitDate[2]
       
elif '/' in inputDate:
    splitDate = inputDate.split('/')
    EUdate = splitDate[1] + "/" + splitDate[0] + "/" + splitDate[2]
 
print(EUdate)
