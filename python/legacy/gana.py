#!/usr/bin/env python2
# -*- coding: utf-8 -*
import requests
from scrapy import Selector
import os
import codecs

root_dir_name = '200GANA'
root_dir_path = os.path.join(os.getcwd(), root_dir_name)
urlgen = lambda x : 'http://blog.livedoor.jp'\
					'/kirekawa39-siro/archives/200GANA-%d.html' %x

if not os.path.exists(root_dir_path):
	os.mkdir(root_dir_path)

for movie_num in range(1, 700):

	url = urlgen(movie_num)
	res_text = requests.get(url).text

	img_urls = Selector(text=res_text)\
			   .xpath('//a/@href').re('.*jpg$')

	desc_contents = Selector(text=res_text)\
					.xpath('//blockquote/text()').extract()

	if not img_urls:
		print 'No images!!!!'
		continue

	sub_dir_name = url.split('/')[-1].strip('.html')
	sub_dir_path = os.path.join(root_dir_path, sub_dir_name)
	sub_dir_desc_file_name = os.path.join(sub_dir_path, 'description.txt')

	if not os.path.exists(sub_dir_path):
		os.mkdir(sub_dir_path)

	os.chdir(sub_dir_path)

	with codecs.open(sub_dir_desc_file_name, 'a', encoding='utf-8') as f:
		for content in desc_contents:
			f.write(content)

	for img_url in img_urls:
		cmd = 'wget -nc -t 1 %s &' %img_url
		os.system(cmd)

	os.chdir(root_dir_path)


