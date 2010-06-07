package main

import "fmt"


/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

func main (){

	result := 0

	for  i:= 0; i< 1000; i++{
		result += test (i)
	}
	fmt.Printf("result: %v\n",result)
}


func test(i int) int{
	if i % 3 == 0 {
		fmt.Printf("i: %v\n",i)
		return i
	}
	if i % 5 == 0 {
		fmt.Printf("i: %v\n",i)
		return i
	}
	return 0
}



