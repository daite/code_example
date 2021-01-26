#!/usr/bin/env python3
from threading import Thread
import urllib.request 
from bs4 import BeautifulSoup as BS

url = 'http://www.bbc.co.uk/podcasts/series/globalnews'
href = (x['href'] for x in BS(urllib.request.urlopen(url))\
		.findAll('a', href=True) if '.mp3' in x['href'])

def download(url):
	file_name = url.split('/')[-1]
	print('Downloading..', file_name)
	data = urllib.request.urlopen(url).read()
	with open(file_name, 'wb') as f:
		f.write(data)

def main():
	threads = (Thread(target=download, args=(url,)) for url in href)
	for t in threads:
		t.start()
	for t in threads:
		t.join()
if __name__ == '__main__':
	main()
