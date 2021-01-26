package fib

type Memoized func(int) int

func Channel(ch chan int, counter int) {
	n1, n2 := 0, 1
	for i := 0; i < counter; i++ {
		ch <- n1
		n1, n2 = n2, n1+n2

	}
	close(ch)
}

func FibChannel(n int) int {
	n += 1
	ch := make(chan int)
	go Channel(ch, n)
	var result int
	for num := range ch {
		result = num
	}
	return result
}

func FibSimple(n int) int {
	if n == 0 {
		return 0
	} else if n < 2 {
		return 1
	} else {
		return FibSimple(n-2) + FibSimple(n-1)
	}
}

func Memoize(mf Memoized) Memoized {
	cache := make(map[int]int)
	return func(key int) int {
		if val, ok := cache[key]; ok {
			return val
		}
		temp := mf(key)
		cache[key] = temp
		return temp
	}
}

func FibMemoized(n int) int {
	return Memoize(FibSimple)(n)
}

func SumLoop(nums []int) int {
	sum := 0
	for _, num := range nums {
		sum += num
	}
	return sum
}

func SumRecursive(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	return nums[0] + SumRecursive(nums[1:])
}
