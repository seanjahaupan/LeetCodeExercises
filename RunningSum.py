#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

runningSum = 0

for num in arr:
    runningSum += num
    
print(runningSum)
