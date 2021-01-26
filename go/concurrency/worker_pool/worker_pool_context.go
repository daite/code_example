package main

import (
	"context"
	"fmt"
	"math/rand"
	"sync"
	"time"
)

var wg sync.WaitGroup

const (
	numOfGoRoutines = 60
	numOfTasks      = 100
)

func genRandomNumber(n int) int {
	return rand.Intn(n)
}

func worker(cx context.Context, id int, ch chan int) {
	wg.Add(1)
	defer wg.Done()
	for {
		select {
		case val := <-ch:
			fmt.Printf("Worker%d: %d\n", id, val)
			time.Sleep(time.Millisecond)
		case <-cx.Done():
			//fmt.Println(cx.Err())
			return
		}
	}
}

func main() {
	rand.Seed(time.Now().UnixNano())

	cx := context.Background()
	cx, cancel := context.WithTimeout(cx, time.Duration(time.Second*2))
	defer cancel()

	ch := make(chan int, numOfGoRoutines)
	go func() {
		for i := 0; i < numOfTasks; i++ {
			ch <- genRandomNumber((i + 65) * 4)
		}
	}()
	for i := 0; i < numOfGoRoutines; i++ {
		go worker(cx, i, ch)
	}
	wg.Wait()

}
