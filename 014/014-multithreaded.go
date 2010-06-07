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
//import "time"

const size uint64 = 1000000

type Result struct {n,cnt uint64}


func main(){

	fin := make (chan int)
	c := make(chan Result)    
	go aggregate(c)
	

	go check(1,449999, c, fin)
	go check(500000,1000000,c,fin)
	
	//wait for the two routines
	<-fin	
	<-fin

}

func aggregate(c chan Result){
	var r Result 
	var max Result
	var i uint64
	for i=1; i <=size; i++{
		r = <-c
		
		if r.cnt > max.cnt{
			fmt.Printf("New max.n=%v, max.cnt=%v\n",max.n, max.cnt)
			max = r
		}
		
		//fmt.Printf("n=%v, cnt=%v\n",r.n, r.cnt)
	}
	
	fmt.Printf("result: n=%v, cnt=%v\n", max.n, max.cnt)
	
}


func check(from,to uint64, c chan Result, fin chan int){
	//fmt.Printf("checking from:%v to:%v\n", from, to)
	var i uint64
	for i=from; i <=to; i++{
		var r Result
		r.n = i
		r.cnt = getCnt(i)
		c <- r
	}
	
	//announce that this routine has finished
	fin <- 1
}


func getCnt(n uint64) uint64{
var cnt uint64=0
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
return 0
}
