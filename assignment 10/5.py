import numpy as np

def stringcentred(a):
    for x in a:
        if len(x)>15:
            print(x[:15])
        else :
            m = (15 - len(x)) // 2  
            print("_ " * m + x + " _" * (15 - m - len(x)))

def leftjustified(a):
    for x in a:
        if len(x)>15:
            print(x[:15])
        else :
           print(x + " _" * (15 - len(x)))

def rightjustified(a):
    for x in a:
        if len(x)>15:
            print(x[:15])
        else :
            print("_ " * (15-len(x)) + x)
        

arr = np.array(['tejeswarraoalias', 'allu arjun', 'mahesh', 'kalyan'])
print("string centred")
print()
stringcentred(arr)
print()
print("left justified")
print()
leftjustified(arr)
print()
print("right justified")
print()
rightjustified(arr)
