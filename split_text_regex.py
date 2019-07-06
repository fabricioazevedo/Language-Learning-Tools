# coding: utf-8
import re
import csv
import pandas as pd

# from googletrans import Translator
# translator = Translator()
# f = open('american_gods.txt','r',encoding='utf-8') # errors='ignore'
# text = f.read()
# f.close()

# with open('america.txt') as f:
    # wordList = f.read().split()

list_w = [] # list of worlds
list_s = [] # list of sentences

r1 = "[.:^,'""-].[^.,:-?'!""]*[-.,?'!""]"  # match any sentence
# r3 = "([.:^,'""](.[^.,:?'!""]*)(\s){}(\s)(.[^.,:?'!""]*)[.,?'!""])".format(w)


textfile = open('ic3peak_sentences.txt','r',encoding='utf-8')
filetext = textfile.read()
textfile.close()
r1_c = re.compile(r1)
sent = open('sentences_ic3.txt','a+',encoding='utf-8')

matches = re.findall(r1, filetext)

for item in matches:
	sent.write(item)
	sent.write("\n")

print(len(matches))

# for match in re.findall(r1, filetext):
	# if match:
		# print(match.encode("utf-8"))
		# sent.write(match.encode("utf-8"))
	# else:
		# print("None!")
