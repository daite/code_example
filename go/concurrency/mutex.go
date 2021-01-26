package main

import (
	"fmt"
	"os"
	"strconv"
	"sync"
	"time"
)

var (
	m  sync.Mutex
	v1 int
)

func change(i int) {
	m.Lock()
	time.Sleep(time.Second)
	v1++
	if v1%10 == 0 {
		v1 = v1 - 10*i
	}
	m.Unlock()
}

func read() int {
	m.Lock()
	a := v1
	m.Unlock()
	return a
}

func main() {
	var wg sync.WaitGroup
	if len(os.Args) != 2 {
		fmt.Println("Please give me an integer!")
		return
	}
	n, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("%d", read())
	for i := 0; i < n; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			change(i)
			fmt.Printf("-> %d", read())
		}(i)
	}
	wg.Wait()
	fmt.Printf("-> %d\n", read())
}
