def nestedlist():
	li = []
	for _ in range(int(raw_input())):
	    name = raw_input()
	    score = float(raw_input())
	    s = [name,score]
	    li.append(s)

	for i in range(len(li)):
		print li[i][1]

if __name__ == "__main__":
	nestedlist()