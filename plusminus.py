#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

positive = 0
negative = 0
zeros = 0
for number in arr:
    if number == 0:
        zeros += 1
    elif number > 0:
        positive += 1
    elif number < 0:
        negative += 1
        
        
print(round(positive / len(arr), 6))
print(round(negative / len(arr), 6))
print(round(zeros / len(arr), 6))


