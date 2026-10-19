# Caesar Cipher

# https://www.hackerrank.com/challenges/caesar-cipher-1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    new = ""
    k = k % 26

    for i in s:
        if i.islower():
            new += chr((ord(i) - ord('a') + k) % 26 + ord('a'))
        elif i.isupper():
            new += chr((ord(i) - ord('A') + k) % 26 + ord('A'))
        else:
            new += i

    return new

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
