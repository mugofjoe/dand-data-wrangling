#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
Note: Electric Reliability Council of Texas (ERCOT)

"""
import numpy as np
import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"
zipfile  = "2013-ercot-hourly-load-data"


def open_zip(datafile):
    pass
    # with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
    #     myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
    #sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    ### other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:", 
    # print sheet.nrows
    # print "Type of data in cell (row 3, col 2):", 
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):", 
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):", 
    # print sheet.cell_type(1, 0)
    # exceltime = sheet.cell_value(1, 0)
    # print "Time in Excel format:",
    # print exceltime
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)
    

    # list of Hour_End times
    hour_end_times = sheet.col_values(0, start_rowx=1, end_rowx=None)
    # list of hourly load for the Texas Coast customers
    coast_loads = sheet.col_values(1, start_rowx=1, end_rowx=None)

    # largest value and index in list of hourly load in Texas Coast region
    maxvalue = max(coast_loads)
    index_maxvalue = coast_loads.index(maxvalue) 

    # print("max load using max: {}".format(maxvalue))
    # print("index of max load using max: {}".format(index_maxvalue))
    # print(coast_loads[index_maxvalue])

    # lowest value and index in list of hourly load in Texas Coast region
    minvalue = min(coast_loads)
    index_minvalue = coast_loads.index(minvalue) 

    # print("min load using min: {}".format(minvalue))
    # print("index of min load using min: {}".format(index_minvalue))
    # print(coast_loads[index_minvalue])

    maxtime = xlrd.xldate_as_tuple(hour_end_times[index_maxvalue], 0)
    # print("maxtime: {}".format(maxtime))
    mintime = xlrd.xldate_as_tuple(hour_end_times[index_minvalue], 0)
    # print("mintime: {}".format(mintime))

    # average hourly load in the Coast column
    avgcoast = np.mean(coast_loads)

    
    data = {
            'maxtime': maxtime,
            'maxvalue': maxvalue,
            'mintime': mintime,
            'minvalue': minvalue,
            'avgcoast': avgcoast
    }
    return data


def test():
    open_zip(zipfile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()