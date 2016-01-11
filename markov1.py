from pymarkovchain import MarkovChain

import os
#import sys
from os import remove, close
import re

mc = MarkovChain("./markov")

#get files
prod_text_path = '/home/simon/workspace/'
listing = os.listdir(prod_text_path + 'cleaned/')
string = ""
for infile in listing:

	#print ("current file is: " + infile)
	f = open(prod_text_path + 'cleaned/' + infile)
	string += str(f.read())	
	f.close()

mc.generateDatabase(string)

f = open('/home/simon/workspace/keywords.txt')
kw = f.read().split("\n")
f.close()

#tries = 0

def sayLine():
	i=1000
	while (i >= 0):
		#tries += 1
		out = mc.generateString()
		#output.write("TESTING: " + out+"\n")
		if(len(out) > 67):
			#output.write("ERROR: too long\n")
			continue
		
		if(checkLine(out)):
			output.write(out + "\n")
		
		else:
			#output.write("ERROR: no interesting name present\n")
			continue
		
		
		i -=1
		
def checkLine(line):
	goodline = False
	for key in kw:
		regex = re.compile("\W"+ key + "\W")
		if(bool(regex.search(str(line)))):
			goodline = True
	return goodline
	
output = open('/home/simon/workspace/markov_experiment/output.txt', 'w')		
sayLine()
output.close()
print ("output complete")
