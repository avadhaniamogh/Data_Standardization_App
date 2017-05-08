import os
import Utils

import filters
import split_fullname
import sort
# import short_version
# import dictionary

# outputAddress = '/home/amogh/Desktop/preandpostdir/output/'
#
# new_input_folder = '/home/amogh/Desktop/preandpostdir/input/'

# for add in os.listdir(new_input_folder):
#     if(add.endswith('.csv')):
        # print add
        # open_addresses_filters.toLowerCase(new_input_folder + add, outputAddress + add)
        # open_addresses_filters.removeRowsHavingNoStreetNames(new_input_folder + add, outputAddress + add)
        # split_fullname.split_fullname(new_input_folder + add, outputAddress + add)
        # open_addresses_filters.processHouseNumbers(new_input_folder + add, outputAddress + add)
        # open_addresses_filters.processPostCodes(new_input_folder + add, outputAddress + add)
        # open_addresses_filters.removeRearFromStreetNames(new_input_folder + add, outputAddress + add)
        # split_fullname.removePrefixFromEndofStreetName(new_input_folder + add, outputAddress + add)
        # open_addresses_filters.removePlaceOfFromCity(new_input_folder + add, outputAddress + add)
        # open_addresses_sort.addRowNumbers(new_input_folder + add, outputAddress + add)
        # open_addresses_sort.sortRowsOnStreetName(new_input_folder + add, outputAddress + add)
        # filters.keep_columns(new_input_folder + add, outputAddress + add)
        # short_version.convertToShortForm(new_input_folder + add, outputAddress + add)
        # add_txt = add.replace("csv", "txt")
        # print add
        # dictionary.make_dict(new_input_folder + add, outputAddress + add_txt)
        # open_addresses_filters.toLowerCase(new_input_folder + add, outputAddress + add)
        # split_fullname_new.printDirectionalFields(new_input_folder + add, outputAddress + add)
        # split_fullname.postDirectionalProcessing(new_input_folder + add, outputAddress + add)
        # open_addresses_filters.processHouseNumbers(new_input_folder + add, outputAddress + add)
        # open_addresses_sort.addRowNumbers(new_input_folder + add, outputAddress + add)
        # split_fullname.remedyPostDirectional(new_input_folder + add, outputAddress + add)


lower_case_csv = filters.toLowerCase(Utils.PATH, Utils.file)
print lower_case_csv
remove_rows_csv = filters.removeRowsHavingNoStreetNames(lower_case_csv, Utils.file)
print remove_rows_csv
split_full_name_csv = split_fullname.split_fullname(remove_rows_csv, Utils.file)
print split_full_name_csv
post_dir_process_csv = split_fullname.postDirectionalProcessing(split_full_name_csv, Utils.file)
print post_dir_process_csv
remedy_post_csv = split_fullname.remedyPostDirectional(post_dir_process_csv, Utils.file)
print remedy_post_csv
process_house_number_csv = filters.processHouseNumbers(remedy_post_csv, Utils.file)
print process_house_number_csv
process_post_codes_csv = filters.processPostCodes(process_house_number_csv, Utils.file)
print process_post_codes_csv
remove_junk_post_codes_csv = filters.removeJunkPostcodes(process_post_codes_csv, Utils.file)
print remove_junk_post_codes_csv
add_row_numbers_csv = sort.addRowNumbers(remove_junk_post_codes_csv, Utils.file)
print add_row_numbers_csv
sort_street_names_csv = sort.sortRowsOnStreetName(add_row_numbers_csv, Utils.file)
print sort_street_names_csv
filters.keep_columns(sort_street_names_csv, Utils.file, Utils.keep_cols)