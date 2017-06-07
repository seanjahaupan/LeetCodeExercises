#!/bin/python3

import sys


time = input().strip()
if time[-2] == 'P':
    hour = 12
else:
    hour = 0
editedtime = time[:-2]
newTime = editedtime.split(':')

if newTime[0] != '12':
    newTime[0] = str(int(newTime[0]) + hour)
elif time[-2] == 'A':
    newTime[0] = '00'
    
if len(newTime[0]) == 1:
    newTime[0] = '0'+newTime[0]

    
print(':'.join(newTime))
