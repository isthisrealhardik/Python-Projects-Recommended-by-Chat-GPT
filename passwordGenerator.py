# password generator
# it returns lower, upper and a number to generator a number of specified length by the user

from random import randint

def lowerLetter():
    return chr(randint(ord('a'), ord('z')))

def upperLetter():
    return chr(randint(ord("A"), ord("Z")))

def numRandom():
    return str(randint(0, 9))

length = int(input("Length of the password you'd like?: "))

charList = [lowerLetter(), upperLetter(), numRandom()]
print(charList)

def passwordGen():
    randomPass = []
    for i in range(0, length):
        ranChr = charList[randint(0, len(charList) - 1)]
        randomPass.append(ranChr)
    joined = ''.join(randomPass)
    return joined

print(passwordGen())
