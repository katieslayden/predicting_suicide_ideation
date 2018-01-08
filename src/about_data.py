'''
This file stores variables detailing feature names.

Separate out the features based on their survey responses in order to automate
a lot of the cleaning.

Once I determine which survey responses are of what type (there seem to be < 8 groups)
I can use those dictionaries (cryptic_feature_name: plain_english_description)
in my make_data_clean.py file.

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
    Return: list of csv file names.
    '''
    with open(path) as f:
        lines = f.readlines()
    return [line.rstrip() for line in lines]

def make_csv_paths


if __name__ == "__main__":
    txt_file_path = '/Users/Winnifred/Desktop/Capstone/diagnosis_capstone/data/feature_group_file_names.txt'
    csv_root_file_path = '/Users/Winnifred/Desktop/Capstone/diagnosis_capstone/data/feature_name_data/'
    file_name_list(txt_file_path)








# end of doc
