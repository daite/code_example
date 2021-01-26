package main

import (
	"fmt"
	"sync"
	"time"
)

/*
	createjob을 이용해 item을  conveychannel로 보낸다.
	conveychannel로 다 보냈으면 channel를 close 한다.
	그 후 작업자가  conveychannel를 통해서 item를 가져와서 square를 계산하여
	resultchannel로 보낸다.
	resultchannel로 더 이상 보낼 데이터가 없으면 resultchannel를 close 한다.
	마지막으로 resultchannel로 부터 데이터를 읽어온다.

	[WorkerID #9] started job
	[WorkerID #2] started job
	[WorkerID #6] started job
	[WorkerID #1] started job
	[WorkerID #7] started job
	[WorkerID #8] started job
	[WorkerID #9] completed job: 1
	[WorkerID #2] completed job: 9
	[WorkerID #6] completed job: 16
	[WorkerID #1] completed job: 4
	[WorkerID #7] completed job: 25
	[WorkerID #8] completed job: 36
	[WorkerID #4] started job
	[WorkerID #5] started job
	[WorkerID #0] started job
*/

var (
	conveyChannel = make(chan Item, 10)
	resultChannel = make(chan Data, 10)
	wg            sync.WaitGroup
)

type Item struct {
	tagId  int
	number int
}

type Data struct {
	workerId int
	square   int
}

func createJob(n int) {
	for i := 0; i < n; i++ {
		conveyChannel <- Item{i, i}
	}
	close(conveyChannel)
}

func DoJob(n int) {
	for i := 0; i < n; i++ {
		wg.Add(1)
		go worker(i)
	}
	wg.Wait()
	close(resultChannel)
}

func worker(workerId int) {
	defer wg.Done()
	for item := range conveyChannel {
		fmt.Printf("[WorkerID #%d] started job\n", workerId)
		resultChannel <- Data{workerId, item.number * item.number}
		time.Sleep(time.Millisecond)
	}
}

func main() {
	go createJob(30) // 30 tasks
	go DoJob(10)     // 10 workers
	for data := range resultChannel {
		fmt.Printf("[WorkerID #%d] completed job: %d\n", data.workerId, data.square)
	}
}
