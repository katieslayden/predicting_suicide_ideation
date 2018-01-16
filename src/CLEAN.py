'''
SETUP file contains the class Clean. This is step 3 of 4 in modeling for
suicide ideation prediction from the ICPSR dataset on mental health.
All four steps are run from and return output to the COORDINATOR program.
'''

class Clean():





    def get_group(self, feature):
        for akey, apair in self.full_dict.items():
            for bkey, bpair in apair.items():
                for ckey, cpair in bpair.items():
                    if feature == ckey:
                        return bkey

    def get_descriptions(self, feature):
        for akey, apair in self.full_dict.items():
            for bkey, bpair in apair.items():
                for ckey, cpair in bpair.items():
                    if feature == ckey:
                        return cpair[0]

    def return_group_descriptions(self, feature_list):
        '''
        Input: feature list and full dictionary
        Output: a list of unique groups and a list of descriptions
        '''
        groups = []
        descriptions = []
        for feature in features_list:
            groups.append(self.get_group(feature))
            descriptions.append(self.get_descriptions(feature))
        return list(set(groups)), descriptions
