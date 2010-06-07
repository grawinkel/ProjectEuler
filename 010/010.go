package main

/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
*/

import "fmt"

const size int = 2000001 //adresses from 0 - 2.000.000
func main (){

	var a [size+1]bool
	var x int = 0
	
	for i:=2; i<len(a);i++{
		a[i]=true
	}
	
	for i:=2; i<len(a);i++{
		if a[i]{
			//this value was not sieved and therefore is a prime!
			x = i
			for {
				//wipe all multiples
				x+=i
				if x <= size{
				a[x]=false
				//	fmt.Printf("wiped %v as a multiple of %v\n",x,i)
				}else{
					break
				}			
			}
		}
	}

	//to big for int
	var result uint64 = 0

	for j:=2; j<len(a);j++{
		
		if a[j]{
			result += uint64(j)
		}
	}
	fmt.Printf("result: %v\n",result )

}
