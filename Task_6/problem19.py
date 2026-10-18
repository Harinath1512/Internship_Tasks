# Company Logo

# https://www.hackerrank.com/challenges/company-logo/problem

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    result = sorted(d.items(), key=lambda x: (-x[1], x[0]))

    for char, count in result[:3]:
        print(char, count)