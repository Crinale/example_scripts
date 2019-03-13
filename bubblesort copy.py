n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# Write Your Code Here
count = 0
arraysort = False
while(not arraysort):
    arraysort = True
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            count += 1
            arraysort = False

print count
print a[0]
print a[-1]

print "Array is sorted in {} swaps.".format(count)
print "First Element: {}".format(a[0])
print "Last Element: {}".format(a[-1])