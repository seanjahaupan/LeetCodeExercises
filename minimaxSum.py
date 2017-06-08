#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))

min = float('Inf')
max = 0
runningSum = 0
for num in arr:
    if num < min:
        min = num
    if num > max:
        max = num
    runningSum += num
    
    
print(runningSum - max, runningSum - min)
