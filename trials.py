# from __future__ import print_function
# from __future__ import division
# import maths
import random


def random_num(lower, upperBound):
    """Return a random number."""
    random_ = random.randint(lower, upperBound)
    print(random_)


print(random_num(2, 10))
