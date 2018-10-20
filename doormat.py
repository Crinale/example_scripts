x = int(raw_input())
y = int(raw_input())

maxchar = x * y
LRofWel = ((y-7)/2)*"-"

#print(".|.".center(y,'-'))
#print("Welcome".center(y,'-'))
#print(".|.".center(y,'-'))


for i in reversed(range(3,x+5,3)):
	print(i*"-")

print ('%sWelcome%s'%(LRofWel,LRofWel))

for i in range(3,x+5,3):
	print(i*"-")


for i in range(x/2):
	print((".|."*(2*i+1)).center(y,'-'))

print("Welcome".center(y,'-'))

for i in reversed(range(x/2)):
	print((".|."*(2*i+1)).center(y,'-'))