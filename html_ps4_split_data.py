#!/usr/bin/env python
# -*- coding: utf-8 -*-
# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# so that you can process the resulting files as valid XML documents.
#
# hint: http://stackoverflow.com/questions/12717294/split-one-file-into-multiple-files-based-on-pattern-cut-can-occur-within-lines

import os
import xml.etree.ElementTree as ET


PATENTS = ""
COMPUTER_NAME = os.environ['COMPUTERNAME']

if COMPUTER_NAME == "MELLOYELLO":
    PATENTS = "D:/Google Drive/Backpack/Udacity DAND/04 Data Wrangling/patent.data"


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


# a generator for the file to be written to
def outfile_generator(filename):
    n = -1
    while True:
        n += 1
        yield open('{0}-{1}'.format(filename, n), 'w')


def split_file(filename):
    """
    Split the input file into separate files, each containing a single patent.
    As a hint - each patent declaration starts with the same line that was
    causing the error found in the previous exercises.

    The new files should be saved with filename in the following format:
    "{}-{}".format(filename, n) where n is a counter, starting from 0.
    """
    # the pattern on which the file is split
    pat = "<?xml"

    # an iterator for the filename
    outfile_iterator = outfile_generator(filename)
    pass


def test():
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print "You have not split the file {} in the correct boundary!".format(fname)
            f.close()
        except:
            print "Could not find file {}. Check if the filename is correct!".format(fname)


test()
