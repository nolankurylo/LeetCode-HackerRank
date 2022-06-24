#!/bin/python
from bisect import bisect_left

def compute_median(X):
    X.sort()
    n = len(X)
    
    if n == 0:
        # print(n, X)
        return "Wrong!"
    elif n % 2 != 0:
        m = X[n//2]
    else:
        m = (X[(n-1)//2]+X[(n+1)//2]) / 2
    return ('%f' % m).rstrip('0').rstrip('.')

def median(a,x):
    median_list = []
    for i in range(len(a)):
        operation = a[i]
        value = x[i]
        
        idx = bisect_left(median_list, value, 0, len(median_list))
        if operation == 'r':
            if idx >= len(median_list) or median_list[idx] != value:
                
                print("Wrong!")
            else:
                median_list.pop(idx)
                print(compute_median(median_list))
        if operation == 'a':
            median_list.insert(idx, value)
            print(compute_median(median_list))
           

N = int(input())
s = []
x = []
for i in range(0, N):
   tmp = input().strip().split(' ')
   a, b = [xx for xx in tmp]
   s.append(a)
   x.append(int(b))
median(s,x)
