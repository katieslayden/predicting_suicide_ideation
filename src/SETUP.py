class Setup():
    def __init__(self, csv_root_path, txt_path):
        self.root = csv_root_path
        self.txt_path = txt_path
        self.all_paths = []

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
            self.all_paths.append(path)
        return csv_paths

    # EXTRACTING GROUP, FEATURE TYPE, DESCRIPTION
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

    def true_universals(self, file_path):
        '''
        Input: file path to csv file containing feature name/description lines
        Output: list of True/False depending on if the survey question appeared in
        all three surveys.
        '''
        with open(filepath) as f:
            lines = f.readlines()
        true_false = []
        for line in lines[1:]:
            # each line includes the feature name for each survey it was in
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

    def make_dict(self, file_path):
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

    def run_setup(self):
        full_dict = {}
        for file_path in self.all_paths:
            dictionary[self.get_group_title(file_path)] = self.make_dict(file_path)
        return full_dict





# end of doc
