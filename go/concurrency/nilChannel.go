package main

import (
	"fmt"
	"math/rand"
	"time"
)

func add(c chan int) {
	sum := 0
	t := time.NewTimer(time.Second)
	for {
		select {
		case input := <-c:
			fmt.Println("[*] Receving: ", input)
			sum += input
		case <-t.C:
			c = nil
			fmt.Println(sum)
		}
	}
}

func send(c chan int) {
	for {
		val := rand.Intn(10)
		fmt.Println("[*] Sending: ", val)
		c <- val
	}
}

func main() {
	c := make(chan int)
	go add(c)
	go send(c)
	time.Sleep(3 * time.Second)
}
