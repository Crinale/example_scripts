#!/bin/python

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
	flag = 0
	for i in set(s1):
		if i in set(s2):
			flag = 1
			print 'YES'
	if flag == 0:
		print 'NO'


twoStrings("Hello","Hi")
twoStrings("world","hello")
twoStrings("woudlyoulikefries","abcabcabcabcabcabc")
twoStrings("cdecdecdecdecdecdecde","jackandjill")
twoStrings("wentupthehill","writetoyourparents")
twoStrings("hi","hello")
twoStrings("hi","hello")

