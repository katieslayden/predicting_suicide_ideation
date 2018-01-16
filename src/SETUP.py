'''
SETUP file contains the class Setup. This is step 1 of 4 in modeling for
suicide ideation prediction from the ICPSR dataset on mental health.
All four steps are run from and return output to the COORDINATOR program.
'''

class Setup():

    def __init__(self, csv_root_path, txt_path):
        self.root = csv_root_path
        self.txt_path = txt_path
        self.all_paths = self.make_paths()

    def file_name_list(self):
        '''
        Input: file path for text file containing list of csv file names
        Output: list of csv file names
        '''
        with open(self.txt_path) as f:
            filenames = f.readlines()
        return [file_.rstrip() for file_ in filenames]

    def make_paths(self):
        '''
        Input: path for text file containing csv file names, csv root path
        Output: list of file paths for each csv file
        '''
        csv_file_names = self.file_name_list()
        csv_paths = []
        for file_name in csv_file_names:
            path = self.root + file_name
            csv_paths.append(path)
        return csv_paths

    def get_group_title(self, filepath):
        '''
        Input: file path to csv table for survey grouping (i.e. 'BLAGORAPHO-Table 1.csv')
        Output: group title for survey question (i.e. 'Agoraphobia')
        '''
        with open(filepath) as f:
            lines = f.readlines()
        return lines[0].split(',')[0]

    def get_feature_names(self, filepath):
        '''
        Input: file path leading to csv file containing survey table for one survey category grouping
        (i.e. 'VLAGORAPHO-Table 1.csv')
        Output: dictionary where KEY = feature_name, VALUE = description of feature
        This function connects names like V01626 to descriptions like "Fear being alone"
        '''
        with open(filepath) as f:
            lines = f.readlines()
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

    def get_descriptions(self, filepath):
        '''
        Input: file path to csv file containing feature name/description lines
        Output: list of descriptions
        '''
        with open(filepath) as f:
            lines = f.readlines()
        descriptions = []
        for line in lines[1:]:
            start = line.find(':')+2
            end = line.find(',')
            descriptions.append(line[start:end].lower())
        return descriptions

    def true_universals(self, filepath):
        '''
        Input: file path to csv file containing feature name/description lines
        Output: list of True/False depending on if the survey question appeared in
        all three surveys.
        '''
        with open(filepath) as f:
            lines = f.readlines()
        true_false = []
        for line in lines[1:]:
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

    def make_dict(self, filepath):
        '''
        Input: file path to csv file containing feature table
        Output: a dictionary {group: {feature1: description1, feature2: description2}}
        '''
        title = self.get_group_title(filepath)
        features = self.get_feature_names(filepath)
        descriptions = self.get_descriptions(filepath)
        true_false = self.true_universals(filepath)
        feat_descr = {feature: [descriptions[idx], true_false[idx]] for idx, feature in enumerate(features)}
        titled = {title: feat_descr}
        return titled

    def run_setup(self):
        '''
        Class method to run all setup class methods and return complete dictionary.
        '''
        full_dict = {}
        for filepath in self.all_paths:
            full_dict[self.get_group_title(filepath)] = self.make_dict(filepath)
        return full_dict
