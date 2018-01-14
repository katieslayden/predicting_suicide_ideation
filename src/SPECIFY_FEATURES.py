from about_data import *
import numpy as numpy
import pandas as pd

# BASIC FUNCTIONS FOR INITIAL/COMMON DATAFRAME OPERATIONS
def setup(txt_path, csv_root_path):
    dictionary = {}
    for file_path in make_paths(txt_path, csv_root_path):
        dictionary[get_group_title(file_path)] = make_feat_desc_dict(file_path)
    return dictionary
def create_dataframe(csv_data_file):
    df = pd.read_csv(csv_data_file, sep='\t', low_memory=False)
    return df
def column_average(df, feature):
    return None

# DEFINING WHAT WE DO AND DO NOT WANT TO KEEP
def get_universals(txt_path, csv_root_path):
    '''
    Identify features that are universal (in all three surveys) and nonuniversal.
    Input: dictionary
    Output: keys where the second item in the value list is True
    '''
    universals = {}
    nonuniversals = {}
    comprehensive = setup(txt_path, csv_root_path)
    for akey, avalue in comprehensive.items():
        for bkey, bvalue in avalue.items():
            for ckey, cvalue in bvalue.items():
                if cvalue[1] == True:
                    universals[ckey] = cvalue
                else:
                    nonuniversals[ckey] = cvalue
    return universals, nonuniversals

def feature_max(feature):
    x = feature_uniques[feature]
    # x is [' ', '-8', '-9', '1', '5']
    sorted_x = sorted(x, reverse=True)
    # sorted_x is ['5', '1', '-9', '-8', ' ']
    no_space = sorted_x[0:-1]
    # no_space is ['5', '1', '-9', '-8']
    range_list = []
    for i in no_space:
        range_list.append(float(i))
    # range_list is [5, 1, -9, -8]
    # min(range_list) is -9
    # max(range_list) is 5
    return max(range_list)
def clean_by_max(data_file, maxvalue=5):
    '''
    Input: data_file, maxvalue desired in unique values for a column
    Output:
    '''
    messy_df = pd.read_csv(data_file, sep='\t', low_memory=False)
    clean_df = pd.DataFrame()

    universal_features, nonuniversal_features = get_universals(txt_path, csv_root_path)

    good_features = list(universal_features.keys())
    for feature in good_features:
        clean_df[feature] = messy_df[feature]

    feature_uniques = {}
    for feature in good_features:
        feature_uniques[feature] = list(pd.unique(clean_df[feature]))

    features_max5 = []
    for feature in good_features:
        if feature_max(feature) <= 5.0:
            features_max5.append(feature)

    return features_max5

def get_group(feature, full_dict):
    for akey, apair in full_dict.items():
        for bkey, bpair in apair.items():
            for ckey, cpair in bpair.items():
                if feature == ckey:
                    return bkey
def get_descriptions(feature, full_dict):
    for akey, apair in full_dict.items():
        for bkey, bpair in apair.items():
            for ckey, cpair in bpair.items():
                if feature == ckey:
                    return cpair[0]
def return_group_descriptions(feature_list, full_dict):
    '''
    Input: feature list and full dictionary
    Output: a list of unique groups and a list of descriptions
    '''
    groups = []
    descriptions = []
    for feature in features_list:
        groups.append(get_group(feature, full_dict))
        descriptions.append(get_descriptions(feature, full_dict))
    return list(set(groups)), descriptions

# INTERMEDIATE FUNCTIONS FOR REFORMATTING / CLEANING
def reformat_frequencies(df, columns):
    '''
    Reformats data from survey "frequency" format.

    Input: Array-like data structure in "frequency" format.
    Output: Array-like data structure, reformatted for modeling.

    "Frequency" format:
    {1: 'NEARLY ALL THE TIME', 2: 'PRETTY OFTEN', 3: 'NOT VERY MUCH',
    4: 'NEVER', -9: 'REFUSED', -8: 'DONT KNOW', '.': '-'}
    Assume "-" responses are missing data.

    Reformatted:
    {1: ['NEARLY ALL THE TIME', 'PRETTY OFTEN'],
    0: ['NOT VERY MUCH', 'NEVER', 'REFUSED', 'DONT KNOW', '-']}
    '''

    return None
def reformat_ratings(df, feature_names, new_value):
    '''
    Cleans data from survey "rating" format.

    Input: Array-like data structure in "rating" format.
    Output: Array-like data structure, reformatted for modeling.

    "Rating" format:
    {1: 'EXCELLENT', 2: 'VERY GOOD', 3: 'GOOD', 4: 'FAIR', 5: 'POOR',
    -9: 'REFUSED', -8: 'DONT KNOW', '.': '-'}

    Reformatted:
    {1: 'EXCELLENT', 2: 'VERY GOOD', 3: 'GOOD', 4: 'FAIR', 5: 'POOR',
    new_value: ['REFUSED', 'DONT KNOW', '_']}
    '''
    # The problem with this one is that I don't want to reformat the NaN values
    # because I don't want to attribute a numeric value to them that doesn't map
    # Consider replacing them with the average value? Maybe make the column avg
    # the default and allow user to change the value?
    mask = {-9: new_value, -8: new_value, '.': new_value}

    for feature in feature_names:
        # replace the current value of bad values with useful ones
        pass
    return None
def clean_binaries(df):
    '''
    What does a binary question look like in this data? Yes/No ?
    '''
    return None
def clean_continuous(df):
    '''
    What kind of cleaning do continuous features need?
    '''
    return None

def main():
    data_file = '/Users/Winnifred/Desktop/Capstone/ICPSR_20240_RAWDATA/DS0001/20240-0001-Data.tsv'
    txt_path = '/Users/Winnifred/Desktop/Capstone/diagnosis_capstone/data/feature_group_file_names.txt'
    csv_root_path = '/Users/Winnifred/Desktop/Capstone/diagnosis_capstone/data/feature_name_data/'

if __name__ == "__main__":
    main()

















# end of file
