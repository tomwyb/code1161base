from __future__ import print_function
from __future__ import division


def countdown(message, start, stop, completion_message):
    cntdwn_list = []
    if start > stop:
        step = -1
    elif start == stop:
        return(completion_message)
    else:
        step = 1
    for i in range(start, stop, step):
        cntdwn_list.append(message + " {}".format(i))
    return(cntdwn_list)

# def countdown02(message, start, stop, completion_message):
#     num_down = len(start - stop) + 1
#     print(message + num_down)


print(countdown("Getting ready to start in ", 9, 1, "Let's go! 01"))
print(countdown("Getting ready to start in ", 0, 15, "Let's go! 02"))
# print(countdown02("Getting ready to start in ", 9, 1, "Let's go! 01"))
# print(countdown02("Getting ready to start in ", 0, 15, "Let's go! 02"))
