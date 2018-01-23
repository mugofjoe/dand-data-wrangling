"""
Parse a csv file and return a list of dictionary items.
Each list row-item contains a dictionary-ed version of each CSV record.
"""

import os
import pprint
import csv

DATADIR = ""
DATAFILE = "specimen1.csv"


def parse_file(datafile):
    '''
        Create a list of dictionaries
        Only process 10 rows
    '''
    data = []
    with open(datafile, "rb") as f:
        header = f.readline().split(",")
        counter = 0
        for line in f:
            if counter == 10:
                break

            fields = line.split(",")
            entry = {}

            for i, value in enumerate(fields):
                entry[header[i].strip()] = value.strip()

            data.append(entry)
            counter += 1

    return data


def parse_csv(datafile):
    '''
        Use the csv module
    '''
    data = []
    n = 0
    with open(datafile, 'rb') as sd:
        r = csv.DictReader(sd)
        for line in r:
            data.append(line)
    return data


def test():
    # a simple test of your implementation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    # firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1',
    #              'Label': 'Parlophone(UK)', 'Released': '22 March 1963',
    #              'US Chart Position': '-', 'RIAA Certification': 'Platinum',
    #              'BPI Certification': 'Gold'}
    # tenthline = {'Title': '', 'UK Chart Position': '1',
    #              'Label': 'Parlophone(UK)', 'Released': '10 July 1964',
    #              'US Chart Position': '-', 'RIAA Certification': '',
    #              'BPI Certification': 'Gold'}

    # assert d[0] == firstline
    # assert d[9] == tenthline


# test()


if __name__ == '__main__':
    datafile = os.path.join(DATADIR, DATAFILE)
    parse_csv(datafile)
    d = parse_csv(datafile)
    pprint.pprint(d)



'''

import os
cwd = os.getcwd()
print(cwd)

DATADIR = ""
DATAFILE = "beatles-discography.csv"

datafile = os.path.join(DATADIR, DATAFILE)

with open(datafile, "rb") as f:
    header = True
    for line in f:
        if header:
            header = False
            continue

        dict1 = {'Title': '',
                 'Released': '',
                 'Label': '',
                 'UK Chart Position': '',
                 'US Chart Position': '',
                 'BPI Certification': '',
                 'RIAA Certification': ''}

        dict1['Title'] = line.split(',')[0]
        dict1['Released'] = line.split(',')[1]
        dict1['Label'] = line.split(',')[2]
        dict1['UK Chart Position'] = line.split(',')[3]
        dict1['US Chart Position'] = line.split(',')[4]
        dict1['BPI Certification'] = line.split(',')[5]
        dict1['RIAA Certification'] = line.split(',')[6]

        print(dict1)
        # print(line.split(',')[1])



'''