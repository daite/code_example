# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup as BS
import codecs

start_urls = ['http://www.asahi.com/paper/editorial.html?iref=comtop_pickup_p',
              'http://www.asahi.com/paper/editorial2.html']
headers = ('User-Agent', 'nonofyourbusiness')
handler = urllib2.HTTPHandler(debuglevel=1)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)
for url in start_urls:
	req = urllib2.Request(url)
	req.add_header(*headers)
	u = urllib2.urlopen(req)
	result = BS(u).find('div', {'class' : 'ArticleText'}).findAll('p')
	with codecs.open('hi.txt','a', encoding='utf-8') as f:
		for r in result:
			f.write(r.string + '\r\n')
		f.write('\r\n\r\n')
