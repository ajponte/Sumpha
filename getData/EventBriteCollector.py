'''
 A Collector for gathering JSON data from the RESTful
 API from Eventbrite.com
 Created on Jul 19, 2014

 @author: aponte
'''

import requests
import json
import Defaults
class EventBriteCollector():
    def __init__(self, city, state, query):
        self.city = city
        self.state = state
        self.query = query
        self.jsonData = self.getJSON()
        self.OAuthToken = "RNNTBCERPT2RRYLC5C3U"

    def setOauthToken(self, token):
        """ Sets the API's Oath token to TOKEN."""
        self.OAuthToken = token

    @property
    def OauthToken(self):
        return self.OAuthToken

    def getResourceURL(self):
        """ Returns the Resource URL used to prompt the REST API for JSON data. """
        url = "https://www.eventbriteapi.com/v3/events/search/?q=" + self.query+ "&venue.city=" + self.city + "&token=" + Defaults.Defaults["EventBriteOAuthToken"]
        return url
    
    def getJSON(self):
        jsonData = requests.get(self.getResourceURL()).text
        data = json.loads(jsonData) 
        return data
    
    def getData(self, key):
        """ Returns the JSON data associated with the KEY. """
        return self.jsonData[key]
    
    def getJSONdata(self):
        """ Returns THIS EventBriteCollector's JSON String. """
        return self.jsonData

    def getKeys(self): 
        """ Returns the Keys of the JSON String for 
            THIS EventBRiteCollector. """
        return self.jsonData.keys()

    def getEventURL(self, eventNum):
        """ Returns the URL for the event indicated by EVENTNUM. """
        assert eventNum > self.numEvents, "There is no event numbered " + eventNum
        return self.jsonData['events'][eventNum]['url']
    
    def getEventURLs(self):
        """ Returns a list of all the URLs for all events. """
        urls = []
        for i in range(0, self.numEvents + 1):
            urls.append(self.jsonData['events'][i]['url'])
        return urls
    
    def getEventDescription(self, eventNum): 
        """ Returns the description for the event indicated by EVENTNUM."""
        assert eventNum > self.numEvents, "There is no event %r " % eventNum
        return self.jsonData['events'][eventNum]['description']
        
    def getEventName(self, eventNum):
        """ Returns the name of the Event indicated by EVENTNUM. """
        assert eventNum > self.numEvents, "There is no event %r " % eventNum
        return self.jsonData['events'][eventNum]['name']['text']
        
    def getVenue(self, eventNum):
        """ Returns the Venue of the Event indicated by EVENTNUM. """
        assert eventNum > self.numEvents, "There is no event %r " % eventNum
        return self.jsonData['events'][eventNum]['venue']
    
    def getVenueName(self, eventNum):
        """ Returns the name of the Venue of the event indicated by EVENTNUM. """
        assert eventNum > self.numEvents, "There is no event %r " % eventNum
        return self.getVenue(eventNum)['name']
    
    @property
    def numEvents(self):
        """ Returns the number of events which are returned by a 
            request to the API. """
        return len(self.jsonData['events'])

            
    
        