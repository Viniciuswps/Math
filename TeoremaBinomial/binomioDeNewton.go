package main

import (
    "strconv"
	"fmt"
	"math"
)

// calcula o número binomial (n k)  =  n! / (k!(n-k)!)
func numeroBinomial(n,k int) int {
	return fatorial(n) / (fatorial(k) * fatorial(n-k))
}

func fatorial(n int) int{
	if (n == 0){
		return 1
	} else {
		return n * fatorial(n-1)
	}
}

func imprimeTrianguloDePascal(size int) {
	for i:=0; i < size; i++{
		for j:=0; j < i+1; j++ {
			fmt.Print(numeroBinomial(i,j))
			fmt.Print(" ")
		}
		fmt.Println()
	}
}

//(x + a) ^ n = sum,k=0 -> n ( n k) * x ^ (n-k) * a ^k
func teoremaBinomial(a,n int) string{
	result := ""
	for k:= 0; k <= n; k++ {
		coeficiente := numeroBinomial(n,k)
		aElevadoK := int(math.Pow(float64(a), float64(k)))
		stringaux := strconv.Itoa(coeficiente * aElevadoK) + " * x^" + strconv.Itoa(n-k) + "   "
		result += stringaux 
	}
	expressao := "(x + " + strconv.Itoa(a)  + ")^" +  strconv.Itoa(n) + " =  "
	return expressao + result
}

func main() {
	imprimeTrianguloDePascal(10)
	// output
	// 1
	// 1 1
	// 1 2 1
	// 1 3 3 1
	// 1 4 6 4 1
	// 1 5 10 10 5 1
	// 1 6 15 20 15 6 1
	// 1 7 21 35 35 21 7 1
	// 1 8 28 56 70 56 28 8 1
	// 1 9 36 84 126 126 84 36 9 1

	fmt.Println(teoremaBinomial(2,0))
	fmt.Println(teoremaBinomial(2,1))
	fmt.Println(teoremaBinomial(2,2))
	fmt.Println(teoremaBinomial(2,3))
	// output
	// (x + 2)^0 =  1 * x^0
	// (x + 2)^1 =  1 * x^1   2 * x^0
	// (x + 2)^2 =  1 * x^2   4 * x^1   4 * x^0
	// (x + 2)^3 =  1 * x^3   6 * x^2   12 * x^1   8 * x^0
}