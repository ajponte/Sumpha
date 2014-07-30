""" Methods for getting event data
    from www.Eventbrite.com 
    and www.Meetup.com
    @author Alan Ponte
"""

from __future__ import print_function
from pprint import pprint
import xml.etree.ElementTree as ET
import urllib2

def getEventBriteData(city, query, appKey):
    """ Returns a dict of data from a 
        RESTful API request to www.eventbrite.com
        using the CITY and the QUERY.
    """
    url = "https://www.eventbrite.com/xml/event_search?app_key=" + appKey + "&keywords=" + query+"&city=" + city +"&date=This+month"
    foo = "https://www.eventbrite.com/xml/event_search?app_key=DYVEWBELHOJDXT7VPS&keywords=jazz+music&rap&city=San+Francisco&date=This+month"
    data = urllib2.urlopen(url).read()
    root = ET.fromstring(data)
    description = ""
    descriptions = []
    titles = []
    title = ""
    url = ""
    eventData = []
    eventDataMap = {}
    for child in root:
        try:
            description = child.find("description").text
            url = child.find("url").text
            title = child.find("title").text
            errorMessage = child.find("error_message")
            errorType = child.find("error_type")
            errorMap = {
            errorMessage: errorType
            }
            eventDataMap = {
                            'title': title,
                            'description': description,
                            'url': url,
                            'error': errorMap
                            }
            eventData.append(eventDataMap)
        except AttributeError:
            print("cant find description tag")
        #print(description)
    return eventData

