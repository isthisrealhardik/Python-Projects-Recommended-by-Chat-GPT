# Basic Number Guessing Game
# Where the user will input a number
# and our computer will tell if it's less than or more than the random chosen by the computer
# it will do that untill the user has came to the answer

from random import randint

range = int(input("select a range to choose a random number from: "))
value = randint(0, range)
userInput = int(input("Enter your random guess: "))

while (userInput != value): 
    if (userInput > value):
        print("way too bigger, go for a lower number")
        userInput = int(input("Enter a lower number: "))
    elif (userInput < value):
        print("way too lower, go for something bigger")
        userInput = int(input("Enter a bigger number: "))

print(f"you guessed the number correctly, your number: {userInput}, and computer's number: {value}")