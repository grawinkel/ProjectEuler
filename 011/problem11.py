# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="meatz"
__date__ ="$01.08.2010 14:10:38$"


m = []
max = 0
maxa,maxb = 0,0

def nw(a,b):
    global max,maxa,maxb
    prod = int(m[a][b]) * int(m[a-1][b-1]) * int(m[a-2][b-2]) * int(m[a-3][b-3])
    if (prod > max):
        max = prod
        maxa = a
        maxb = b

def n(a,b):
    global max,maxa,maxb
    prod = int(m[a][b]) * int(m[a-1][b]) * int(m[a-2][b]) * int(m[a-3][b])
    if (prod > max):
        max = prod
        maxa = a
        maxb = b

def sw(a,b):
    global max,maxa,maxb
    prod = int(m[a][b]) * int(m[a+1][b-1]) * int(m[a+2][b-2]) * int(m[a+3][b-3])
    if (prod > max):
        max = prod
        maxa = a
        maxb = b
        
def w(a,b):
    global max,maxa,maxb
    prod = int(m[a][b]) * int(m[a][b-1]) * int(m[a][b-2]) * int(m[a][b-3])
    if (prod > max):
        max = prod
        maxa = a
        maxb = b


def s(a,b):
    global max,maxa,maxb
    prod = int(m[a][b]) * int(m[a+1][b]) * int(m[a+2][b]) * int(m[a+3][b])
    if (prod > max):
        max = prod
        maxa = a
        maxb = b

def se(a,b):
    global max,maxa,maxb
    prod = int(m[a][b]) * int(m[a+1][b+1]) * int(m[a+2][b+2]) * int(m[a+3][b+3])
    if (prod > max):
        max = prod
        maxa = a
        maxb = b

def ne(a,b):
    global max,maxa,maxb
    prod = int(m[a][b]) * int(m[a-1][b+1]) * int(m[a-2][b+2]) * int(m[a-3][b+3])
    if (prod > max):
        max = prod
        maxa = a
        maxb = b

def e(a,b):
    global max,maxa,maxb
    prod = int(m[a][b]) * int(m[a][b+1]) * int(m[a][b+2]) * int(m[a][b+3])
    if (prod > max):
        max = prod
        maxa = a
        maxb = b

def run(m):
    for a in range(20):
         for b in range(20):
            if (a-3>=0):
                n(a,b)
            if (a+3<=19):
                s(a,b)
            if (b-3>=0): #check the west
                 w(a,b)
                 if (a-3>=0):
                     nw(a,b)
                 if (a+3<=19):
                     sw(a,b)
            if (b+3<20): #check the east
                 e(a,b)
                 if (a-3>=0):
                     ne(a,b)
                 if (a+3<20):
                     se(a,b)


if __name__ == "__main__":
     f = open("data.txt","r")
     

     for x in f.readlines():
         m.append(x.split(" "))
     

     run(m)
     print max
     
     



    