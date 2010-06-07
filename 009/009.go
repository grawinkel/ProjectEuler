package main

/*
pythagorean triplet is a set of three natural numbers a < b < c
for which :
	a^2 + b^2 = c^2
*/

import "fmt"

func main (){
	for a:=1;a<1000;a++{
		for b:=a+1;b<1000;b++{
			for c:=b+1;c<1000;c++{
				if a + b + c == 1000{
					if (a*a)+(b*b)==(c*c){
						fmt.Printf("result: a=%v, b=%v, c=%v: result: %v\n", a,b,c, a*b*c)
					}
				}
			}
		}
	}
}
