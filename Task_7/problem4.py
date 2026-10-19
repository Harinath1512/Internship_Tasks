# Funny String

# https://www.hackerrank.com/challenges/funny-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    rev=s[::-1]
    for i in range(len(s)):
        diff1 = abs(ord(s[i]) - ord(s[i - 1]))
        diff2 = abs(ord(rev[i]) - ord(rev[i - 1]))

        if diff1 != diff2:
            return "Not Funny"

    return "Funny"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
