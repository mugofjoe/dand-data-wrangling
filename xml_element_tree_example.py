#%%
import xml.etree.ElementTree as ET
import pprint

# with ElementTree we can parse data in couple of ways
# parse it by filename
# use from string method of the ElementTree module
# to parse XML stored as a string value in our program

# As we think about parsing XML using element trees
# it makes sense to work with Document-oriented XML data

tree = ET.parse('E:/Google Drive/Backpack/Udacity DAND/04 Data Wrangling/exampleResearchArticle.xml')
root = tree.getroot()

"""
print "Children of root:"
for child in root:
    # print "Type of child: {}".format(type(child))
    print child.tag  # print out the tag name of each element
"""

title = root.find('./fm/bibl/title')  # this is an XPath expression
title_text = ""
for p in title:
    title_text += p.text
    


print("\nTitle:\n {}".format(title_text))


# return all elements that match the XPath expression
print "\nAuthor email addresses:"
for a in root.findall('./fm/bibl/aug/au'):
    email = a.find('email')
    if email is not None:
        print email.text
