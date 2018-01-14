'''
This file houses functions for (ultimately) creating a link between the feature
name and description. This is crucial for filtering by survey question type b/c
types can be gleaned from descriptions.

The next step is to use these functions in 'clean.py' to filter between categories
of data and consider creating a class for all these functions instead of having
everything separated out like this.

Main categories of interest:
    DX - diagnosis features
    mental health features
    other features (example: housing, employment, etc.)

Outstanding TO-DO items for this file:
    - reformat code to use classes instead of functions
    - refactor code for efficiency and interpretability
    - practice writing tests by creating some for this py file

Use case:
    This code is intended for using with the public access crosswalk from the
    studies located at: http://www.icpsr.umich.edu/icpsrweb/ICPSR/studies/20240.
'''

# BASICS
def get_lines(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    return lines

# FILE PATHS
def file_name_list(file_path):
    '''
    Input: file path for text file containing list of csv file names.
    Output: list of csv file names.
    '''
    lines = get_lines(file_path)
    return [line.rstrip() for line in lines]
def make_paths(txt_path, csv_root_path):
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

# EXTRACTING GROUP, FEATURE TYPE, DESCRIPTION
def get_group_title(x):
    '''
    Input: file path to csv table for survey grouping (i.e. 'BLAGORAPHO-Table 1.csv')
    Output: group title for survey question (i.e. 'Agoraphobia')
    '''
    lines = get_lines(x)
    group_title = lines[0].split(',')[0]
    return group_title
def get_feature_names(file_path):
    '''
    Input: file path leading to csv file containing survey table for one survey category grouping
    (i.e. 'VLAGORAPHO-Table 1.csv')
    Output: dictionary where KEY = feature_name, VALUE = description of feature
    This function connects names like V01626 to descriptions like "Fear being alone"
    '''
    lines = get_lines(file_path)
    titles = []
    for line in lines[1:]:
        if line[0] == 'V':
            titles.append(line[0:6])
        elif line[1] == 'V':
            titles.append(line[1:7])
        else:
            # three responses in 'Constructed Demographic Variables' do not comply
            pass
    return titles
def get_descriptions(file_path):
    '''
    Input: file path to csv file containing feature name/description lines
    Output: list of descriptions
    '''
    lines = get_lines(file_path)
    descriptions = []
    for line in lines[1:]:
        start = line.find(':')+2
        end = line.find(',')
        descriptions.append(line[start:end].lower())
    return descriptions
def true_universals(file_path):
    '''
    Input: file path to csv file containing feature name/description lines
    Output: list of True/False depending on if the survey question appeared in
    all three surveys.
    '''
    lines = get_lines(file_path)
    true_false = []
    for line in lines[1:]:
        # each line includes the feature name if included in the survey
        # if any one of these are a '-' we want to mark it "False"
        check = line.split(',')[-3:]
        indicator = 0
        for element in check:
            if element == '-':
                indicator += 1
        if indicator > 0:
            true_false.append(False)
        else:
            true_false.append(True)
    return true_false
def make_feat_desc_dict(file_path):
    '''
    Input: file path to csv file containing feature table
    Output: a dictionary {group: {feature1: description1, feature2: description2}}
    '''
    title = get_group_title(file_path)
    features = get_feature_names(file_path)
    descriptions = get_descriptions(file_path)
    true_false = true_universals(file_path)
    feat_descr = {feature: [descriptions[idx], true_false[idx]] for idx, feature in enumerate(features)}
    titled = {title: feat_descr}
    return titled

if __name__ == "__main__":
    # LOCAL PATHS -- UPDATE FOR YOUR LOCAL PATHS AFTER DOWNLOADING DATA
    txt_path = '/Users/Winnifred/Desktop/Capstone/diagnosis_capstone/data/feature_group_file_names.txt'
    csv_root_path = '/Users/Winnifred/Desktop/Capstone/diagnosis_capstone/data/feature_name_data/'

    # dictionary = {}
    # for file_path in make_paths(txt_path, csv_root_path):
    #     dictionary[get_group_title(file_path)] = make_feat_desc_dict(file_path)
    #
    # print(dictionary.keys())











# end of doc