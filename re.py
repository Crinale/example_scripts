fullString = raw_input()
match = raw_input() 
import re
pattern = re.compile(match)
r = pattern.search(fullString)
if not r: 
    print "(-1, -1)"
while r:
    print "({0}, {1})".format(r.start(), r.end() - 1)
    r = pattern.search(fullString,r.start() + 1)