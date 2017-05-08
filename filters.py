import utm, csv, operator
import re
import sys
import pandas as pd
import os
import Utils
import shutil

csv.field_size_limit(sys.maxsize)

# csvfile = r'/home/amogh/Desktop/OpenAddresses_Data/ny/Clean_version/erie.csv'
# manipulatedcsv = r'/home/amogh/Desktop/OpenAddresses_Data/ny/Cleaner_version/erie.csv'

def toLowerCase(path, file):
    csvfile = path + "input/" + file
    if not os.path.exists(path + "/tmp"):
        os.makedirs(path + "/tmp")

    if not os.path.exists(path + "/tmp" + "/lower_case"):
        os.makedirs(path + "/tmp" + "/lower_case")

    return_manipulatedcsv = path + "tmp" + "/lower_case/"

    manipulatedcsv = path + "tmp" + "/lower_case" + "/" + file

    with open(csvfile) as f:
        reader = csv.reader(f)
        header = next(reader)

        with open(manipulatedcsv, "a") as fp:
            # Write headers
            writer = csv.DictWriter(fp, fieldnames=header)
            writer.writeheader()

        fp.close()
    f.close()

    with open(csvfile) as f:
        reader = csv.reader(f)
        header = next(reader)

        with open(manipulatedcsv, "r+a") as fp:
            manipulated_file_reader = csv.reader(fp)
            manipulated_file_header = next(manipulated_file_reader)
            # Now data
            counter = 0
            for row in reader:

                new_row = []
                for item in row:
                    lower_item = item.lower()
                    new_row.append(lower_item)

                # print row
                # print new_row
                wr = csv.writer(fp, dialect='excel')
                wr.writerow(new_row)

        fp.close()
    f.close()

    return return_manipulatedcsv

def removeRowsHavingNoStreetNames(path, file):
    csvfile = path + file
    # print csvfile

    if not os.path.exists(Utils.PATH + "/tmp"):
        os.makedirs(Utils.PATH + "/tmp")

    if not os.path.exists(Utils.PATH + "/tmp" + "/rows_without_street_names"):
        os.makedirs(Utils.PATH + "/tmp" + "/rows_without_street_names")

    return_manipulatedcsv = Utils.PATH + "tmp" + "/rows_without_street_names/"

    manipulatedcsv = Utils.PATH + "tmp" + "/rows_without_street_names" + "/" + file

    with open(csvfile) as f:
        reader = csv.reader(f)
        header = next(reader)

        with open(manipulatedcsv, "a") as fp:
            # Write headers
            writer = csv.DictWriter(fp, fieldnames=header)
            writer.writeheader()

        fp.close()
    f.close()

    with open(csvfile) as f:
        reader = csv.reader(f)
        header = next(reader)
        index_street_name = header.index(Utils.street_column)

        with open(manipulatedcsv, "r+a") as fp:
            manipulated_file_reader = csv.reader(fp)
            manipulated_file_header = next(manipulated_file_reader)
            # Now data
            counter = 0
            for row in reader:

                street_name = row[index_street_name]

                if(street_name):
                    wr = csv.writer(fp, dialect='excel')
                    wr.writerow(row)


        fp.close()
    f.close()

    return return_manipulatedcsv

def processHouseNumbers(path, file):
    csvfile = path + file
    # print csvfile

    if not os.path.exists(Utils.PATH + "/tmp"):
        os.makedirs(Utils.PATH + "/tmp")

    if not os.path.exists(Utils.PATH + "/tmp" + "/process_house_numbers"):
        os.makedirs(Utils.PATH + "/tmp" + "/process_house_numbers")

    return_manipulatedcsv = Utils.PATH + "tmp" + "/process_house_numbers/"

    manipulatedcsv = Utils.PATH + "tmp" + "/process_house_numbers" + "/" + file
    with open(csvfile) as f:
        reader = csv.reader(f)
        header = next(reader)
        new_header = header
        new_header.append("BASE_NUM")
        new_header.append("BUILD_NUM")

        with open(manipulatedcsv, "a") as fp:
            # Write headers
            writer = csv.DictWriter(fp, fieldnames=new_header)
            writer.writeheader()

        fp.close()
    f.close()

    with open(csvfile) as f:
        reader = csv.reader(f)
        header = next(reader)
        index_street_number = header.index(Utils.house_number_column)

        with open(manipulatedcsv, "r+a") as fp:
            manipulated_file_reader = csv.reader(fp)
            manipulated_file_header = next(manipulated_file_reader)
            mani_index_base_num = manipulated_file_header.index("BASE_NUM")
            mani_index_building_num = manipulated_file_header.index("BUILD_NUM")
            # Now data
            counter = 0
            for row in reader:

                new_row = [None] * len(manipulated_file_header)
                i = 0
                for value in row:
                    new_row[i] = value
                    i = i + 1
                # print new_row

                street_number = row[index_street_number]
                if (street_number):

                    house_numbers = re.split('-|\/|\\|\*', street_number)
                    # print "House numbs
                    # m = re.search(r'[A-Za-z]$', hn[0])
                    # if m is not None:
                    #     print m.group()

                    hn = []
                    if(len(house_numbers) == 4):
                        if(house_numbers[0] == house_numbers[2]):
                            # print house_numbers
                            average = (int(house_numbers[1]) + int(house_numbers[3])) / 2
                            average = int(average)
                            hn.append(house_numbers[0])
                            hn.append(str(average))
                        elif(house_numbers[1] == house_numbers[3]):
                            average = (int(house_numbers[0]) + int(house_numbers[2])) / 2
                            average = int(average)
                            hn.append(str(average))
                            hn.append(house_numbers[1])

                    else:
                        hn = house_numbers

                    # print hn
                    if(len(hn) > 0):
                        building_result = re.sub('[^0-9]', '', hn[0])
                        hn[0] = building_result
                        # print hn[0]
                        if (len(hn) > 1):
                            if (hn[1]):
                                base_result = re.sub('[^0-9]', '', hn[1])
                                hn[1] = base_result
                                # print hn[1]

                        if (len(hn) > 1):
                            new_row[mani_index_base_num] = hn[1]
                        if (len(hn) > 0):
                            new_row[mani_index_building_num] = hn[0]

                    wr = csv.writer(fp, dialect='excel')
                    wr.writerow(new_row)

        fp.close()
    f.close()

    return return_manipulatedcsv

def processPostCodes(path, file):
    csvfile = path + file
    # print csvfile

    if not os.path.exists(Utils.PATH + "/tmp"):
        os.makedirs(Utils.PATH + "/tmp")

    if not os.path.exists(Utils.PATH + "/tmp" + "/process_post_codes"):
        os.makedirs(Utils.PATH + "/tmp" + "/process_post_codes")

    return_manipulatedcsv = Utils.PATH + "tmp" + "/process_post_codes/"

    manipulatedcsv = Utils.PATH + "tmp" + "/process_post_codes" + "/" + file

    with open(csvfile) as f:
        reader = csv.reader(f)
        header = next(reader)
        new_header = header
        new_header.append("POSTCODE1")
        new_header.append("POSTCODE2")

        with open(manipulatedcsv, "a") as fp:
            # Write headers
            writer = csv.DictWriter(fp, fieldnames=new_header)
            writer.writeheader()

        fp.close()
    f.close()

    with open(csvfile) as f:
        reader = csv.reader(f)
        header = next(reader)
        index_postcode = header.index(Utils.postcodes_column)

        with open(manipulatedcsv, "r+a") as fp:
            manipulated_file_reader = csv.reader(fp)
            manipulated_file_header = next(manipulated_file_reader)
            manipulated_index_postcode_1 = manipulated_file_header.index("POSTCODE1")
            manipulated_index_postcode_2 = manipulated_file_header.index("POSTCODE2")
            # Now data
            counter = 0
            for row in reader:
                new_row = [None] * len(manipulated_file_header)
                i = 0
                for value in row:
                    new_row[i] = value
                    i = i + 1

                pc = row[index_postcode]
                postcodes = pc.split(' ')

                if (len(postcodes) > 0):
                    new_row[manipulated_index_postcode_1] = postcodes[0]
                    # print postcodes[0]
                if (len(postcodes) > 1):
                    new_row[manipulated_index_postcode_2] = postcodes[1]

                wr = csv.writer(fp, dialect='excel')
                wr.writerow(new_row)

        fp.close()
    f.close()

    return return_manipulatedcsv

def removeJunkPostcodes(path, file):
    csvfile = path + file
    # print csvfile

    if not os.path.exists(Utils.PATH + "/tmp"):
        os.makedirs(Utils.PATH + "/tmp")

    if not os.path.exists(Utils.PATH + "/tmp" + "/remove_junk_postcodes"):
        os.makedirs(Utils.PATH + "/tmp" + "/remove_junk_postcodes")

    return_manipulatedcsv = Utils.PATH + "tmp" + "/remove_junk_postcodes/"

    manipulatedcsv = Utils.PATH + "tmp" + "/remove_junk_postcodes" + "/" + file

    with open(csvfile) as f:
        reader = csv.reader(f)
        header = next(reader)
        new_header = header

        with open(manipulatedcsv, "a") as fp:
            # Write headers
            writer = csv.DictWriter(fp, fieldnames=new_header)
            writer.writeheader()

        fp.close()
    f.close()

    with open(csvfile) as f:
        reader = csv.reader(f)
        header = next(reader)
        index_postcode1 = header.index("POSTCODE1")
        index_postcode2 = header.index("POSTCODE2")

        with open(manipulatedcsv, "r+a") as fp:
            manipulated_file_reader = csv.reader(fp)
            manipulated_file_header = next(manipulated_file_reader)
            # Now data
            counter = 0
            for row in reader:

                postcode1 = row[index_postcode1]
                postcode2 = row[index_postcode2]

                if not postcode1.isdigit():
                    # print postcode1
                    row[index_postcode1] = ""
                    row[index_postcode2] = ""

                # if not postcode2.isdigit():
                #     print postcode2

                wr = csv.writer(fp, dialect='excel')
                wr.writerow(row)

        fp.close()
    f.close()

    return return_manipulatedcsv

def keep_columns(path, file, keep_cols):
    csvfile = path + file
    # print csvfile

    if not os.path.exists(Utils.PATH + "/output"):
        os.makedirs(Utils.PATH + "/output")

    manipulatedcsv = Utils.PATH + "/output" + "/" + file
    df = pd.read_csv(csvfile, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
    # keep_cols.append("PREFIX")
    # keep_cols.append("POSTFIX")
    # keep_cols.append("POSTDIRECTIONAL")
    keep_cols.append("BASE_NUM")
    keep_cols.append("BUILD_NUM")
    keep_cols.append("POSTCODE1")
    keep_cols.append("POSTCODE2")
    new_df = df[keep_cols]
    new_df.to_csv(manipulatedcsv, index=False)

    shutil.rmtree(Utils.PATH + "/tmp")
