'''
This file holds code to clean the data for my Galvanize capstone project.
'''

import numpy as numpy
import pandas as pd


def clean_frequencies():
    '''
    Cleans data from survey "frequency" format to usable ints.
    Input: Array-like data structure.
    Output: None
    Notes:
    "Frequency" features are: {1: 'NEARLY ALL THE TIME', 2: 'PRETTY OFTEN',
    3: 'NOT VERY MUCH', 4: 'NEVER', -9: 'REFUSED', -8: 'DONT KNOW', '.': '-'}
    I'm assuming that the "-" responses are ones where there was missing data.
    '''
    return None

def clean_binaries():
    

def clean_continuous():
