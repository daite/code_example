package main

import (
	"fmt"
	"os"
	"sync"
	"time"
)

var Password = secret{password: "myPassword"}

type secret struct {
	RWM      sync.RWMutex
	M        sync.Mutex
	password string
}

func change(c *secret, pass string) {
	c.RWM.Lock()
	fmt.Println("LChange")
	time.Sleep(10 * time.Second)
	c.password = pass
	c.RWM.Unlock()
}

func show(c *secret) string {
	c.RWM.RLock()
	fmt.Print("show")
	time.Sleep(3 * time.Second)
	defer c.RWM.RUnlock()
	return c.password
}

func showWithLock(c *secret) string {
	c.M.Lock()
	fmt.Println("show with lock")
	time.Sleep(3 * time.Second)
	defer c.M.Unlock()
	return c.password
}
func main() {
	var showFunction = func(c *secret) string { return "" }
	if len(os.Args) != 2 {
		fmt.Println("Using sync.RWMutex!")
		showFunction = show
	} else {
		fmt.Println("Using sync.Mutex")
		showFunction = showWithLock
	}
	var wg sync.WaitGroup
	fmt.Println("Pass: ", showFunction(&Password))
	for i := 0; i < 15; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			fmt.Println("Go pass: ", showFunction(&Password))
		}()
	}
	go func() {
		wg.Add(1)
		defer wg.Done()
		change(&Password, "123456")
	}()
	wg.Wait()
	fmt.Println("Pass: ", showFunction(&Password))
}
