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
All other attributes can be ignored

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

"""