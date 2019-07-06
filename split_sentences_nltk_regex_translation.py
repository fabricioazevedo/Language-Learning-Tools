#!/usr/bin/env python
# -*- coding: utf-8 -*-

from textblob import TextBlob
from nltk.tokenize import  sent_tokenize, word_tokenize
import time
import re
import pandas as pd

def translit(text, language):
	trans_blob = TextBlob(text)
	try:
		trans = trans_blob.translate(from_lang=language, to='en')
	except:
		return ''
	return trans
	
language = "ru"

with open('ic3peak_interview.txt','r',encoding='utf-8') as f:
	print("load list of worlds ....")
	# list_words = f.read().split()
	text = f.read()
	print("text loaded ! ")
name_file = 'list_senteces_'	
index = 'ic3peak'
sents = open('{}{}_sents.txt'.format(name_file, index), 'w' ,encoding='utf-8')
trans = open('{}{}_trans.txt'.format(name_file, index), 'w' ,encoding='utf-8')
mode = 2 # mode 1 -> NLTK ; mode 2 -> REGEX

if mode == 1:
	sentences = sent_tokenize(text)
	for s in sentences:
		sents.write(s)
		sents.write("\n")	
	
if mode == 2:
	r1 = "[.:^,'""-].[^.,:-?'!""]*[-.,?'!""]"  # match any sentence
	r1_c = re.compile(r1)
	matches = re.findall(r1, text)
	sentences = matches
	for m in matches:
		sents.write(m)
		sents.write("\n")

print(len(matches))
	
i = 0
for s in sentences:
	i += 1
	print('sentence number: {} has been processed....'.format(i))
	time.sleep(1)
	trans_text = str(translit(s,language))
	trans.write(trans_text)
	trans.write("\n")
	
sents.close()
trans.close()

try:
	df = pd.DataFrame(sents, trans)
	df.to_csv('csvSentencesTranslation.csv')
except:
	print("Fail to generate .csv file")