#!/usr/bin/env python3
from threading import Thread
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen

#【画像】女性芸能人にガッカリおっぱい多すぎるwwww

url = 'http://newskvip.blog.fc2.com/blog-entry-3095.html'
base_img_url = 'http://blog-imgs-58-origin.fc2.com/n/e/w/newskvip'
href = (x['href'] for x in BS(urlopen(url)).findAll('a', href=True) \
	    if base_img_url in x['href'])

def download_image(url):
	file_name = url.split('/')[-1]
	print("Downloading .. ", url)
	doc = urlopen(url).read()
	with open(file_name, 'wb') as f:
		f.write(doc)

def main():
	threads = (Thread(target=download_image, args=(url,)) for url in href)
	for t in threads: t.start()
	for t in threads: t.join()
if __name__ == '__main__':
	main()
