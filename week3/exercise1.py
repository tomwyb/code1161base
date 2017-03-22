# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""
from __future__ import division
from __future__ import print_function


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """
    loopy_range = []
    while start < stop:
        loopy_range.append(start)
        start = start + step
    print(loopy_range)
    return loopy_range


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    lonely_range = []
    while start < stop:
        lonely_range.append(start)
        start = start + step
    return lonely_range


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    double_step_range = []
    while start < stop:
        double_step_range.append(start)
        start = start + 2
    print(double_step_range)
    return double_step_range


def gene_krupa_range(start, stop, even_step, odd_step):
    """Make a range that has two step sizes.

    make a list that instead of having evenly spaced steps
    has odd steps be one size and even steps be another.
    """
    gk_range = []
    it_num = 1
    while start < stop:
        gk_range.append(start)
        if it_num % 2 != 0:
            print(str(it_num) + "odd")
            start += even_step
        else:
            print(str(it_num) + "even")
            start += odd_step
        it_num += 1
    print (gk_range)
    return gk_range


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """

    while True:
        x = int(raw_input("Enter a number between %s and %s: " % (low, high)))
        if low <= x and x <= high:
            print("Hooray for you!")
            return x
        else:
            print ("Try again, dummy:")

    return x


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    message = "enter a number: "
    while True:
        try:
            y = int(raw_input(message))
            print("Hooray for you")
            return y
        except:
            print("Try again, dummy")

    return y


def super_asker(low, high):
    """Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """

    ask = "Enter a number between %s and %s: " % (low, high)
    while True:
            try:
                z = int(raw_input(ask))
                if low <= z and z <= high:
                    print("Hooray for you!")
                    return z
                else:
                    print ("Try again, dummy:")
            except:
                print("Not a number, dingis")


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    # inside Atom, you need to run them from the terminal. E.g.:
    # ben@um:~/projects/git/code1161base$ python week3/exercise1.py

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\ngene_krupa_range", gene_krupa_range(1, 20, 2, 5))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector()
    print("\nsuper_asker")
    super_asker(33, 42)
