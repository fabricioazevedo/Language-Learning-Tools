# coding: utf-8
import re
import csv
import pandas as pd
from translate import Translator

# from googletrans import Translator
# translator = Translator()
f = open('american_gods.txt','r',encoding='utf-8') # errors='ignore'
text = f.read()
f.close()

translator= Translator(to_lang="pt-br")
dict = {}

with open('america2.txt') as f:
    wordList = f.read().split()

# print(wordList)
list_w = [] # list of worlds
list_s = [] # list of sentences
list_t = [] #translations
f=open("sentences_books.txt", "a+")

for w in wordList:
	print(w)
	# r1 = '[\s.,].{}.{{10,60}}\s[.,\s]'.format(w)
	# r2 = "([:.,](\s)?.*(\s){}(\s).*[.,]){{1,25}}".format(w)
	r3 = "([.:^,](.[^.,:]*)(\s){}(\s)(.[^.,]*)[.,])".format(w)
	# r4 = "([.:,].*(\s){}(\s)[,.]{{1,25}}$)".format(w)
	rs = re.search(r3,text)
	if rs: # Check if there is any match 
		f.write(w +" -> "+ "[" + rs.group(0) + "]" + "\n")
		print(rs.group(0))
		list_w.append(w)
		list_s.append(rs.group(0))
		# list_t.append(translator.translate(rs.group(0)))
	else:
		wordList.remove(w)
		print(w +" :was removed")
		

	# list.append(rs.group(0))
	# start with [:.,] space or not - anything - space - WORD - space - anything - end with [.,]  
	# print(r1)
	# print(r1)
f.close()
print(len(list_w),len(list_s),len(list_t))
# df = pd.DataFrame(list,wordList)
# print(len(list),len(wordList))
# df.to_csv('frequencyList_sentences.csv')

df = pd.DataFrame(list_s,list_w)
df.to_csv('frequencyList.csv')







	
	