# Weighted Uniform Strings

# https://www.hackerrank.com/challenges/weighted-uniform-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    weights = set()
    prev = ''
    count = 0

    for i in s:
        if i == prev:
            count += 1
        else:
            count = 1

        weight = (ord(i) - ord('a') + 1) * count
        weights.add(weight)
        prev = i

    result = []

    for q in queries:
        if q in weights:
            result.append("Yes")
        else:
            result.append("No")

    return result
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
