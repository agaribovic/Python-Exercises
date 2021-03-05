import os

height, width = os.popen('stty size', 'r').read().split()

def playingBoard(rows, columns):
    for row in range(rows):
        if row % 2 == 0:
            for column in range(1, columns):
                if column % 2 == 1:
                    if column != 5:
                        print(" ", end="")
                    else:
                        print(" ")
                else:
                    print("|", end="")
        else:
            print("-----")
    if rows > int(height) or columns > int(width):
        return False  
    else:
        return True 
            
