'''
 A Collector for meetup.com
 Created on Jul 19, 2014

 @author: aponte
'''

import json
import requests

class MeetupCollector():
    
    def __init__(self, city, state, query):
        """ Returns the JSON from querying the API
           for CITY, STATE, and the QUERY.
        """
        self.city = city
        self.state = state
        self.query = query
        self.url = self.createURL()
        
    def getJSON(self):
        """ Returns the JSON representation of the 
            API call.
        """
        data = requests.get(self.url).text
        data = json.loads(data)
        return data
    
    def createURL(self):
        """ Builds and returns the URL based on the search parameters. """
        
        url = "http://api.meetup.com/2/open_events?status=upcoming&radius=25.0&state=" + self.state + "&and_text=False&limited_events=False&text=" + self.query + "&desc=False&city=" + self.city + "&offset=0&photo-host=public&format=json&page=20&country=us&sig_id=14329201&sig=e31eef1653769211053be6849d5285b63f0593f6"
        return url
    
    def getURL(self):
        """ Returns THIS URL. """
        return self.url
        
      
        