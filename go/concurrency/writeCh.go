package main

import (
	"fmt"
	"time"
)

func main() {
	c := make(chan int)
	go writeToChannel(c, 2)
	time.Sleep(time.Second)
	fmt.Println("Read: ", <-c)
	time.Sleep(time.Second)
	val, ok := <-c
	fmt.Println(val)
	if ok {
		fmt.Println("Channel is open")
	} else {
		fmt.Println("Channel is closed")
		// channel closed: default type value (ex. int is 0)
	}

}

func writeToChannel(c chan<- int, x int) {
	fmt.Println("Before sending....", x)
	c <- x
	close(c)
	fmt.Println("After sending...", x)
}
