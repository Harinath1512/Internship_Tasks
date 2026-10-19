# Super Reduced String

# https://www.hackerrank.com/challenges/reduced-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    result = []

    for i in s:
        if result and result[-1] == i:
            result.pop()
        else:
            result.append(i)

    if result:
        return ''.join(result)
    else:
        return "Empty String"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
