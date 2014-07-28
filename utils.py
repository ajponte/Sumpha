import random
import math
import re

from getData import MeetupCollector, EventBriteCollector

""" Utilities for JSON data manipulation
    @author Alan Ponte
"""

def numEvents(meetupCllctr, eventBriteCllctr):
	""" Returns the maximum number of events from MEETUPCLLCTR
	    or EVENTBRITECLLCTR, whichever is higher.
	"""
	return max(meetupCllctr.numEvents, eventBriteCllctr.numEvents)

def getRandom(maximum):
	""" Returns a random integer X, such that
		1 <= X <= MAXIMUM
	"""
 	return int(math.floor(random.random() * maximum))


def createMeetupCollector(city, state, query):
	""" Creates and returns a new MeetupCollector, which will
	    use CITY, STATE, and QUERY, to get event information
	    in JSON format.
	"""
	mc = MeetupCollector.MeetupCollector(city, state, query)
	return mc

def createEventBriteCollector(city, state, query):
	""" Creates and returns a new EVENTBRITECOLLECTOR, which will
	    use CITY, STATE, and QUERY to get event informatio in
	    JSON format.
	""" 
	ec = EventBriteCollector.EventBriteCollector(city, state, query)
	return ec

def main():
	mc = MeetupCollector.MeetupCollector("san+francisco", "ca", "jazz+music")
	ec = EventBriteCollector.EventBriteCollector("san+francisco", "ca", "jazz+music")
	nEvents = numEvents(mc, ec)
	print nEvents

	print(getRandom(nEvents))



def printLines(textInput):
            """ Returns the first 140 characters of textInput.
                If textInput exceeds 140 characters, cut off at the nearest 'whole word'
                and insert a '...' at the end of the string.
            """
            numChars = 0
            strBuilder = ""

            textInput = re.sub('<[^>]*>', '', textInput)

            """ for each word in textInput, count the number of characters.
                If the number of characters exceeds 140, then return to the nearest 'whole word.'
            """
            for word in textInput.split():
                numChars += len( word )
                numChars += 1 # adds 1 for space between words 
                if numChars <= 140:
                    strBuilder += word 
                    strBuilder += ' '
                else:
                    return strBuilder
            return strBuilder + '...'

if __name__ == "__main__":
	main()

