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
	fmt.Println(teoremaBinomial(2,0))
	fmt.Println(teoremaBinomial(2,1))
	fmt.Println(teoremaBinomial(2,2))
	fmt.Println(teoremaBinomial(2,3))
}