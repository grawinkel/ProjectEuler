#Project Euler Problem 22 solution in python

def getScore(s):
	score = 0
	
	#s starts and ends with ", slice it away
	s=s[1:-1]
	for c in s:
		score += (ord(c)-64) #A==Ascii 65
	return score
	
if __name__ == "__main__":
	f = open("names.txt","r")
	names=sorted( f.readline().split(",") )
	
	result = 0
	for x in range(len(names)):
		result += (x+1) * getScore(names[x])
	print result