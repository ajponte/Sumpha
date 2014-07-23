import random
import math

""" Utilities for JSON data manipulation
    @author Alan Ponte
"""

def getRandom():
	""" Returns a random integer X, such that
		1 <= X <= 10
	"""
 	return math.floor(random.random() * 10)


def printLines(words, numLines, wordsPerLine):
	""" Prints the first N lines from the string 
	    WORDS, where N = NUMLINES.  Each line has
	    a maximum number of words, WORDSPERLINE.
	"""
	i = 0
	lines = 0
	strBuilder = ""
	for word in words:
		if i <= wordsPerLine:
			strBuilder += (" " + word)
		elif lines >= numLines:
			break
		else:
			strBuilder += "\n"
			lines += 1
			i = 0
	return strBuilder

