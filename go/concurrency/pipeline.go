package main

import (
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"time"
)

var (
	CLOSEA = false
	DATA   = make(map[int]bool)
)

func random(min, max int) int {
	return rand.Intn(max-min) + min
}

func first(min, max int, out chan<- int) {
	for {
		if CLOSEA {
			close(out)
			return
		}
		out <- random(min, max)
	}
}

func second(out chan<- int, in <-chan int) {
	for x := range in {
		fmt.Print(x, " ")
		_, ok := DATA[x]
		if ok {
			CLOSEA = true
		} else {
			DATA[x] = true
			out <- x
		}
	}
	fmt.Println()
	close(out)
}

func third(in <-chan int) {
	sum := 0
	for x := range in {
		sum += x
	}
	fmt.Printf("The sume of the random numbers: %d\n", sum)
}

func main() {
	if len(os.Args) != 3 {
		fmt.Println("Need two integer parameters")
		os.Exit(1)
	}
	n1, _ := strconv.Atoi(os.Args[1])
	n2, _ := strconv.Atoi(os.Args[2])
	if n1 > n2 {
		fmt.Printf("%d should be smaller than %d\n", n1, n2)
		return
	}
	rand.Seed(time.Now().UnixNano())
	a := make(chan int)
	b := make(chan int)
	go first(n1, n2, a)
	go second(b, a)
	third(b)
}
