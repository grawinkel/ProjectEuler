package main

/*

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? */


/*
The Plan:

If a number is divisible by 20, it is also devisible by 10, 5 and 2
if divisble by 18, also by 9,6,3,2
...
The remaining numbers are 20, 19, 18, 17, 16, 15,14,13,12,11.
Now find the least common multiple of these.

This is done by Primfaktorzergegung of the elements

20 = 2 2 	5
19 = 				19
18 = 2 		3 3
17 = 17
16 = 2 2 2 2
15 = 			3 5
14 = 2 	7
13 = 13
12 = 2 		3 3
11 = 11
2*2*2*2*3*3*5*7*11*13*17*19
solution: 2 2 2 2 3 3 5 7 11 13 17 19  = 232792560
*/

import "fmt"

func main(){

}