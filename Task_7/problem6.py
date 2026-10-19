# Pangrams

# https://www.hackerrank.com/challenges/pangrams/problem

a='jhaeg'

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    d={}
    s=s.replace(' ','')
    for i in s.lower():
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    s=''
    for i in d.keys():
        s+=i
    if sorted(s)==sorted('abcdefghijklmnopqrstuvwxyz'):
        return 'pangram'
    else:
        return 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
