#!/bin/python3

import sys

def getRecord(s):
    # Complete this function
    highest = s[0]
    lowest = s[0]
    highestCount = 0
    lowestCount = 0
    
    for game in s:
        if game > highest:
            highest = game
            highestCount += 1
        elif game < lowest:
            lowest = game
            lowestCount += 1
    return [highestCount,lowestCount]

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))



