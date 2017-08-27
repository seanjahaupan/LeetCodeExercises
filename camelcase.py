#CamelCase.py
#!/bin/python3
import sys

s = input().strip()
words = 1
for char in s:
    if char.isupper():
        words += 1
        
print(words)


