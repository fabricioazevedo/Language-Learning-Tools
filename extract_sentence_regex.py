# coding: utf-8
import re
import csv
import pandas as pd
	
# from googletrans import Translator
# translator = Translator()
f = open('coraline.txt','r',encoding='utf-8') # errors='ignore'
text = f.read()
f.close()

dict = {}

with open('words.txt') as f:
    wordList = f.read().split()

# print(wordList)
list = []

f=open("sentences_books.txt", "a+")

for w in wordList:
	print(w)
	# r1 = '[\s.,].{}.{{10,60}}\s[.,\s]'.format(w)
	# r2 = "([:.,](\s)?.*(\s){}(\s).*[.,]){{1,25}}".format(w)
	r3 = "([.:^,](.[^.,:]*)(\s){}(\s)(.[^.,]*)[.,])".format(w)
	# r4 = "([.:,].*(\s){}(\s)[,.]{{1,25}}$)".format(w)
	rs = re.search(r3,text)
	f.write(w +" -> "+ "[" + rs.group(0) + "]" + "\n")
	print(rs.group(0))
	list.append(rs.group(0))
	# list.append(rs.group(0))
	# start with [:.,] space or not - anything - space - WORD - space - anything - end with [.,]  
	# print(r1)
	# print(r1)
f.close()

df = pd.DataFrame(list,wordList)
df.to_csv('frequencyList.csv')







	
	