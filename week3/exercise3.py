"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""
from __future__ import division
from __future__ import print_function
import random


def not_number_rejector():
    message = "enter a number: "
    while True:
        try:
            y = int(raw_input(message))
            return y
        except:
            print("A 'NUMBER', dummy :")


def greater_than_rejector(low):
    while True:
        x = not_number_rejector()
        if low < x:
            return x
        else:
            print ("Upper means bigger, you mook:")


def super_asker(low, high):
    ask = "Enter a number between %s and %s: " % (low, high)
    while True:
            try:
                z = int(raw_input(ask))
                if low <= z and z <= high:
                    print("Hooray for you!")
                    return z
                else:
                    print ("Between %s and %s, dummy:" % (low, high))
            except:
                print("Not a number, dingis")

    return int(z)


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nwelcome to the ADVANCED guessing game!")
    print("\nLet's set a lower bound\n")
    lowerBound = not_number_rejector()
    print("\nOK, now let's set a upper bound\n")
    upperBound = greater_than_rejector(lowerBound)
    print("BEGIN FUN GAME!")
    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = int(super_asker(lowerBound, upperBound))
        print("you guessed {},".format(guessedNumber),)
        if guessedNumber == actualNumber:
            print("you got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("too small, try again ")
        else:
            print("too big, try again   ")
    return "You got it!"


if __name__ == "__main__":
    advancedGuessingGame()
