'''
 A Collector for gathering JSON data from the RESTful
 API from Eventbrite.com
 Created on Jul 19, 2014

 @author: aponte
'''

import requests

class EventBriteCollector():
    def __init__(self, city, state, query):
        self.city = city
        self.state = state
        self.query = query
        self.url = self.getURL()
        
    def getURL(self):
        url = "https://www.eventbriteapi.com/v3/events/search/?q=" + self.query+ "&venue.city=" + self.city + "&token=RNNTBCERPT2RRYLC5C3U"
        return url
    
    def getJSON(self):
        data = requests.get(self.url).text
        return data
        