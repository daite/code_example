#!/usr/bin/env python

import requests
from urlparse import urlparse

#### Global Value #########################################
start_str = "document.getElementById('dlbutton').href = "
###########################################################

def download_torrent_file(url):
	base_url = 'http://' + urlparse(url).netloc
	s = requests.Session()
	doc = s.get(url).text
	start_num = doc.find(start_str)
	end_num = doc[start_num:].find(';')

	final_doc = doc[start_num : start_num + end_num].strip(start_str)
	split_list = final_doc.split('"')
	text1 = split_list[1]
	text2 = eval(split_list[2].strip('(+ )'))
	text3 = split_list[-2]

	down_url =  base_url + text1 + str(text2) + text3
	headers = {'Referer' : url}
	r = s.get(down_url, headers=headers)
	file_name = r.headers['content-disposition'].split("'")[-1]
	print 'Downloading : %s' %file_name
	with open(file_name, 'wb') as f:
		f.write(r.content)

if __name__ == '__main__':
	url = 'http://www73.zippyshare.com/v/NHbN7ogU/file.html'
	download_torrent_file(url)
