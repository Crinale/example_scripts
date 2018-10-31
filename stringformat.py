def print_formatted(number):
    # your code goes here
    for i in range(number):
        print ("%s %s %s %s"%(i+1,oct(i+1)[1:],hex(i+1)[2:].upper(),bin(i+1)[2:]))



if __name__ == '__main__':
 	n = int(raw_input())
 	print_formatted(n)