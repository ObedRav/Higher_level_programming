#!/usr/bin/python3
import sys

argv = sys.argv

if (len(argv) == 1):
    print("{0} arguments.".format((len(argv))-1))
elif (len(argv) == 2):
    print("{0} argument:".format((len(argv))-1))
else:
    print("{0} arguments:".format((len(argv)-1)))

for i, arguments in enumerate(argv):
    if (i == 0):
        continue
    print("{0}: {1}".format(i, arguments))
