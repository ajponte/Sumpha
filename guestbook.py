
''' Controller for the Sumpha App. 
    Renders and serves index.html.
    Passes JSON data to the html, for 
    displaying the results.

    @author Alan Ponte 
'''

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


from getData import MeetupCollector, EventBriteCollector
from utils import getRandom, printLines, createMeetupCollector, createEventBriteCollector, numEvents, replaceSpaces

""" Main Controller.  Resposible for rendering the main HTML and passing
    event information to the page.
    @author Alan POnte
"""

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

API_KEY = "2a1375761e5858197f2c1d546f417342"
TEST_QUERY = "http://api.meetup.com/2/open_events?status=upcoming&radius=25.0&state=ca&and_text=False&limited_events=False&text=jazz+music&desc=False&city=san+francisco&offset=0&photo-host=public&format=json&page=20&country=us&sig_id=14329201&sig=e31eef1653769211053be6849d5285b63f0593f6"
jsonResults = None

# [START main_page]
class MainPage(webapp2.RequestHandler):

    def get(self):
        data = requests.get(TEST_QUERY).text
        jsonData = json.json.loads(data)
        template = JINJA_ENVIRONMENT.get_template('index.html', {})

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
        data = requests.get(TEST_QUERY).text
        jsonData = json.json.loads(data)
        template = JINJA_ENVIRONMENT.get_template('showEvents.html', {})

        query = cgi.escape(self.request.get('query'))
        #query = str(replaceSpaces(query))
        #eventBriteCllctr = createEventBriteCollector("san+francisco", "ca", "jazz+music")
        meetupCllctr = createMeetupCollector("san+francisco", "ca", query)


        #numberEvents = numEvents(meetupCllctr.numEvents, eventBriteCllctr.numEvents)
        ranNum = getRandom(10)
        eventName1 = meetupCllctr.getEventName(ranNum)
        description1 = meetupCllctr.getDescription(ranNum)
        url1 = meetupCllctr.getEventURL(ranNum)

        ranNumPrime = getRandom(10)
        eventName2 = meetupCllctr.getEventName(ranNumPrime)
        description2 = meetupCllctr.getDescription(ranNumPrime)
        url2 = meetupCllctr.getEventURL(ranNumPrime)

        ranNumPrimePrime = getRandom(10)
        eventName3 = meetupCllctr.getEventName(ranNumPrimePrime)
        description3 = meetupCllctr.getDescription(ranNumPrimePrime)
        url3 = meetupCllctr.getEventURL(ranNumPrimePrime)

        template_values = {
        'jsonResults': jsonData,
        'printLines': printLines,
        'randomNum': getRandom,
        'query': query,
        'eventName1':eventName1,
        'description1': description1,
        'eventName2': eventName2,
        'description2': description2,
        'eventName3': eventName3,
        'description3': description3,
        'url1': url1,
        'url2': url2,
        'url3': url3
        }

        self.response.write(template.render(template_values))


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', ShowEvents),
   
], debug=True)