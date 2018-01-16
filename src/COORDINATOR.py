'''
SETUP file contains the class Setup. This is step 1 of 4 in modeling for
suicide ideation prediction from the ICPSR dataset on mental health.
All four steps are run from and return output to the COORDINATOR program.
'''

from SETUP import *
from SPECIFY_FEATURES import *
# from CLEAN import *
# from MODEL import *


def main():
    data_file = '/Users/Winnifred/Desktop/Capstone/ICPSR_20240_RAWDATA/DS0001/20240-0001-Data.tsv'
    filenames = '/Users/Winnifred/Desktop/Capstone/diagnosis_capstone/data/feature_group_file_names.txt'
    csv_root_path = '/Users/Winnifred/Desktop/Capstone/diagnosis_capstone/data/feature_name_data/'

    set_inst = Setup(csv_root_path, filenames)
    complete_dict = set_inst.execute_setup()

    reduce_inst = Reduce_Features()


if __name__ == "__main__":
    main()
