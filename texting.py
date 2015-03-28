#!/usr/bin/env python

import string
import re
from collections import OrderedDict

d={'A':2,'B':2,'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,'I':4,'J':5,'K':5,'L':5,'M':6,'N':6,'O':6,'P':7,'Q':7,'R':7,'S':7,'T':8,'U':8,
'V':8,'W':9,'X':9,'Y':9,'Z':9,' ':'*'}

d1={2:['A','B','C'],3:['D','E','F'],4:['G','H','I'],5:['J','K','L'],6:['M','N','O'],7:['P','Q','R','S'],8:['T','U','V'],9:['W','X','Y','Z']}

bnc_str=""


def text_to_nums(s):
	"""for key in d:
		print '%c:%s' %(key,d[key])"""
	
	#print s
	
	num_string=''.join(str(d[ch]) for ch in s)
	
	#print num_string
	
	return num_string

def nums_to_text(num_string):
	li=[]
	li=num_string.split('*')
	d2=OrderedDict()
	for num_word in li:
		textonyms_li=[]
		textonyms_li=textonyms(num_word)
		d2[num_word]=textonyms_li
	
	#print d2
	
	"""need to sort these list values based on bnc frequency list"""
	
	handler=open('all.num.o5.txt')
	
	global bnc_str
	bnc_str=handler.read()
	
	all_words=[]
		
	for k in d2:
		print k,d2[k]
		s_words=[]
		d3={}
		d4={}
		for item in d2[k]:
			match=re.search(r'(\S)* %s '%(item.lower()),bnc_str)
			s=match.group()
			d3[item]=s.split()[0]
			for k in d3:
				d4[int(d3[k])]=k
			#print sorted(d4)
		for k in sorted(d4):
			s_words.append(d4[k])
		#print s_words
		all_words.append(s_words[::-1])
	
	print all_words			
	
def textonyms(text):
	"""to find all textonyms for a given word"""
	handler=open('words.txt')
	words=[]
	
	all_possible=[]
	
	for line in handler:
		words.append(str(line).strip())
	
	
	for word in words:
		if text==text_to_nums(word):
			all_possible.append(word)
	
	
	return all_possible
	

def change_string(s):
	"""
	covert all to upper case
	remove all punctuations
	space converted to '*'
	"""	
	s=s.upper()
	exclude=set(string.punctuation)
	
	"""print exclude"""
	
	final_s=''.join(ch for ch in s if ch not in exclude)
	
	"""print final_s"""
	
	return final_s
	

def main():
	s=raw_input('Enter the string\n')
	"""text_to_nums(change_string(s))"""
	
	nums_to_text(s)
	
	#print bnc_str
	
	return 0

if __name__ == '__main__':
	main()

