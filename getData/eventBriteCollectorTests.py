'''
Created on Jul 19, 2014

@author: aponte
'''

from __future__ import print_function
import EventBriteCollector

jsonData = None
def main():
   # ebc = EventBriteCollector.EventBriteCollector("san+francisco", "ca", "jazz+music")
   # print(ebc.getJSON())
   pass
    
if __name__ == "__main__":
    ebc = EventBriteCollector.EventBriteCollector("san+francisco", "ca", "jazz+music")
    jsonData = ebc.getJSON()
    
    main()
    
