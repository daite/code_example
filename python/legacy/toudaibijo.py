#!/usr/bin/env python
from bs4 import BeautifulSoup as BS
from urllib import urlopen
import subprocess

url = 'http://www.asahi.com/and_M/gallery/141219_toudaibijo/girl%.2d.html'
img_url = (BS(urlopen(u)).find('meta', {'property' : 'og:image'})['content'] for u in (url %i for i in range(1, 36)))
for i in img_url :  subprocess.call('start wget %s' %i, shell=True)
