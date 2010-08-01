# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="meatz"
__date__ ="$01.08.2010 14:01:35$"

if __name__ == "__main__":
    f = open("data.txt","r")
    sum =0
    for x in f.readlines():
        sum+=int(x)
    print str(sum)[0:10]