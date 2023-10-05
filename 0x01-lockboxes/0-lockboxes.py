#!/usr/bin/python3
"""
An n-1 boxes is given where the next box is opened
depending on the number in the previous box, the task
in here is to determine is the key in the parents box
is capable of unlocking the next box, repeat the same
search to determine if all the boxes could be open
"""


def canUnlockAll(boxes):
    """
     determine the True or False if the boxes could be
     open or not and return the expected result
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False