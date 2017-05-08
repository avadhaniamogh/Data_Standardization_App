import utm, csv, operator
import re
import sys
import pandas as pd
from itertools import *
import ast
import Utils
import os

csv.field_size_limit(sys.maxsize)

# csvfile = r'/home/amogh/Desktop/OpenAddresses_Data/ny/Clean_version/city_of_new_york.csv'
# manipulatedcsv = r'/home/amogh/Desktop/OpenAddresses_Data/ny/Cleaner_version/city_of_new_york.csv'


def addRowNumbers(path, file):
    csvfile = path + file
    # print csvfile

    if not os.path.exists(Utils.PATH + "/tmp"):
        os.makedirs(Utils.PATH + "/tmp")

    if not os.path.exists(Utils.PATH + "/tmp" + "/add_row_num"):
        os.makedirs(Utils.PATH + "/tmp" + "/add_row_num")

    return_manipulatedcsv = Utils.PATH + "tmp" + "/add_row_num/"

    manipulatedcsv = Utils.PATH + "tmp" + "/add_row_num" + "/" + file
    with open(csvfile, 'rb') as input, open(manipulatedcsv, 'wb') as output:
        reader = csv.reader(input, delimiter=',')
        writer = csv.writer(output, delimiter=',')

        all = []
        row = next(reader)
        row.insert(0, 'RowId')
        all.append(row)
        for k, row in enumerate(reader):
            all.append([str(k + 1)] + row)
        writer.writerows(all)

    return return_manipulatedcsv

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def sortRowsOnStreetName(path, file):
    csvfile = path + file
    # print csvfile

    if not os.path.exists(Utils.PATH + "/tmp"):
        os.makedirs(Utils.PATH + "/tmp")

    if not os.path.exists(Utils.PATH + "/tmp" + "/sort_street_names"):
        os.makedirs(Utils.PATH + "/tmp" + "/sort_street_names")

    return_manipulatedcsv = Utils.PATH + "tmp" + "/sort_street_names/"

    manipulatedcsv = Utils.PATH + "tmp" + "/sort_street_names" + "/" + file
    sortable_dict = {}
    rows = []
    with open(csvfile) as f:
        reader = csv.reader(f)
        header = next(reader)
        index_street_name = header.index(Utils.street_column)
        index_row_num = header.index("RowId")

        for row in reader:

            rows.append(row)

            street_name = row[index_street_name]
            row_num = row[index_row_num]
            isit = is_number(street_name)
            if(isit):
                street_name = int(street_name)

            sortable_dict[row_num] = street_name

    f.close()

    sorted_dict = sorted(sortable_dict.iteritems(), key=lambda (k, v): (v, k))

    with open(csvfile) as f:
        reader = csv.reader(f)
        header = next(reader)

        with open(manipulatedcsv, "a") as fp:
            # Write headers
            writer = csv.DictWriter(fp, fieldnames=header)
            writer.writeheader()

        fp.close()
    f.close()

    with open(manipulatedcsv, "r+a") as fp:
        manipulated_file_reader = csv.reader(fp)
        manipulated_file_header = next(manipulated_file_reader)
        # Now data
        counter = 0

        new_row = [None] * len(manipulated_file_header)
        for key, value in sorted_dict:
            key = int(key)
            new_row = rows[key - 1]
            wr = csv.writer(fp, dialect='excel')
            wr.writerow(new_row)

    fp.close()

    return return_manipulatedcsv

# sortRowsOnStreetName(csvfile, manipulatedcsv)
# print cursor