import requests
from bs4 import BeautifulSoup as BS
import os
import re


def search_torrent(search_word, episode='.', file_extension='mkv'):
	url = 'http://www.bt8.nl/index.php?movie=%s' %search_word
	r = requests.get(url)
	s_code = r.status_code
	if s_code == 200:
		tr_tags = (x for x in BS(r.text).findAll('tr'))
		for tr_tag in tr_tags:
			all_info =  tr_tag.findAll('td')
			if len(all_info) == 5:
				if all(ord(c) < 128 for c in all_info[1].text):
					title = all_info[1].text
				else:
					title = '.'.join(all_info[1].text.\
						    encode('cp949', errors='ignore').split('.')[1:])
				magnet = all_info[4].find('a', href=True)['href'].split('&')[0]
				if re.search(search_word, title.lower(), re.IGNORECASE) \
					and episode in title.lower() and title.endswith(file_extension):
					print title, '\n', magnet
					print '*' * 60
					return 
	else:
		print s_code

def start_torrent(magnet):
	print 'starting downloading torrent....'
	torrent_app = r'E:\ST\uTorrent.exe'
	cmd = 'start %s "%s"' % (torrent_app, magnet)
	os.system(cmd)

def test():
	program = ["I'm.home", "pokitto", "wagayae", "rintaro", "algernon"]
	for p in program:
		search_torrent(p)


if __name__ == '__main__':
	test()
	# search_words = "Pokitto"
	# episode = '05'
	# search_torrent(search_words, episode)
