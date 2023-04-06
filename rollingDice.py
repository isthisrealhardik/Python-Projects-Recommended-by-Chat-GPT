# rolling dice game
# that simulates a random number from 1 to 6

from random import randint

def rollingDice():
    value = randint(1, 6)
    return value

print(rollingDice())
