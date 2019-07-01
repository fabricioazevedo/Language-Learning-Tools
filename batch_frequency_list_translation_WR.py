# encoding: utf-8

import webbrowser
import pandas as pd
from tkinter import Tk
import csv
root = Tk()
root.withdraw()
from bs4 import BeautifulSoup
import requests 
# while True:
# input("Press Enter to continue...")
# word = root.clipboard_get()
# word = 'listen'

csv_file = open('words_examples.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['sentence', 'translation'])
my_dict = {} #dictionary
lista1 = []
lista2 = []

# list_words = ['listen', 'pain', 'dream']
with open('100words.txt') as f:
    list_words = f.read().split()

lim = 1

for word in list_words:
	# text = "Donnerwetter"
	# root.clipboard_clear()
	# text to clipboard
	# root.clipboard_append(text)
	# text from clipboard
	# clip_text = root.clipboard_get()
	# csv_writer.writerow([words])
	url = 'https://www.wordreference.com/enpt/{}'.format(word)
	# url = 'https://context.reverso.net/traducao/ingles-portugues/{}'.format(word)
	page = requests.get(url).text
	# MacOS
	# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
	# Windows
	chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
	# Linux
	# chrome_path = '/usr/bin/google-chrome %s'
	# webbrowser.get(chrome_path).open(url)

	# page = urlopen(wiki)p
	# soup =  BeautifulSoup(page, "html.parser" ).encode('UTF-8')
	sp =  BeautifulSoup(page,'lxml')

	#---------------- WORD REFERENCE-------------------------------#
	# for wrd in (sp.find_all(class_='ToWrd',limit =3)):
			# wrd1 = wrd.text #.encode('UTF-8')
			# print(wrd1)
			# csv_writer.writerow([])
			
	for st in sp.find_all(class_='FrEx',limit =lim):
			print(st.text)
			sentence = st.text
			my_dict['sentence'] = st.text
			lista1.append(sentence)
			# dict = pd.DataFrame({'sentece':st.text})
			# csv_writer.writerow([sentence])
			
	for trans in sp.find_all(class_='ToEx',limit =lim):
			print(trans.text)
			translation = trans.text
			my_dict['translation'] = trans.text
			lista2.append(translation)
			# dict = pd.DataFrame({'translation':trans.text})
			# csv_writer.writerow([translation])
			
	#---------------- REVERSO CONTEXT-------------------------------#
	# for wrd in (sp.find_all(class_='translation')):
			# wrd1 = wrd.text #.encode('UTF-8')
			# print(wrd1)
			
	# for st in sp.find_all(class_='text',lang='en',limit =2):
			# print(st.text)
			# sentence = st.text
			# csv_writer.writerow([sentence])
			
	# for trans in sp.find_all(class_='text',limit =2):
			# print(trans.text)
			# translation = trans.text
			# csv_writer.writerow([translation])		
		
# csv_file.close()
# csv_columns = ['sentence','translation']

# dict.to_csv(file_name, sep='\t', encoding='utf-8')

# with open('mycsvfile.csv', 'w') as f:  # Just use 'w' mode in 3.x
    # w = csv.DictWriter(f, my_dict.keys())
    # w.writeheader()
    # w.writerow(my_dict)

with open('lista1.txt', 'w') as f:
    for item in lista1:
        f.write("%s\n" % item)
		
with open('lista2.txt', 'w') as f:
	for item in lista2:
		f.write("%s\n" % item)
		
df = pd.DataFrame(lista2,lista1)
df.to_csv('frequencyList.csv')

