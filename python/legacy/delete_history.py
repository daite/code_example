#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from urllib import urlopen
from bs4 import BeautifulSoup as BS
from threading import Thread
import threading

def search_history(bbs_count):
	print 'Searching...%s' %threading.currentThread
	for i in range(*bbs_count):
		url = 'http://xxxx.co.kr/xx/index.xxx?xxx=xxxx&page=%d' %i
		href = (x for x in BS(urlopen(url)).findAll('a', {'class' : 'member_0'}))
		for h in href:
			if u'김민지' in h.string:
				print url

def main():
	t1 = Thread(target=search_history, args=((0, 100),))
	t2 = Thread(target=search_history, args=((100, 200),))
	t3 = Thread(target=search_history, args=((200, 300),))
	t4 = Thread(target=search_history, args=((300, 400),))

	t1.start();t2.start();t3.start();t4.start();
	t1.join();t2.join();t3.join();t4.join();
if __name__ == '__main__':
	main()
