from itertools import cycle

def charLoop(char):
    capitals = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lowercase = list("abcdefghijklmnopqrstuvwxyz")

    if char.isupper(): 
        for idx, val in enumerate(capitals): 
            if val == char: 
                newIdx = idx
                for j in range(13): 
                    if newIdx - 1 < 0: 
                        newIdx = len(capitals) - 1
                    else: 
                        newIdx -=1
                return str(capitals[newIdx])
    else: 
        for idx, val in enumerate(lowercase): 
            if val == char: 
                newIdx = idx
                for j in range(13): 
                    if newIdx - 1 < 0: 
                        newIdx = len(lowercase) - 1
                    else: 
                        newIdx -=1
                return str(lowercase[newIdx])

def rot13(message):
    returnMessage = ''
    for i in message: 
        if i.isalpha():
            returnMessage += charLoop(i)
        else: 
            returnMessage += i
    
    return returnMessage
