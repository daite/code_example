package main

import "C"
import "fmt"

//export PrintMessage
func PrintMessage() {
	fmt.Println("A go function")
}

//export Multiply
func Multiply(a, b int) int {
	return a * b
}

func main() {

}

// go build -o usedByC.o -buildmode=c-shared usedByC.go
