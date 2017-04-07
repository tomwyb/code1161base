# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""
from __future__ import division
from __future__ import print_function
import math
# import time


def binary_search(low, high, actual_number):

    guessed = False
    tries = 0

    while not guessed:
        guess = int(math.floor((high - low) / 2 + low))
        tries += 1
        print("Attempt %s : " % (tries))
        print(guess)
        if guess < actual_number:
            print(str(guess) + " is too low")
            low = guess
        elif guess < actual_number:
            print(str(guess) + " is too high")
            high = guess
        else:
            print("%s was the right answer. It took %s attempts"
                  % (guess, tries))
            guessed = True

    return{"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
