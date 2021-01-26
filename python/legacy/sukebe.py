#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#The MIT License (MIT)
# Copyright (c) 2015 daite

# Permission is hereby granted, free of charge, to any person obtaining a 
# copyof this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the 
# Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
# THEAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
# FROM,OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
# IN THE SOFTWARE.

import os
import requests
from collections import namedtuple
from bs4 import BeautifulSoup as BS

class SukebeDownloader:

	"""
	simple torrent downloader from sukebe
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	>>> import sukebe
	>>> s = sukebe.SukebeDownloader(search_words='ムラムラ')
	>>> info = s.search_torrent_file()
	>>> s.download_torrent_file(info)
	>>> u = sukebe.SukebeDownloader(user_id='265295')
	>>> info = u.search_torrent_file(keyword='ムラムラ’)
	>>> u.download_torrent_file(info)
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	"""
	nomo_interests = ['天然むすめ', 'ムラムラってくる素人']
	mo_interests   = ['SIRO', '200GANA', 'TUS', 'CHN', 'ABP']

	def __init__(self, user_id=None, search_words=None, offset=1):
		"""
		url is based on user_id : active user!
		"""
		if user_id is None:
			self.keyword = search_words
			self.url = ('http://sukebei.nyaa.eu/?page=search'
			           '&term={}&offset={}'.format(self.keyword, offset))
		else:
			self.url = 'http://sukebei.nyaa.eu/?user={}'.format(user_id)
		headers = {'User-Agent': 'fuckme'}
		self.soup = BS(requests.get(self.url, 
			       headers=headers).text, 'html.parser')

	def soup_gen(self, tag_name):
		"""
		find all by tag_name
		"""
		return self.soup.findAll('td', {'class': '%s' % tag_name})
	
	def extract_data(self, tag_name, attr_name='text'):
		"""
		extract data from soup_gen
		"""
		if attr_name == 'text':
			return (x.text for x in self.soup_gen(tag_name))
		else:
			return (x.find('a')['href'] for x in self.soup_gen(tag_name))

	def get_torrent_info(self):
		"""
		torrent namedtuple --> TITLE | URL | SIZE | SE | LE | TD
		"""
		titles     = self.extract_data('tlistname')
		urls 	   = self.extract_data('tlistdownload', 'href')
		sizes      = self.extract_data('tlistsize')
		seeders    = self.extract_data('tlistsn')
		leechers   = self.extract_data('tlistln')
		tds    	   = self.extract_data('tlistdn')

		torrent = namedtuple('torrent', 
				     ['title', 'url', 'size', 
				      'seeder', 'leecher', 'td'])
		return (torrent(title, url, size, seeder, leecher, td) 
				for title, url, size, seeder, leecher, td in 
				zip(titles, urls, sizes, seeders, leechers, tds))
												
	def download_torrent_file(self, torrent_object):
		"""
		download torrent files by using curl
		torrent_object is namedtuple created by search_torrent_file
		"""
		for t in torrent_object:
			title = t.title.replace('/', '')
			cmd = 'curl -# "{}" -o "{}.torrent" &'.format(t.url, title)
			os.system(cmd)

	def search_torrent_file(self, seeder=100, keyword=None):
		"""
		search torrents by keyword & seeder
		"""
		info = self.get_torrent_info()
		try:
			if self.keyword:
				keyword = self.keyword
		except AttributeError:
				keyword = keyword
		return (x for x in info if keyword in x.title
			    and int(x.seeder) > seeder
		       )

def download_handler(mode='search'):

	nomo_interests = SukebeDownloader.nomo_interests
	mo_interests   = SukebeDownloader.mo_interests

	if mode == 'search':
		keyword = mo_interests[0]
		s = SukebeDownloader(search_words=keyword)
		s.download_torrent_file(s.search_torrent_file())

	elif mode == 'user':
		s = SukebeDownloader(user_id='265295')
		for keyword in nomo_interests:
			s.download_torrent_file(s.search_torrent_file(keyword=keyword))

	else:
		print('there is no mode!!')

if __name__ == '__main__':
	download_handler()
