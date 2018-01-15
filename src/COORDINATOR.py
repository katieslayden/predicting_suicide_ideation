from SETUP import *
# from SPECIFY_FEATURES import *
# from CLEAN import *
# from MODEL import *

def main():
    filenames = '/Users/Winnifred/Desktop/Capstone/diagnosis_capstone/data/feature_group_file_names.txt'
    csv_root_path = '/Users/Winnifred/Desktop/Capstone/diagnosis_capstone/data/feature_name_data/'
    data_file = '/Users/Winnifred/Desktop/Capstone/ICPSR_20240_RAWDATA/DS0001/20240-0001-Data.tsv'

    set_inst = Setup(csv_root_path, filenames)
    full_dict = set_inst.run_setup()
    print(full_dict)

if __name__ == "__main__":
    main()
