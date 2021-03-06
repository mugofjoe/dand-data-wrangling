#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TOPIC: Iterative Parsing
How many of each distinct top-level tags are there in an XML file?

Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
Fill out the count_tags function. It should return a dictionary with the 
tag name as the key and number of times this tag can be encountered in 
the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
#%%
import xml.etree.cElementTree as ET
import pprint

def count_tags(filename):

        # YOUR CODE HERE
        tags_dict = {}  # initialize an empty dictionary

        # SAX parsing of the file
        for event, elem in ET.iterparse(filename):
            if elem.tag not in tags_dict:
                tags_dict[elem.tag] = 1
            else:
                tags_dict[elem.tag] += 1

        return tags_dict



def test():

    tags = count_tags('conroy_oakridge.osm')
    pprint.pprint(tags)
    # assert tags == {'bounds': 1,
    #                  'member': 3,
    #                  'nd': 4,
    #                  'node': 20,
    #                  'osm': 1,
    #                  'relation': 1,
    #                  'tag': 7,
    #                  'way': 1}


if __name__ == "__main__":
    test()