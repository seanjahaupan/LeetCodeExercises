#!/bin/python3
#testing
import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    shouldCharge = 0
    for i in range(n):
        if i != k:
            shouldCharge += ar[i]
            
    shouldCharge /= 2
    if shouldCharge - b == 0:
        return 'Bon Appetit'
    else:
        return int(b - shouldCharge)

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
