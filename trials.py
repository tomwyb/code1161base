from __future__ import print_function
from __future__ import division
import maths


def calculate_hypotenuse(base, height):
    hypotenuse = math.sqrt(base**2 + height**2)
    return(hypotenuse)


def calculate_area(base, height):
    area = (base * height)/2
    return(area)


def calculate_perimeter(base, height):
    perimeter = calculate_hypotenuse(base, height) + base + height
    return(perimeter)


def calculate_aspect(base, height):
    if base == height:
        print("equal")
    elif base < height:
        print("tall")
    elif base > height:
        print("wide")


def get_triangle_facts(base, height, units="mm"):
    return {"area": calculate_area(base, height),
            "perimeter": calculate_perimeter(base, height),
            "height": height,
            "base": base,
            "hypotenuse": calculate_hypotenuse(base, height),
            "aspect": calculate_aspect(base, height),
            "units": units}


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm
# It has a perimeter of 40.0mm
# This is a tall triangle.
def tell_me_about_this_right_triangle(facts_dictionary):
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
                       ∕ |
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

    pattern = ("This triangle is {area}{units}\n"
               "It has a perimeter of {perimeter}{units}\n"
               "This is a {aspect} triangle.\n")

    facts = pattern.format(facts_dictionary)

    if get_triangle_facts["aspect"] == "tall":
        return(tall_)
    elif get_triangle_facts["aspect"] == "wide":
        return(wide_)
    elif get_triangle_facts["aspect"] == "equal":
        return(equal_)

    return("/n" + facts)


def triangle_master(base,
                    height,
                    return_diagram=False,
                    return_dictionary=False):
    if return_diagram and return_dictionary:
        return None
    elif return_diagram:
        return None
    elif return_dictionary:
        return None
    else:
        print("You're an odd one, you don't want anything!")


print(get_triangle_facts(3, 4, units="mm"))
print("tall" + calculate_aspect(3, 4))
print("wide" + calculate_aspect(10, 4))
print("equal =" + calculate_aspect(4, 4))
