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


"""