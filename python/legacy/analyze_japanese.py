#!/usr/bin/env python
# coding: utf-8
# reference : http://developer.yahoo.co.jp/webapi/jlp/ma/v1/parse.html

# filter:##################################
# 1 : 형용사                              #
# 2 : 형용동사                            #
# 3 : 감동사                              # 
# 4 : 부사                                #
# 5 : 연체사                              #
# 6 : 접속사                              #
# 7 : 접두사                              #
# 8 : 접미사                              #
# 9 : 명사                                #
# 10 : 동사                               #
# 11 : 조사                               #
# 12 : 조동사                             #
# 13 : 특수（구두점, 괄호, 기호등）       #
###########################################

import requests
from bs4 import BeautifulSoup as BS
import codecs
import urllib

#####################################################################
app_id = 'your id'
app_url = 'http://jlp.yahooapis.jp/MAService/V1/parse?appid=%s&'\
	      'results=ma&filter=%s&sentence=%s'
editorial_url = 'http://www.asahi.com/paper/editorial.html'
UTF8 = 'utf-8'
#####################################################################

def analyze_japanese_text(app_id, search_filter, mode='editorial'):

	if mode == 'editorial': target = get_text_from_editorial()
	else: target = get_text_from_file()

	for sentence in target:
		url = app_url %(app_id, search_filter, sentence)
		r = requests.get(url)
		status_code = r.status_code
		if status_code == 200:
			print '[%s] ===> [%s] OK' %(mode, status_code)
			for word in BS(r.text).findAll('word'):
				category = word.find('pos').text
				kanji = word.find('surface').text
				hiragana = word.find('reading').text
				with codecs.open('output.txt', 'a', encoding=UTF8) as f:
					japanese_meaning = get_japanese_meaning(kanji)
					text = '[%s]\t%s\t%s\t%s' %(category, kanji, hiragana, japanese_meaning)
					f.write(text + '\r\n')
		else:
			print '[check] %s' %status_code
	dedupe()

def get_text_from_editorial():
	soup = BS(requests.get(editorial_url).content)
	div_tag = soup.find('div', {'class': 'ArticleText'})
	for p_tag in div_tag.findAll('p'):
		yield p_tag.text

def get_text_from_file():
	with codecs.open('somefile.txt', encoding='utf-8') as f:
		for sentence in f.readlines():
			yield sentence

def dedupe():
	print 'deduping.....'
	text_list = set()
	with codecs.open('output.txt', 'r', encoding='utf-8') as f:
		for x in f.readlines() : text_list.add(x) 
		for text in text_list:
			with codecs.open('deduped_output.txt', 'a', encoding=UTF8) as g:
				g.write(text)

def get_korean_meaning(japanese_word):
	url = 'http://jpdic.naver.com/search.nhn?range=all&q='\
	      '%s&sm=jpd_hty' %japanese_word
	try:
		korean_meaning = BS(requests.get(url).text).findAll('a', {'class':'kor_link'})
		choice_first = korean_meaning[0].text
		choice_second = korean_meaning[1].text
		choice_third = korean_meaning[2].text
		korean_meaning = '%s, %s, %s' %(choice_first, choice_second, choice_third)
	except:
		korean_meaning = 'Error!'
	return korean_meaning

def get_japanese_meaning(japanese_word):
	url = 'https://kotobank.jp/word/%s' %japanese_word
	try:
		japanese_meaning = BS(requests.get(url).text).\
		                   find('meta', {'property':'og:description'})['content']
	except:
		japanese_meaning = 'errors!'
	return japanese_meaning

if __name__ == '__main__':
	#get_news_data()
	analyze_japanese_text(app_id, '1|2|4|6|9|10|11|12', mode='text')
	#print get_japanese_meaning('切付ける').encode('cp949', errors='ignore')
