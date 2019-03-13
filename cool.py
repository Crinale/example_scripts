#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    for i in grades:
        grademultiple = 5 - i % 5
        grademultiplehigh = i + grademultiple
        gradecurve = grademultiplehigh - i
        if i >= 38 and gradecurve < 3 :
            return grademultiplehigh
        else:
            return i
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    grades = []

    for _ in xrange(n):
        grades_item = int(raw_input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()