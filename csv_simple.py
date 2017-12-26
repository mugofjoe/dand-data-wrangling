'''
Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
split each line on "," and then for each line, create a dictionary
where the key is the header title of the field, and the value is the value of that field in the row.
The function parse_file should return a list of dictionaries,
each data line in the file being a single list entry.
Field names and values should not contain extra whitespace, like spaces or newline characters.
You can use the Python string method strip() to remove the extra whitespace.
You have to parse only the first 10 data lines in this exercise,
so the returned list should have 10 entries!
'''

import csv
import os
import itertools


DATADIR = ""
DATAFILE = "beatles-discography.csv"


def parse_file(datafile):
    # create a list
    data = []
    with open(datafile, "r") as f:
        for line in itertools.islice(csv.DictReader(f), 10):
            data.append(line)

    return data


def test():
    # a simple test of your implementation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1',
                 'Label': 'Parlophone(UK)', 'Released': '22 March 1963',
                 'US Chart Position': '-', 'RIAA Certification': 'Platinum',
                 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1',
                 'Label': 'Parlophone(UK)', 'Released': '10 July 1964',
                 'US Chart Position': '-', 'RIAA Certification': '',
                 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline


test()