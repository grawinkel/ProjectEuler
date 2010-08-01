# Problem 25 
# What is the first term in the Fibonacci sequence to contain 1000 digits?
n=1
n1=1
n2=1
x = 2
    
while 1:
	n=n1+n2
	n2=n1
	n1=n
	x+=1
	if (len(str(n))>=1000):
		print x
		break;