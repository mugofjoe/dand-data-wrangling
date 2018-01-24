#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Preparing for Database - SQL

After auditing is complete the next step is to prepare the data 
to be inserted into a SQL database.

To do so you will parse the elements in the OSM XML file, 
transforming them from document format to tabular format,
 thus making it possible to write to .csv files.  
 These csv files can then easily be imported to a 
 SQL database as tables.

 The process for this transformation is as follows:
- Use iterparse to iteratively step through each top level element in the XML
- Shape each element into several data structures using a custom function
- Utilize a schema and validation library to ensure the transformed data is in
  the correct format
- Write each data structure to the appropriate .csv files

We've already provided the code needed to load the data, 
perform iterative parsing and write the output to csv files. 

Your task is to complete the shape_element function that will 
transform each element into the correct format. 

To make this process easier we've already defined a schema (see
the schema.py file in the last code tab) for the .csv files 
and the eventual tables. 

Using the cerberus library we can validate the output
against this schema to ensure it is correct.

## Shape Element Function
The function should take as input an iterparse Element object 
and return a dictionary.

### NODE TAG
### If the element top level tag is "node":

The dictionary returned should have the format {"node": .., "node_tags": ...}

The "node" field should hold a dictionary of the following top level node attributes:
- id
- user
- uid
- version
- lat
- lon
- timestamp
- changeset
- *All other attributes can be ignored

The "node_tags" field should hold a list of dictionaries, one per secondary tag. 

Secondary tags are child tags of node which have the tag name/type: "tag". 

Each dictionary should have the following
fields from the secondary tag attributes:

- id: the top level node id attribute value
- key: the full tag "k" attribute value if no colon is
  present or the characters after the colon if one is.
- value: the tag "v" attribute value
- type: either the characters before the colon in the 
  tag "k" value or "regular" if a colon is not present.

Additionally,

- if the tag "k" value contains problematic characters, the tag should be ignored

- if the tag "k" value contains a ":" the characters before the ":" should be set as the tag type
  and characters after the ":" should be set as the tag key

- if there are additional ":" in the "k" value they should be ignored and kept as part of
  the tag key. For example:

  <tag k="addr:street:name" v="Lincoln"/>
  should be turned into
  {'id': 12345, 'key': 'street:name', 'value': 'Lincoln', 'type': 'addr'}

- If a node has no secondary tags then the "node_tags" 
  field should just contain an empty list.

The final return value for a "node" element should look something like:

{'node': {'id': 757860928,
          'user': 'uboot',
          'uid': 26299,
          'version': '2',
          'lat': 41.9747374,
          'lon': -87.6920102,
          'timestamp': '2010-07-22T16:16:51Z',
          'changeset': 5288876},
          'node_tags': [{'id': 757860928,
                            'key': 'amenity',
                            'value': 'fast_food',
                            'type': 'regular'},
                        {'id': 757860928,
                            'key': 'cuisine',
                            'value': 'sausage',
                            'type': 'regular'},
                        {'id': 757860928,
                            'key': 'name',
                            'value': "Shelly's Tasty Freeze",
                            'type': 'regular'}
                        ]
          }


### WAY TAG
### If the element top level tag is "way":

The dictionary should have the format {"way": ..., "way_tags": ..., "way_nodes": ...}

The "way" field should hold a dictionary of the following top level way attributes:
- id
-  user
- uid
- version
- timestamp
- changeset
- *All other attributes can be ignored

The "way_tags" field should again hold a list of dictionaries, following the exact same rules as
for "node_tags".

Additionally, the dictionary should have a field "way_nodes". 

"way_nodes" should hold a list of
dictionaries, one for each nd child tag. 

Each dictionary should have the fields:

- id: the top level element (way) id
- node_id: the ref attribute value of the nd tag
- position: the index starting at 0 of the nd tag i.e. what order the nd tag appears within
            the way element

The final return value for a "way" element should look something like:

{'way': {'id': 209809850,
         'user': 'chicago-buildings',
         'uid': 674454,
         'version': '1',
         'timestamp': '2013-03-13T15:58:04Z',
         'changeset': 15353317},
 'way_nodes': [{'id': 209809850, 'node_id': 2199822281, 'position': 0},
               {'id': 209809850, 'node_id': 2199822390, 'position': 1},
               {'id': 209809850, 'node_id': 2199822392, 'position': 2},
               {'id': 209809850, 'node_id': 2199822369, 'position': 3},
               {'id': 209809850, 'node_id': 2199822370, 'position': 4},
               {'id': 209809850, 'node_id': 2199822284, 'position': 5},
               {'id': 209809850, 'node_id': 2199822281, 'position': 6}],
 'way_tags': [{'id': 209809850,
               'key': 'housenumber',
               'type': 'addr',
               'value': '1412'},
              {'id': 209809850,
               'key': 'street',
               'type': 'addr',
               'value': 'West Lexington St.'},
              {'id': 209809850,
               'key': 'street:name',
               'type': 'addr',
               'value': 'Lexington'},
              {'id': '209809850',
               'key': 'street:prefix',
               'type': 'addr',
               'value': 'West'},
              {'id': 209809850,
               'key': 'street:type',
               'type': 'addr',
               'value': 'Street'},
              {'id': 209809850,
               'key': 'building',
               'type': 'regular',
               'value': 'yes'},
              {'id': 209809850,
               'key': 'levels',
               'type': 'building',
               'value': '1'},
              {'id': 209809850,
               'key': 'building_id',
               'type': 'chicago',
               'value': '366409'}]}

"""
import cerberus
import csv
import codecs  # standard python endcoder/decoder
import pprint
import re
import schema
import xml.etree.cElementTree as ET

OSM_PATH = "example_11.osm"

NODES_PATH = "nodes.csv"
NODE_TAGS_PATH = "nodes_tags.csv"
WAYS_PATH = "ways.csv"
WAY_NODES_PATH = "ways_nodes.csv"
WAY_TAGS_PATH = "ways_tags.csv"

SCHEMA = schema.schema

# Make sure the fields order in the csvs matches the column order in the sql table schema
NODE_FIELDS = ['id', 'lat', 'lon', 'user', 'uid', 'version', 'changeset', 'timestamp']
NODE_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_FIELDS = ['id', 'user', 'uid', 'version', 'changeset', 'timestamp']
WAY_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_NODES_FIELDS = ['id', 'node_id', 'position']

# ================================================== #
#               Main Function                        #
# ================================================== #
def process_map(file_in, validate):
    """
    Iteratively process each XML element and write to csv(s)
    """  

    # opens the files for writing
    with codecs.open(NODES_PATH, 'w') as nodes_file, \
         codecs.open(NODE_TAGS_PATH, 'w') as nodes_tags_file, \
         codecs.open(WAYS_PATH, 'w') as ways_file, \
         codecs.open(WAY_NODES_PATH, 'w') as way_nodes_file, \
         codecs.open(WAY_TAGS_PATH, 'w') as way_tags_file:


if __name__ == '__main__':
    # Note: Validation is ~ 10X slower. For the project consider using a small
    # sample of the map when validating.
    process_map(OSM_PATH, validate=True)