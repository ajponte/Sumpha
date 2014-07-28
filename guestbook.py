
# [START imports]
import math
import random
import re

import os
import urllib
import cgi

from google.appengine.api import users
from google.appengine.ext import ndb
from webapp2_extras import json

import jinja2
import webapp2
import requests
import EventBriteCollector


from getData import MeetupCollector
from utils import getRandom, printLines
import MeetupCollector

""" Main Controller.  Resposible for rendering the main HTML and passing
    event information to the page.
    @author Alan POnte
"""

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

TEST_QUERY = "http://api.meetup.com/2/open_events?status=upcoming&radius=25.0&state=ca&and_text=False&limited_events=False&text=jazz+music&desc=False&city=san+francisco&offset=0&photo-host=public&format=json&page=20&country=us&sig_id=14329201&sig=e31eef1653769211053be6849d5285b63f0593f6"
jsonResults = None

# [START main_page]
class MainPage(webapp2.RequestHandler):

    def get(self):
        data = requests.get(TEST_QUERY).text
        jsonData = json.json.loads(data)
        template = JINJA_ENVIRONMENT.get_template('index.html', {})

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

        def getRandom():
            """ Returns a random integer X, such that
                1 <= X <= 10
            """
            return math.floor(random.random() * 13)

        template_values = {
        'jsonResults': jsonData,
        'printLines': printLines,
        'randomNum': getRandom,
        }
        self.response.write(template.render(template_values))

# [END main_page]


class ShowEvents(webapp2.RequestHandler):
    """ Class for displaying the events to the user. """
    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each Greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.

        self.redirect('/')

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/', ShowEvents),
   
], debug=True)
