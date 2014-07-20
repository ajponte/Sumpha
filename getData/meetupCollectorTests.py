'''
Created on Jul 19, 2014

@author: aponte
'''

from __future__ import print_function
import MeetupCollector

def main():
    print("in main")
    mc = MeetupCollector.MeetupCollector("san+francisco", "ca", "jazz+music")
    print("getting JSON for MC")
    print(mc.getURL())
    print(mc.getJSON())
    
if __name__ == "__main__":
    main()