package fib

import "testing"

var fibTests = []struct {
	a        int
	expected int
}{
	{0, 0},
	{2, 1},
	{3, 2},
	{4, 3},
	{10, 55},
}

func TestSimple(t *testing.T) {
	for _, ft := range fibTests {
		if v := FibSimple(ft.a); v != ft.expected {
			t.Errorf("FibSimple(%d) returned %d expected %d", ft.a, v, ft.expected)
		}
	}
}

func benchmarkFibSimple(i int, b *testing.B) {
	for n := 0; n < b.N; n++ {
		FibSimple(i)
	}
}
func BenchmarkFibSimple46(b *testing.B) { benchmarkFibSimple(46, b) }

func benchmarkMemoized(i int, b *testing.B) {
	for n := 0; n < b.N; n++ {
		FibMemoized(i)
	}
}

func BenchmarkMemoized46(b *testing.B) { benchmarkMemoized(46, b) }

func benchmarkChannel(i int, b *testing.B) {
	for n := 0; n < b.N; n++ {
		FibChannel(i)
	}
}
func BenchmarkChannel46(b *testing.B) { benchmarkChannel(46, b) }

func benchmarkSumLoops(s []int, b *testing.B) {
	for n := 0; n < b.N; n++ {
		SumLoop(s)
	}
}

func BenchmarkSumLoop40(b *testing.B) {
	benchmarkSumLoops([]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40}, b)
}

func benchmarkSumRecursive(s []int, b *testing.B) {
	for n := 0; n < b.N; n++ {
		SumRecursive(s)
	}
}

func BenchmarkSumRecursive40(b *testing.B) {
	benchmarkSumRecursive([]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40}, b)
}
