#!/usr/bin/env python3

from urllib.request import urlopen
from multiprocessing import Process
from threading import Thread
import time

NUM = 100000000

def test(num):
	while num > 0:
		num -= 1

def parallel():
	start = time.time()
	t1 = Thread(target=test, args=(NUM // 2,))
	t2 = Thread(target=test, args=(NUM // 2,))
	t1.start(); t2.start(); t1.join(); t2.join()
	end = time.time()
	print("[parallel] time:", end - start)

def serial():
	start = time.time()
	test(NUM)
	end = time.time()
	print("[serial] time:", end - start)
	
if __name__ == '__main__':
	parallel()
	serial()
