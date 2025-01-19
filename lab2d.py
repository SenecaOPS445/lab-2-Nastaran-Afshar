#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print('Usage: ' + sys.argv[0] + ' name age')
    sys.exit()

name = str(sys.argv[1])
age = int(sys.argv[2])

print('Hi ' + str(sys.argv[1]) + ', you are ' + str(sys.argv[2]) + ' years old.')