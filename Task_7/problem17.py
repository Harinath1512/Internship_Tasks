# Separate the Numbers

# https://www.hackerrank.com/challenges/separate-the-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    for i in range(1, len(s) // 2 + 1):
        first = int(s[:i])
        num = first
        result = ""

        while len(result) < len(s):
            result += str(num)
            num += 1

        if result == s:
            print("YES", first)
            return

    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
