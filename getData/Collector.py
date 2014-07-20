'''
Created on Jul 19, 2014

@author: aponte
'''

import json
import requests
class Collector():
    def __init__(self, city, state, query):
        self.city = city
        self.state = state
        self.query = query
