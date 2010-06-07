package main

/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
*/



import "fmt"


func main (){
	
	var	result uint64 = 0
	primes := sieve()
	for i:= 1; i<=10001; i++{
		result = <- primes
//		fmt.Printf("prime: %v = %v\n",i,result)			
	}
	fmt.Printf("result: %v\n",result)
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
	//fmt.Printf("created new filter %v\n", prime)
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


