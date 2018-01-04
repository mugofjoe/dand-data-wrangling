"""
Parse an Excel spreadsheet. 
Do operations on cells within columns.
"""
import xlrd

datafile = "2013_ERCOT_Hourly_Load_Data.xls"

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0) 

    # sheet_data is a list of lists sheet_data[row][column]
    # 
    sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
    # print(sheet_data[0][:]) # prints the first row, all columns

    cv = sheet.col_values(1, start_rowx=1, end_rowx=None)
    # col_values(column_number, start_row, end_row) returns a list

    maxval = max(cv)
    #print("maxval: {}".format(maxval))
    minval = min(cv)
    #print("minval: {}".format(minval))

    # we add 1 because we will be using this on the original sheet
    # which still has the header in row 0
    maxpos = cv.index(maxval) + 1
    minpos = cv.index(minval) + 1

    # cell_value(row_idx, col_idx)
    maxtime = sheet.cell_value(maxpos, 0) 
    realmaxtime = xlrd.xldate_as_tuple(maxtime, 0)

    mintime = sheet.cell_value(minpos, 0)
    realmintime = xlrd.xldate_as_tuple(mintime, 0)

    data = {
        'maxtime': realmaxtime,
        'maxvalue': maxval,
        'mintime': realmintime,
        'minvalue': minval,
        'avgcoast': sum(cv) / float(len(cv))
    }
    return data

data = parse_file(datafile)
import pprint
pprint.pprint(data)

assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
assert round(data['maxvalue'], 10) == round(18779.02551, 10)
