import csv
import pprint

fieldname = "wgs84_pos#lat"
minval = -90
maxval = 90

def skip_lines(input_file, skip):
    for i in range(0, skip):
        next(input_file)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

