#!/usr/bin/python
#
# Developed by Hen's Teeth Network for the PDG Commerce Community
#
# This work is licensed under the Creative Commons Attribution-ShareAlike 3.0 
# Unported License. To view a copy of this license, visit 
# http://creativecommons.org/licenses/by-sa/3.0/ 
# or send a letter to Creative Commons, 444 Castro Street, Suite 900, 
# Mountain View, California, 94041, USA.
#
# The code to iterate over and replace text in files -- primarily the code to 
# create and use temp files -- is from Thomas Watnedal's answer to the following
# Stack Overflow question, which is also licensed under a Creative Commons
# Attribution-ShareAlike license.
# http://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python
# -*- coding:utf-8 -*-
#
# clean_prod_text.py
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Clean Product Text -- a Python script to remove special characters,
# commonly added when pasting text from a MS Word document, into a
# product's Specific Product Text using PDG Administrator
#
# usage: install in your web server's cgi-bin folder. Make sure the script's 
# permissions are correct for your installation. You can then run the script 
# from the URL, from the command line or from a cron script.
#
# The script assumes that your product text files are in the standard 
# location: cgi-bin/PDG_Commerce/ProdText/
#
# From the URL: http://domain.com/cgi-bin/clean_prod_text.py
# From the command line: python clean_prod_text.py
# From cron: wget http://domain.com/cgi-bin/clean_prod_text.py
#
# Running the script will remove special characters from the text files
# and replace them with whitespace. You may edit the script to replace
# carriage returns and other special characters, 
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# http://stackoverflow.com/users/4059/thomas-watnedal
#
# Version 1.0 - October 2011
#


import os
import re
import sys
from tempfile import mkstemp
from shutil import move
from os import remove, close

def cleanText(text):
	# Replace non-ASCII characters with printable ASCII. 
	# Use HTML entities when possible
	if None == text:
		return ''


	text = re.sub(r'\x85', '...', text) # replace ellipses
	text = re.sub(r'\x91', "'", text)  # replace left single quote
	text = re.sub(r'\x92', "'", text)  # replace right single quote
	text = re.sub(r'\x93', '"', text)  # replace left double quote
	text = re.sub(r'\x94', '"', text)  # replace right double quote
	text = re.sub(r'\x95', '*', text)   # replace bullet
	text = re.sub(r'\x96', '-', text)        # replace bullet
	text = re.sub(r'\x99', "'", text)  # replace TM
	text = re.sub(r'\xae', '(r)', text)    # replace (R)
	text = re.sub(r'\xb0', '', text)    # replace degree symbol
	text = re.sub(r'\xba', '', text)    # replace degree symbol

	# Do you want to keep new lines / carriage returns? These are generally 
	# okay and useful for readability
	text = re.sub(r'[\n\r]+', ' ', text)     # remove embedded \n and \r

	# This is a hard-core line that strips everything else.
	text = re.sub(r'[\x00-\x1f\x80-\xff]', '', text)

	return text


print("Content-type: text/plain");
print("");
print("clean_prod_text");

prod_text_path = '/home/simon/workspace/'
listing = os.listdir(prod_text_path + 'input/')

for infile in listing:

	print "current file is: " + infile

	#Create temp file
	fh, tmp_path = mkstemp()
	new_file = open(tmp_path,'w')
	old_file = open(prod_text_path + 'input/' + infile)

	for line in old_file:
		new_file.write(cleanText(line))


	#close temp file
	new_file.close()
	close(fh)
	old_file.close()

	#Remove original file
	#remove(prod_text_path + infile)

	#Move new file
	move(tmp_path, prod_text_path + 'cleaned/' + infile)



