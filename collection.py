import collections
howmany = int(raw_input())
shoes = collections.Counter(map(int, raw_input().split()))
cust = int(raw_input())

print shoes

income = 0

for i in range(cust):
	size, price =map(int, raw_input().split())
	if shoes[size]:
		income += price
		shoes[size] -= 1

print income 