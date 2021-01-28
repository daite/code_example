package main

import (
	"fmt"
	"os"
	"reflect"
)

type t1 int
type t2 int

type a struct {
	X    int
	Y    float64
	Text string
}

func (a1 a) compareStruct(a2 a) bool {
	rv1 := reflect.ValueOf(a1)
	rv2 := reflect.ValueOf(a2)
	for i := 0; i < rv1.NumField(); i++ {
		if rv1.Field(i).Interface() != rv2.Field(i).Interface() {
			return false
		}
	}
	return true
}

func printMethods(i interface{}) {
	rv := reflect.ValueOf(i)
	rt := rv.Type()
	fmt.Printf("Type to examine: %s\n", rt)
	for j := 0; j < rv.NumMethod(); j++ {
		t := rt.Method(j).Type
		fmt.Println(rt.Method(j).Name, "--->", t)
	}
}

func main() {
	x1 := t1(100)
	x2 := t2(100)
	fmt.Printf("The type of x1 is %s\n", reflect.TypeOf(x1))
	fmt.Printf("The type of x2 is %s\n", reflect.TypeOf(x2))
	var p struct{}
	rv := reflect.New(reflect.ValueOf(&p).Type()).Elem()
	fmt.Printf("The type of r is %s\n", reflect.TypeOf(rv))
	var f *os.File
	printMethods(f)
}
