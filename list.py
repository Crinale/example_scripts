if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
    	s = raw_input().split()
    	if s[0] == 'insert':
    		list.insert(int(s[1]),int(s[2]))
    	if s[0] == 'print':
    		print list
    	if s[0] == 'remove':
    		list.remove(int(s[1]))
    	if s[0] == 'append':
    		list.append(int(s[1]))
    	if s[0] == 'sort':
    		list.sort()
    	if s[0] == 'pop':
    		list.pop()
    	if s[0] == 'reverse':
    		list.reverse()
    	
