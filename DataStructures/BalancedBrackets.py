#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    valids = {']':'[', '}':'{', ')':'('}
    stack = []
    for i in range(len(s)):
        
        if s[i] in valids.values():
            stack.append(s[i])
        elif s[i] in valids.keys():
            try:
                inputElem = stack.pop(-1)
            except IndexError:
                return "NO"
            if inputElem != valids[s[i]]:
                return "NO"
        else: 
            return "NO"
            
    if stack != []:
        return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
