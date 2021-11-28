"""
This program compares elements at the beginning and end of a list
if they are the same it removes them
repeat until its no longer possible then it prints out the adjusted list
"""

from typing import List
import sys

def input_func(args):
    """
    Takes all sys.argv and appends them to a list until "." is found
    """
    elements = []
    for i in range(1, len(args)):
        if args[i] != ".":
            elements.append(args[i])
            continue
        return elements



def calc(arr: List[str]) -> List[str]:
    """
    Takes all elements and compares them
    """
    if len(arr) == 1 or len(arr) == 0:
        return arr
    if arr[0] == arr[-1]:
        arr.pop(0)
        arr.pop(-1)
        return calc(arr)
    return arr




if __name__ == "__main__":
    TEMP = input_func(sys.argv)
    F = calc(TEMP)
    print(*F)
