'''
This file stores variables detailing feature names.

Separates out the features based on their survey responses
in order to automate cleaning.

Once I determine which survey responses are of what type (there seem to be < 8 groups)
I can use those dictionaries (cryptic_feature_name: plain_english_description)
in my clean.py file.

Think about how to write replicable, approachable code.

The feature name dictionaries will be great later as well. The current names of
each feature are not interpretable. Having dictionaries with their meaningful
names will be crutial for interpretability.

So far I have spent a lot of time going back to the data docs. These should help
alleviate this back and forth.
'''

import numpy as np

def file_name_list(file_path):
    '''
    Input: file path for text file containing all feature cluster files.
    Output: list of csv file names.
    '''
    with open(file_path) as f:
        lines = f.readlines()
    return [line.rstrip() for line in lines]

def make_csv_paths(txt_path, csv_root_path):
    '''
    Input: path for text file containing csv file names, csv root path
    Output: list of file paths for each csv file
    '''
    csv_file_names = file_name_list(txt_path)
    csv_paths = []
    for file_name in csv_file_names:
        path = csv_root_path + file_name
        csv_paths.append(path)
    return csv_paths

def get_group_title(file_path):
    '''
    
    '''
    with open(file_path) as f:
        lines = f.readlines()
    # get grouping title from first line of file
    # assumes the first line is formatted similarly 'Agoraphobia,CPES,NCSR,NLAAS,NSAL'
    group_title = lines[0].split(',')[0]
    return group_title

def get_feature_names(file_path):
    '''
    Input: file path leading to csv file containing survey table for one survey category grouping
    (i.e. 'VLAGORAPHO-Table 1.csv')
    Output: dictionary where KEY = feature_name, VALUE = description of feature
    This function connects names like V01626 to descriptions like "Fear being alone"
    '''
    with open(file_path) as f:
        lines = f.readlines()
    # get grouping title from first line of file
    # assumes the first line is formatted similarly 'Agoraphobia,CPES,NCSR,NLAAS,NSAL'
    group_title = lines[0].split(',')[0]
    titles = []

    for line in lines[1:]:
        if line[0] == 'V':
            titles.append(line[0:6])
        elif line[1] == 'V':
            titles.append(line(1:7))
        else:
            print('problem with {}'.format(line))

    return None

if __name__ == "__main__":
    # CSV files = each line = feature title, description, origin of info
    lines_of_file_names = '/Users/Winnifred/Desktop/Capstone/diagnosis_capstone/data/feature_group_file_names.txt'
    csv_root_file_path = '/Users/Winnifred/Desktop/Capstone/diagnosis_capstone/data/feature_name_data/'

    print(make_csv_paths(lines_of_file_names, csv_root_file_path))








# end of doc
