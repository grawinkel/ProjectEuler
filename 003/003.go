package main

/*
	The prime factors of 13195 are 5, 7, 13 and 29.
	What is the largest prime factor of the number 600851475143 ?
*/


import "fmt"


func main (){
	var foo uint64 = 600851475143
	var	factor uint64 = 0
	primes := sieve()
	for {
		factor = <- primes
//		fmt.Printf("new factor=%v\n",factor)		
		for{
			if foo % factor == 0{
				foo = foo / factor
				fmt.Printf("foo=: %v - factor = %v \n",foo, factor)
			}else {
				break
			}
		}	
	}
	fmt.Printf("result: %v\n",factor)
}


 
func sieve() chan uint64 {
	out := make (chan uint64)
	go func(){
		ch := generate()
		for {
			prime := <-ch
			out <- prime
			ch = filter (ch, prime)
		}
	}()
	return out
}


// Send the sequence 2, 3, 4, ... to channel 'ch'.
func generate() chan uint64 {
    ch := make(chan uint64)
    go func(){
      var i uint64 = 0
      for i = 2; ; i++ {
         ch <- i
      }
    }()
    return ch
 }

// Copy the values from channel 'in' to channel 'out',
// removing those divisible by 'prime'.
func filter(in chan uint64, prime uint64) chan uint64{
//	fmt.Printf("created new filter %v\n", prime)
	out := make (chan uint64)
	go func(){
		for {
			if i:= <- in; i % prime != 0 {
				out <- i
			}
		}
	}()
	return out
}

