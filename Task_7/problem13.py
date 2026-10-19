# Sherlock and the Valid String

# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isValid(s):
    d = {}

    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    freq = list(d.values())
    count = {}

    for i in freq:
        count[i] = count.get(i, 0) + 1

    if len(count) == 1:
        return "YES"

    if len(count) == 2:
        a, b = count.keys()

        if (count[a] == 1 and (a - 1 == b or a == 1)):
            return "YES"

        if count[b] == 1 and (b - 1 == a or b == 1):
            return "YES"

    return "NO"

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
