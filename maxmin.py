#!/bin/python

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mini = scores[0]
    maxi = scores[0]
    maxcount = 0
    mincount = 0
    for i in scores:
        if i < mini:
            mini = i
            mincount += 1
        elif i > maxi:
            maxi = i
            maxcount += 1
    print ("%s %s" %(maxcount, mincount))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    scores = map(int, raw_input().rstrip().split())

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
