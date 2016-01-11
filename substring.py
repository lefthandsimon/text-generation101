import os
#import sys
from os import remove, close
import re

f = open('/home/simon/workspace/markov_experiment/keywords.txt')
kw = f.read().split("\n")
f.close()
f = open('/home/simon/workspace/markov_experiment/output.txt')
lines = f.read().split("\n")
f.close()

for key in kw:
	regex = re.compile("\W"+ key + "\W")
	for line in lines:
		if bool(regex.search(str(line))):
			print("Success! " + key + " is in " + line)
		#else:
			#print("No match: " + key + " /" + line) 
			


