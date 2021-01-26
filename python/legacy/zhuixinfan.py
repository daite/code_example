# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import gevent
from gevent import monkey
monkey.patch_all()

from bs4 import BeautifulSoup as BS
from collections import namedtuple
from urllib.parse import urljoin
import http.client
import requests
import time
import os

# 3rd party library version info
# >>> import gevent
# >>> gevent.__version__
# '1.1rc4.dev0'
# >>> import requests
# >>> requests.__version__
# '2.9.1'
# >>> import bs4
# >>> bs4.__version__
# '4.4.1'

dramas = {'special_list'      : 'http://zhuixinfan.com/viewtvplay-592.html',
          'naomi_to_nanako'   : 'http://zhuixinfan.com/viewtvplay-593.html',
          'dame_na_watashi'   : 'http://zhuixinfan.com/viewtvplay-591.html',
          'toyko_sentimental' : 'http://zhuixinfan.com/viewtvplay-594.html',
	  'never_let_me_go'   : 'http://zhuixinfan.com/viewtvplay-596.html',
          'fragile'           : 'http://zhuixinfan.com/viewtvplay-597.html',
          'kazoku_no_katachi' : 'http://zhuixinfan.com/viewtvplay-599.html',
	  'aibou_season14'    : 'http://zhuixinfan.com/viewtvplay-109.html',
	  'itsuka_kono'       : 'http://zhuixinfan.com/viewtvplay-600.html'
	 } 

headers = {'Host': 'zhuixinfan.com',
           'User-Agent': "Mozilla/5.0 (Windows NT 6.1)" 
	   "AppleWebKit/537.36 (KHTML, like Gecko)"
           "Chrome/41.0.2228.0 Safari/537.36"
          }

def get_soup(url):
	return BS(requests.get(url, headers=headers).content, 'html.parser')

def get_magnet(title, resource_url):
	drama_data = namedtuple('drama_data', ['title', 'magnet_url'])
	magnet_url = get_soup(resource_url).find('dd', {'id': 'torrent_url'}).text
	return drama_data(title, magnet_url)


def get_data_list(view_url):
	host_url = '/'.join(view_url.split('/')[:-1])
	data = ((x.text, urljoin(host_url, x['href']))
	    	for x in get_soup(view_url).findAll('a', href=True) 
	    	if 'viewresource' in x['href'])
	jobs = [gevent.spawn(get_magnet, title, res_url) 
	        for title, res_url in data]
	gevent.wait(jobs)
	return jobs

def download_handler(view_url):
	data_list = [job.value for job in get_data_list(view_url)]
	for num, obj in enumerate(data_list, 1):
		print('{} --> {}'.format(num, obj.title))
	try:
		n = int(input('select the number: '))
		magnet_url = data_list[n-1].magnet_url
		cmd = 'open -a utorrent.app "{}"'.format(magnet_url)
		os.system(cmd)
	except Exception as e:
		print('[info] ==> raised exception : {}'.format(e))

def timethis(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		func(*args, **kwargs)
		end = time.time()
		print('time: {}'.format(end-start))
	return wrapper

def main(debug_level):
	http.client.HTTPConnection.debuglevel = debug_level
	data = [(n, t) for n, t in enumerate(sorted(dramas.keys()), 1)]
	for n, t in data:
		print('{} ====> {}'.format(n, t))
	try:
		num = int(input('select drama number : '))
		view_url = dramas[data[num-1][1]]
		download_handler(view_url)
	except Exception as e:
		print('[info] ==> raised exception : {}'.format(e))
	
if __name__ == '__main__':
	main(debug_level=0)
