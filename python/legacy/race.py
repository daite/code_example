#!/usr/bin/env python3
# ('total_sum:', 1999000)
# ('total_sum:', 1999000)
# ('total_sum:', 1999000)
#-------------------------------
import threading
total_sum = 0
lock = threading.Lock()
def test(x, y):
	global total_sum
	with lock:
		for i in range(x,y): 
			total_sum += i
def test2(x, y):
	global total_sum
	for i in range(x,y): 
		total_sum += i

if __name__ == '__main__':
	for i in range(20):
		t1 = threading.Thread(target=test, args=(0, 1000))
		t2 = threading.Thread(target=test, args=(1000, 2000))
		t1.start(); t2.start(); t1.join(); t2.join()
		print("total_sum:", total_sum)
		total_sum = 0
