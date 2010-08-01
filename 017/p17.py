# Solution to Project Euler Problem 17 in python
# http://en.wikipedia.org/wiki/List_of_numbers


hn = {}
hn[1] = "one hundred" 
hn[2] = "two hundred"
hn[3] = "three hundred"
hn[4] = "four hundred"
hn[5] = "five hundred"
hn[6] = "six hundred"
hn[7] = "seven hundred"
hn[8] = "eight hundred"
hn[9] = "nine hundred"

tn = {} 
tn[2] =  "twenty" 
tn[3] =  "thirty" 
tn[4] =  "forty" 
tn[5] =  "fifty" 
tn[6] =  "sixty" 
tn[7] =  "seventy" 
tn[8] =  "eigthy" 
tn[9] =  "ninety" 

sn = {}  
sn[0] =  ""
sn[1] =  "one" 
sn[2] =  "two" 
sn[3] =  "three" 
sn[4] =  "four" 
sn[5] =  "five" 
sn[6] =  "six" 
sn[7] =  "seven" 
sn[8] =  "eight" 
sn[9] =  "nine" 
sn[10] = "ten"
sn[11] = "eleven"
sn[12] = "twelve"
sn[13] = "thirteen"
sn[14] = "fourteen"
sn[15] = "fifteen"
sn[16] = "sixteen"
sn[17] = "seventeen"
sn[18] = "eighteen"
sn[19] = "nineteen"




sum=0
for n in range(1,1000):
	name = ""
	
	hundreds = n / 100
	tens = n / 10 % 10
	singles = n%10
		

	if (hundreds):
		name +=hn[hundreds]
		if (tens or singles):
			name +=" and "
		
		
	if ( ( (10 *tens) + singles ) < 20 ):
		name += sn[( (10*tens)+singles)]
	else:	
		if (tens):
			name +=tn[tens]
			if (singles):
				name+="-"
		if (singles):
			name+= sn[singles]

	#print n, hundreds, tens, singles, name
	
	name = name.replace("-","")
	name = name.replace(" ","")
	sum+= len(name)

sum +=len("onethousand") #being lazy
print sum