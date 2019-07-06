#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webbrowser
import pandas as pd
import csv
from bs4 import BeautifulSoup
import requests 
from requests.exceptions import Timeout
import time
from nltk.tokenize import sent_tokenize, word_tokenize

def page_request(url):
	try:
		print("Page Request...Wait...")
		page = requests.get(url)
		if page is not (None or []):
			print('Request with Success!')
			return page
		else:
			print('Request Denied.')
	except:
		print("Fail Request... Trying Again....")
		time.sleep(60)
		
def write_on_file(file, list):
		for item in list:
			try:
				file.write(item)
				file.write("\n")
			except:
				file.write("\n")
	
def extract_info(soup_find_ , string_match, lim, list):
	buffer = []
	flag = 0 # Check no empty results
	Result = soup_find_.find_all(class_= string_match, limit = lim)
	if Result is ([] or None):
		return list
	else:
		for d in Result:
			buffer.append(d.text)
		def_join = ' | '.join(buffer)
		buffer.clear()
		def_join = def_join + "\n"
		list.append(def_join)
		# print(def_join)
		def_join = ''
		flag = 1
	return list, flag

def write_found(flag, file, string ):
	print(" ")
	
index = 12	

wrd_file = open('bs_buffer{}_00.txt'.format(index),'a+',encoding='utf-8')
defs_file = open('bs_buffer{}_01.txt'.format(index),'a+',encoding='utf-8') 
sents_file = open('bs_buffer{}_02.txt'.format(index),'a+',encoding='utf-8') 
trans_file = open('bs_buffer{}_03.txt'.format(index),'a+',encoding='utf-8') 

sents = []
defs = []
trans = []
wrd = []

with open('buffer_{}.txt'.format(index),'r',encoding='utf-8') as f:
	print("load list of worlds ....")
	# list_words = f.read().split()
	text = f.read()
	list_words = word_tokenize(text)
	print("Load List Finished!")


lim = 1
i=0
j=0
buffer = []

for word in list_words:
	print("Start Processing Word List...")
	time.sleep(1)
	url = 'https://www.wordreference.com/enpt/{}'.format(word)
	print(url)
	# if url is ([] or None):
		# break
	# url = 'https://context.reverso.net/traducao/ingles-portugues/{}'.format(word)
	# page = requests.get(url).text
	page = page_request(url) 
	lim = 2
	sp =  BeautifulSoup(page.text,'lxml')
	# tag = sp.table.name # tr, td
	# table = sp.find('table')
	tables = sp.find_all('table')
	# try:
	i += 1
	print(i)
	print("working on it...\n")
	try:
		sents, flag_s = extract_info(tables[1], "FrEx", lim, sents) #last element append to a list
		trans,flag_t = extract_info(tables[1], "ToEx", lim, trans)
		defs,flag_d = extract_info(tables[1], "ToWrd", lim, defs)
		if (flag_d or flag_t or flag_s): #flag for indicate with something was found
			wrd.append(word + "\n")
			wrd_file.write(wrd[-1])
			defs_file.write(defs[-1])
			sents_file.write(sents[-1]) 
			trans_file.write(trans[-1])
		else:
			print("Error: Flag 0 - Not Match ")
		
		print("Word {} added with success !".format(i))
		# except:
			# print("Fail to process current word: {}".format(i))
	except:
		print("Except -> Word {} Fail do process!".format(i))
		

wrd_file.close()
defs_file.close() 
sents_file.close() 
trans_file.close() 		


	
