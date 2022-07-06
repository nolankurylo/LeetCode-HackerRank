#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'downToZero' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
maxN = 10**6

dp = list(range(maxN+1))

for i in range(2, maxN +1):
    dp[i] = min(dp[i],dp[i-1]+1) 
    curr = dp[i]
    for j in range(2, i+1):
        multiple = i * j
        if multiple > maxN:
            break
        
        dp[multiple] = min(dp[multiple], curr + 1)
        
    # print(dp[:i])


def downToZero(n):
    if n <= 3: return n
    return dp[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()
