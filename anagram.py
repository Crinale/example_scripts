#!/bin/python

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
	r = sorted(a)
	s = sorted(b)
	count = len(r)
	count2 = len(s)

	for i in r:
		if i in s:
			count -= 1

	for l in s:
		if l in r:
			print l
			count2 -= 1
	
	print count + count2



#makeAnagram("iceman","cinema")
#makeAnagram("bellhop","popman")
#makeAnagram("abc","cba")
#makeAnagram("listen","silent")
#makeAnagram("fcrxzwscanmligyxyvym","jxwtrhvujlmrpdoqbisbwhmgpmeoke")
makeAnagram("mmax","max")