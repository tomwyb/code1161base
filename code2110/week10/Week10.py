"""Returning Frank Ghery's facade."""
# from PIL import Image
import os


CWD = os.getcwd()


def frank(source="frgh", guard=5):
    """Recursively replace letters acording to the rules."""

    def apply_rules(letter):
        """Retrun the substitutions."""
        if letter == "f":
            return "fgh"
        elif letter == "r":
            return "ghr"
        elif letter == "g":
            return "fg"
        elif letter == "h":
            return "rh"
        else:
            return letter

    parts = list(source)
    result = map(apply_rules, parts)
    frank_string = "".join(result)
    print(frank_string)
    guard -= 1
    if guard > 0:
        return frank(frank_string, guard)
    else:
        return frank_string


# def wall_sq():
#     """Return a square version of frank."""
#     frank_list = []
#     for i in range(1):
#         frank_list.append(frank())
#     return frank_list
#
#
# if __name__ == "__main__":
print(frank())
# print(wall_sq())
