package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func pi(precisao float64) float64{
	var i, somatorio, ultimo_somatorio float64 = 0, 0, 0
	for {
		somatorio += 4 * math.Pow(-1,i) * (1 / (2 * i + 1))
		i++
		if math.Abs(somatorio - ultimo_somatorio) < precisao{
			break
		}
		ultimo_somatorio = somatorio
	}
	return somatorio
}

func main() {
	fmt.Println(pi(0.0001))
	precisoes := []float64{1, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001}

	var info,file string
  
	file = "saida.txt"
	dump("Numero Pi real: 3.14159265\n\n", file)
	for i := 0; i < len(precisoes); i++ {
		info =  "Precisão: " + fmt.Sprintf("%.8f", precisoes[i]) + "  Result: " + fmt.Sprintf("%.8f", pi(precisoes[i])) + "\n"
		dump(info, file)
	}
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func dump(info, file string) {

	f, err := os.OpenFile(file, os.O_WRONLY|os.O_APPEND|os.O_CREATE, 0644)
	check(err)
	defer f.Close()

	w := bufio.NewWriter(f)

	w.WriteString(info)
	w.Flush()
}
