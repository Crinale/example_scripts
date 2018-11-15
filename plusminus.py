#!/bin/python

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    length = float(len(arr))
    pos = 0
    zer = 0
    neg = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i == 0:
            zer += 1
        elif i < 0:
            neg += 1
    print(pos/length)
    print(neg/length)
    print(zer/length)

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)