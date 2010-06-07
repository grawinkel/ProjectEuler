package main

/*

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.

*/


import "fmt"
import "math"

func main (){

   result := 0
   pal := 0
	maxa :=0
	maxb :=0
	for a:=800; a < 1000; a ++{
		for b:=800; b < 1000; b ++{
			pal = a * b
			if checkPalindrome(pal){
				//pal is a palindrome
				if pal > result {
					result = pal
					maxa = a
					maxb = b
				}
				fmt.Printf("%v\n",result)
			}
		}
	}
	fmt.Printf("max: %v, a=%v,b=%v",result,maxa,maxb)
	
}



func extractDigit(number int, digit int) int{
	x := number
	//cut off via modula
	x = x % int ( math.Pow10(1+digit))
	
	//cut off the remainder
	x = x / int ( math.Pow10(digit))	
	
	return x
}

/*
	returns the number of digits of x
*/
func getNumDigits (x int) int {
	return int ( 1+ math.Floor( math.Log10(float64(x))) )
}
 
func checkPalindrome(x int) bool{
	d:= getNumDigits(x) -1
	a:=0
	b:=0
//	fmt.Printf("checking: x=%v with digits(x)=%v\n", x,d)
	for i:=0; i<=d;i++{
		a = extractDigit(x,i)
		//fmt.Printf("a(%v)=%v\n", i, a)
		b = extractDigit(x, d-i)
		//fmt.Printf("b(%v)=%v\n", d-i, b)
		if a != b{
			return false
		}
	}
	return true
}



 
 