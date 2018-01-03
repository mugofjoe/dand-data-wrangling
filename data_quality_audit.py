#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import xml.etree.cElementTree as ET
from collections import defaultdict
import re

OSM_FILE = ""
COMPUTER_NAME = os.environ['COMPUTERNAME']

if COMPUTER_NAME == "MELLOYELLO":
    OSM_FILE = ""
    SAMPLE_FILE = ""
elif COMPUTER_NAME == "JDAZO":
    OSM_FILE = "E:/Repos/data-wrangling-street-type/sample_chicago.osm"

osm_file = open(OSM_FILE, "r")

street_type_re = re.compile(r'\S+\.?$', re.IGNORECASE)
street_types = defaultdict(int)

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()

        street_types[street_type] += 1

def print_sorted_dict(d):
    keys = d.keys()
    keys = sorted(keys, key=lambda s: s.lower())
    for k in keys:
        v = d[k]
        print "%s: %d" % (k, v) 

def is_street_name(elem):
    return (elem.tag == "tag") and (elem.attrib['k'] == "addr:street")

def audit():
    for event, elem in ET.iterparse(osm_file):
        if is_street_name(elem):
            audit_street_type(street_types, elem.attrib['v'])    
    print_sorted_dict(street_types)    

if __name__ == '__main__':
    audit()

    
# Full chicago.osm: http://osm-extracted-metros.s3.amazonaws.com/chicago.osm.bz2
# Full cities file: http://content.udacity-data.com/ud032/infobox/cities.csv.zip
