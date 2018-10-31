def print_formatted(number):
    # your code goes here
    r = len(bin(number)[2:])
    for i in range(number):
        print ('%s %s %s %s'%(str(i+1).rjust(r,' '),oct(i+1)[1:].rjust(r,' '),hex(i+1)[2:].upper().rjust(r,' '),bin(i+1)[2:].rjust(r,' ')))



if __name__ == '__main__':
 	n = int(raw_input())
 	print_formatted(n)