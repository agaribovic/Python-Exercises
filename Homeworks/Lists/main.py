myUniqueList = []
myLeftovers = []

def addToList(value):
    if value not in myUniqueList:
        myUniqueList.append(value)
        return True
    else:
        return False
        
def pushRejectedInputs(value):
    if value in myUniqueList:
        myLeftovers.append(value)
            
    