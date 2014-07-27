<<<<<<< HEAD

=======
# [START imports]
>>>>>>> 8d63f5b16627a5fdfabb56f1c335e573b0e7656d
import math
import random

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
<<<<<<< HEAD

from getData import MeetupCollector
from utils import getRandom, printLines
=======
import MeetupCollector
>>>>>>> 8d63f5b16627a5fdfabb56f1c335e573b0e7656d

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
<<<<<<< HEAD


=======
        def printLines(words, numLines):
            """ Prints the first N lines from the String STR,
                where N = numLines.
            """
            i = 0
            lines = 0
            strBuilder = ""
            for word in words.split():
                if i <= 5:
                    strBuilder += (" " + word)
                elif lines == numLines:
                    break
                else:
                    strBuilder += "\n"
                    numLines += 1
                    i = 0
            return strBuilder
        def getRandom():
            """ Returns a random integer X, such that
                1 <= X <= 10
            """
            return math.floor(random.random() * 10)
>>>>>>> 8d63f5b16627a5fdfabb56f1c335e573b0e7656d

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
