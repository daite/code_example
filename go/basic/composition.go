package main

import "fmt"

type a struct {
	XX int
	YY int
}

type b struct {
	AA string
	XX int
}

type C struct {
	A a
	B b
}

func (A a) A() {
	fmt.Println("Function A() for A")
}

func (B b) B() {
	fmt.Println("Function B() for B")
}

func main() {
	var i C
	i.A.A()
	i.B.B()
}
