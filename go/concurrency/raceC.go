package main

import (
	"fmt"
	"os"
	"strconv"
	"sync"
)

var mu sync.Mutex

func main() {
	arguments := os.Args
	if len(arguments) != 2 {
		fmt.Println("Give me a natural number!")
		os.Exit(1)
	}
	n, err := strconv.Atoi(arguments[1])
	if err != nil {
		fmt.Println(err)
		return
	}
	var wg sync.WaitGroup
	k := make(map[int]int)
	k[1] = 12
	for i := 0; i < n; i++ {
		wg.Add(1)
		go func(j int) {
			defer wg.Done()
			mu.Lock()
			k[j] = j
			mu.Unlock()
		}(i)
	}
	wg.Wait()
	k[2] = 10
	fmt.Printf("k=%#v\n", k)
}
