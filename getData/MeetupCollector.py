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
        self.resourceURL = self.createResourceURL()
        self.JSONdata = self.getJSON()
        
    def getJSON(self):
        """ Returns the JSON representation of the 
            API call.
        """
        data = requests.get(self.resourceURL).text
        data = json.loads(data)
        return data
    
    def createResourceURL(self):
        """ Builds and returns the URL based on the search parameters. """
        
        url = "http://api.meetup.com/2/open_events?status=upcoming&radius=25.0&state=" + self.state + "&and_text=False&limited_events=False&text=" + self.query + "&desc=False&city=" + self.city + "&offset=0&photo-host=public&format=json&page=20&country=us&sig_id=14329201&sig=e31eef1653769211053be6849d5285b63f0593f6"
        return url
    
    def getURL(self):
        """ Returns THIS URL. """
        return self.resourceURL
    
    def getJSONdata(self):
        """ Returns the String representation of the JSON data. """
        return self.JSONdata
    
    def getDescription(self, eventNum):
        """ Returns the descripton for the event indicated by EVENTNUM. """
        if self.numEvents < eventNum:
            raise IndexError("No event numbered " + eventNum)
        else:
            return self.JSONdata['results'][eventNum]['description']
    
    def getEventURL(self, eventNum):
        """ Returns the Event's URL for the Event indicated by EVENTNUM. """
        if self.numEvents < eventNum:
            raise IndexError("No event numbered " + eventNum)
        else:
            return self.JSONdata['results'][eventNum]['event_url']
    
    def getEventURLs(self):
        """ Returns a list of all event URLs. """
        urls = []
        for i in range(0, self.numEvents + 1):
            urls.append(self.getEventURL(i))
        return urls
    
    def getEventName(self, eventNum):
        """ Returns the Event name for the Event indicated by EVENTNUM. """
        if self.numEvents < eventNum:
            raise IndexError("No event numbered " + eventNum)
        else:
            return self.JSONdata['results'][eventNum]['name']
        
    def getEventNames(self):
        """ Returns a list of all the Event names collected 
            by THIS MeetupCollector. """
        names = []
        for i in range(0, self.numEvents + 1):
            names.append(self.getEventName(i))
        return names
    
    @property
    def numEvents(self):
        """ Returns the number of Events returned by a call to the API. """
        return len(self.JSONdata['results'])
        
    
    
        
      
        