def isEqual(a, b, c):
    if int(a) == int(b) or int(a) == int(c):
        return True
    elif int(b) == int(a) or int(b) == int(c):
        return True
    elif int(c) == int(a) or int(c) == int(b):
        return True
    else:
        return False
        

