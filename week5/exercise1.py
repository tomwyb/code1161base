# -*- coding: UTF-8 -*-
"""Refactoring.

This excercise is very similar to week 2, exercise 2. It contains a complete
and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

The resulting file should feel as close to english as possible.
It must also pass the linter.

This is the first file that will be run against the pydocstyle checker. If
you've run the week5_system_prep.sh file you should be getting blue linter dots
that show you where lintere errors are. If they aren't working, you should be
getting the errors in the test output.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""

from __future__ import division
from __future__ import print_function
import math


def countdown(message, start, stop, completion_message):
    """Return a countdown message."""
    cntdwn_list = []
    if start > stop:
        step = -1
    elif start == stop:
        return(completion_message)
    else:
        step = 1
    for i in range(start, stop, step):
        cntdwn_list.append(message + " {}".format(i))
    cntdwn_list.append(completion_message)
    return(cntdwn_list)


def calculate_hypotenuse(base, height):
    """Return the triangle's hypotenuse."""
    hypotenuse = math.sqrt(base**2 + height**2)
    return(hypotenuse)


def calculate_area(base, height):
    """Return the triangle's area."""
    area = (base * height)/2
    return(area)


def calculate_perimeter(base, height):
    """Return the triangle's perimeter."""
    perimeter = calculate_hypotenuse(base, height) + base + height
    return(perimeter)


def calculate_aspect(base, height):
    """Return the triangle's aspect."""
    if base == height:
        return("equal")
    elif base < height:
        return("tall")
    elif base > height:
        return("wide")


def get_triangle_facts(base, height, units="mm"):
    """Return a dictionary used for facts."""
    return{"area": calculate_area(base, height),
           "perimeter": calculate_perimeter(base, height),
           "height": height,
           "base": base,
           "hypotenuse": calculate_hypotenuse(base, height),
           "aspect": calculate_aspect(base, height),
           "units": units}


def tell_me_about_this_right_triangle(facts_dictionary):
    """Return a diagram and dictionary."""
    tall_ = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide_ = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal_ = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = ("This triangle is {area}{units}²\n"
               "It has a perimeter of {perimeter}{units}\n"
               "This is a {aspect} triangle.\n")

    facts = pattern.format(**facts_dictionary)

    if facts_dictionary["aspect"] == "tall":
        return(tall_.format(**facts_dictionary) + "\n" + facts)
    elif facts_dictionary["aspect"] == "wide":
        return(wide_.format(**facts_dictionary) + "\n" + facts)
    elif facts_dictionary["aspect"] == "equal":
        return(equal_.format(**facts_dictionary) + "\n" + facts)


def triangle_master(base,
                    height,
                    return_diagram=False,
                    return_dictionary=False):
    """Return a dict, diagram, or dict and diagram."""
    dictionary = get_triangle_facts(base, height, units="mm")
    diagram = tell_me_about_this_right_triangle(dictionary)
    if return_diagram and return_dictionary:
        return {"diagram": diagram, "facts": dictionary}
    elif return_diagram:
        return diagram
    elif return_dictionary:
        return {"facts": dictionary}
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    """Make a pyramid out of words."""
    list_of_lengths = []
    for i in range(3, 21, 2):
        list_of_lengths.append(i)
    for i in range(20, 3, -2):
        list_of_lengths.append(i)
    return(list_of_words_with_lengths(list_of_lengths))


def get_a_word_of_length_n(length):
    """Entering a length and fetcihng according to the length."""
    import requests
    baseURL = "http://www.setgetgo.com/randomword/get.php?len="
    if length == 0:
        return(None)
    elif type(length) != int:
        return(None)
    else:
        url = baseURL + str(length)
    r = requests.get(url)
    message = r.text
    return(message)


def list_of_words_with_lengths(list_of_lengths):
    """Return words that matches the list of lengths."""
    num_list = []
    for i in range(len(list_of_lengths)):
        num_list.append(get_a_word_of_length_n(list_of_lengths[i]))
    return num_list


if __name__ == "__main__":
    pass
