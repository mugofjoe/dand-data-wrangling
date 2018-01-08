import csv
import pprint
from py_matrix_utils import is_array
from composes.matrix.matrix import Matrix

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

def is_array_or_matrix(data):
    return is_array(data) or isinstance(data, Matrix)


def audit_float_field(v, counts):
    v = v.strip()
    if v == "NULL":
        counts['nulls'] += 1
    elif v == "":
        counts['empties'] += 1
    elif is_array_or_matrix(v):
        counts['arrays'] += 1
    elif not is_number(v):
        print "Found non number:", ValueError
    else:
        v = float(v)
        if not ((minval < v) and (v < maxval)):
            print "Found out of range value:", v


if __name__ == "__main__":
    input_file = csv.DictReader(open("cities3.csv"))
    skip_lines(input_file, 3)
    counts = {"nulls": 0, "empties": 0, "arrays":0}
    nrows = 0
    for row in input_file:
        nrows += 1

    print "num cities:", nrows
    print "nulls:", counts['nulls']
    print "empties:", counts['empties']
