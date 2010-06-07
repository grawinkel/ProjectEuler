package main

/*
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

*/


import "fmt"


func main(){

	var maxn uint64= 0
	var maxcnt uint64 = 0
	var cnt uint64= 0
	var i uint64
	for i=1 ;i <=1000000; i++{
		cnt = find(i)
		if cnt > maxcnt{
			maxcnt = cnt
			maxn = i
			
			fmt.Printf("New maxn: %v, maxcnt: %v\n", maxn, maxcnt)
		}
	}		
	
	fmt.Printf("Result: %v\n", maxn)
}

func find(n uint64) uint64{
	var cnt uint64 = 0
	for{
		if n == 1{
			return cnt
		}else if n % 2 == 0{
			// even
			n = n/2
			cnt++
		}else{
			n = (3*n)+1
			cnt++
		}
	}
	return cnt
}


