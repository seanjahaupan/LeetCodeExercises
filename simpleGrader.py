#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    newGrades = []
    
    for grade in grades:
        if grade <= 35:
            newGrades.append(grade)
        elif grade % 5 > 2:
            newGrades.append(grade + (5 - grade %5))
        else:
            newGrades.append(grade)
            
    return newGrades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
