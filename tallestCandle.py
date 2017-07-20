#!/bin/python3
#see if it's the tallest candle
import sys


n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

tallestCandle = 0
numberOfCandles = 0

for candle in height:
    if candle > tallestCandle:
        tallestCandle = candle
        numberOfCandles = 1
    elif candle == tallestCandle:
        numberOfCandles += 1
        
        
print (numberOfCandles)  
