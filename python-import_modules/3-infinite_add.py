#!/usr/bin/python3
import sys

__name__ = "__main__"

argv = sys.argv

result = 0

for i, numbers in enumerate(argv):
    if (i == 0):
        continue
    result += int(numbers)

print(result)
