#!/usr/bin/env python
"""
TOPIC: Parse a CSV file and extract each row
- The row extracted is cast into a list of lists
- [list for each row][list of column values]

Your task is to process the supplied file and use the csv module to extract data from it.
The data comes from NREL (National Renewable Energy Laboratory) website. Each file
contains information from one meteorological station, in particular - about amount of
solar and wind energy for each hour of day.

Note that the first line of the datafile is neither data entry, nor header. It is a line
describing the data source. You should extract the name of the station from it.

The data should be returned as a list of lists (not dictionaries).
You can use the csv modules "reader" method to get data in such format.
Another useful method is next() - to get the next line from the iterator.
You should only change the parse_file function.
"""

#%%
import csv
import os

DATADIR = ""
DATAFILE = "E:/Google Drive/Backpack/Udacity DAND/04 Data Wrangling/745090.csv"


def parse_file(datafile):
    name = ""
    data = []
    with open(datafile, 'rb') as f:
        # pass
        r = csv.reader(f)  # instantiate a csv.reader object
        firstline = r.next()  # read the first line (returns a list)
        name = firstline[1]  # get the first item in the list
        header = r.next()  # get the next line
        data = [row for row in r]
        # print("foo")

    # Do not change the line below
    return (name, data)


def test():
    datafile = os.path.join(DATADIR, DATAFILE)
    name, data = parse_file(datafile)

    assert name == "MOUNTAIN VIEW MOFFETT FLD NAS"
    assert data[0][1] == "01:00"
    assert data[2][0] == "01/01/2005"
    assert data[2][5] == "2"


if __name__ == "__main__":
    test()


# https://jefflirion.github.io/udacity/Data_Wrangling_with_MongoDB/Problem_Set1.html

# def parse_file(datafile):
#     name = None
#     header = None
#     data = []
#     with open(datafile,'rb') as f:
#         r = csv.reader(f)
#         for line in r:
#             # get the name
#             if not name:
#                 name = line[1]
#                 continue

#             # get the header
#             if not header:
#                 header = line
#                 continue

#             # add the list for the current line to `data`
#             data.append(line)

#     return (name, data)
