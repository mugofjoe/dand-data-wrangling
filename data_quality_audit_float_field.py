import csv
import pprint
import numpy as np
import os

fieldname = "wgs84_pos#lat"
minval = -90
maxval = 90

OSM_FILE = ""
SAMPLE_FILE = ""
COMPUTER_NAME = os.environ['COMPUTERNAME']
if COMPUTER_NAME == "MELLOYELLO":
    OSM_FILE = ""
    SAMPLE_FILE = "D:/Repos/data-wrangling-street-type/sample_chicago.osm"
elif COMPUTER_NAME == "JDAZO":
    OSM_FILE = "E:/Repos/data-wrangling-street-type/sample_chicago.osm"


def skip_lines(input_file, skip):
    for i in range(0, skip):
        next(input_file)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_array(data):
    isinstance(data, (list, tuple, np.ndarray))


def audit_float_field(v, counts):
    v = v.strip()
    if v == "NULL":
        counts['nulls'] += 1
    elif v == "":
        counts['empties'] += 1
    elif is_array(v):
        counts['arrays'] += 1
    elif not is_number(v):
        print "Found non number:", v
    else:
        v = float(v)
        if not ((minval < v) and (v < maxval)):
            print "Found out of range value:", v


if __name__ == "__main__":
    input_file = csv.DictReader(open("cities3.csv"))
    skip_lines(input_file, 3)
    counts = {"nulls": 0, "empties": 0, "arrays": 0}
    nrows = 0
    for row in input_file:
        audit_float_field(row[fieldname], counts)
        nrows += 1

    print "num cities:", nrows
    print "nulls:", counts['nulls']
    print "empties:", counts['empties']
    print "arrays:", counts['arrays']
