package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"sync"
	"time"
)

func timeout(w *sync.WaitGroup, t time.Duration) bool {
	temp := make(chan int)
	go func() {
		time.Sleep(5 * time.Second)
		defer close(temp)
		w.Wait()
	}()
	select {
	case <-temp:
		return false
	case <-time.After(t):
		return true
	}
}

func main() {
	arguments := os.Args
	if len(arguments) != 2 {
		fmt.Println("Need a time duration")
		return
	}
	var wg sync.WaitGroup
	wg.Add(1)
	t, err := strconv.Atoi(arguments[1])
	if err != nil {
		log.Fatalln(err)
	}
	duration := time.Duration(t) * time.Millisecond
	fmt.Printf("Timeout period is %s\n", duration)
	if timeout(&wg, duration) {
		fmt.Println("Timed out!")
	} else {
		fmt.Println("OK")
	}
	wg.Done()
	if timeout(&wg, duration) {
		fmt.Println("Timed out!")
	} else {
		fmt.Println("OK")
	}
}
