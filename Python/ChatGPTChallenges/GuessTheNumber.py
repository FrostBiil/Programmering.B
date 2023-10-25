"""
Write a Python program that generates a random number between 1 and 20 (inclusive) 
and asks the user to guess what the number is. The program should provide feedback 
to the user, indicating whether their guess is too high or too low, and continue to 
ask for guesses until the user correctly guesses the number. Once they guess the 
correct number, the program should print a message congratulating the user and 
indicate how many attempts it took to guess the number.
"""

from random import randint

randomNum = randint(0, 20)
guessCorrect = False

def checkGuess():
    global guessCorrect
    if userInput == randomNum:
        guessCorrect = True
        return print("Congrats on getting the answer correct!")
    
    if userInput < randomNum:
        return print("have another guess, the number is higher")

    return print("have another guess, the number is lower")


while not guessCorrect:
    userInput = int(input("Guess a number between 1 and 20: "))
    checkGuess()

input("press any key to exit")