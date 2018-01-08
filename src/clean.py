'''
This file holds code to reformat the data for my Galvanize capstone project.

Intended to be used for cleaning up data in http://www.icpsr.umich.edu/icpsrweb/ICPSR/studies/20240

'''

import numpy as numpy
import pandas as pd

# BASIC FUNCTIONS FOR INITIAL/COMMON DATAFRAME OPERATIONS
def column_average(df, feature):
    return None


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

if __name__ == "__main__":
    data_file = '/Users/Winnifred/Desktop/Capstone/ICPSR_20240_RAWDATA/DS0001/20240-0001-Data.tsv'
    reformat_frequencies(file)
