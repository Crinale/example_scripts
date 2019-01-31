argus = int(raw_input())
for i in range(argus):
	try:
		a, b = map(int,raw_input().split())
        print (a//b)
    except Exception as e:
        print("Error Code:",e)