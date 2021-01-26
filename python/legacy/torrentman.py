#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as BS
import urllib
import sys

#####################################################################################
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)" \
			 "AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5"
host_url = 'http://torrentme.net/bbs/'
#proxies = {"http" : "183.207.228.50:81"} # you can uncomment if you want
#####################################################################################

def fetch_bbs_data(keyword):
	'''
	fecth data from bbs url on the basis of keyword
	Items obj consists of "(title, dowload_link)"
	'''
	search_url = host_url + 's.php?k=%s' %keyword
	r = requests.get(search_url)
	items = [(x.string.strip('\r\n\t\t\t\t\t\t\r\n\t\t\t'), host_url + x['href']) \
			for x in BS(r.text).findAll('a', href=True) if 's.php?bo_table' in x['href']]
	for number, item in enumerate(items):
		print '%s : %s' %(number, item[0])
	while True:
		try:
			num = int(raw_input('select the number : '))
			title, link = items[num]
			print 'Downloading: %s' %title
			download_torrent_file(link)
		except ValueError:
				print 'ValueEror!'
		except KeyboardInterrupt:
				sys.exit(1)

def download_torrent_file(bbs_url):
	'''
	1. download torrent file from bbs_url
	2. must set "referer : bbs_url"
	3. to be excluded image files when downloading **
	4. 20 download limits / day -> use proxy server : http://www.freeproxylists.net
	'''
	proxies = None
	r = requests.get(bbs_url, proxies=proxies)
	urls = (x['href'].strip('./') for x in BS(r.text).findAll('a', href=True) \
		            if 'download' in x['href'] and '.torrent' in x.text)
	for url in urls:
		download_url =  host_url + url
		headers = {'Referer' : bbs_url, 'User-Agent' : user_agent}
		try:
			r = requests.get(download_url, headers=headers, proxies=proxies)
			file_name = eval(r.headers['content-disposition'].strip('attachment; filename='))
			#save_file_name = urllib.unquote(file_name)
			with open(file_name, 'wb') as f:
				f.write(r.content)
				print 'Done!'
		except KeyError as e:
			print 'Error Occurred : %s' %e

if __name__ == '__main__':
	keyword = raw_input('input the keyword : ')
	fetch_bbs_data(keyword)
	#url = 'http://torrentman.net/bbs/s.php?bo_table=torrent_variety&wr_id=92594&k=K팝스타&page='
	#http://torrentman.net/bbs/download.php?bo_table=torrent_variety&wr_id=92594&no=1&page=6
	#http://torrentman.net/bbs/download.php?bo_table=torrent_variety&wr_id=92594&no=1&page=6
	#download_torrent_file(url)
