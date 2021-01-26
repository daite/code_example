#!/usr/bin/env python
#diry code
from zippy import download_torrent_file
from bs4 import BeautifulSoup as BS
import urllib


drama_dict = { '0': 'http://jdramacity.blogspot.kr/2015/01/ghost-writer.html',
	       '1': 'http://jdramacity.blogspot.kr/2015/01/doctors-3.html',
	       '2':'http://jdramacity.blogspot.kr/2015/01/zeni-no-sensou.html',
	       '3':'http://jdramacity.blogspot.kr/2015/01/masshiro.html'
			}
info = '''
		#########################
		# 0. ghost_writer       #
		# 1. doctor3            #
		# 2. zeni no senso      #
		# 3. massiro            #
		#########################
	   '''
while 1:
	try:
		print info
		number = raw_input('input the number : ')
		drama_url = drama_dict[number]
		href = [x['href'] for x in BS(urllib.urlopen(drama_url)).\
		         findAll('a', href=True) if 'zippy' in x['href']]
		print 'select the episode.... (1,2,3...)'
		total_episode = len(href)
		print '%s has %s episode now...' \
				%(drama_url.split('/')[-1].strip('.html'), total_episode)
		epi_number = int(raw_input('Select the episode to download.... : '))
		epi_url = href[epi_number-1]
		download_torrent_file(epi_url)	
	except:
		break
