package main

import (
	"flag"
	"fmt"
	"sync"
)

func main() {
	n := flag.Int("n", 10, "number of goroutines")
	flag.Parse()
	count := *n
	fmt.Printf("Going to create %d goroutines\n", count)
	var wg sync.WaitGroup
	fmt.Printf("%#v\n", wg)
	for i := 0; i <= count; i++ {
		wg.Add(1)
		go func(x int) {
			defer wg.Done()
			fmt.Printf("%d ", x)
		}(i)
	}
	// wg.Add(1); deadlock
	// wg.Done(); negative waitgroup counter
	wg.Wait()
}
