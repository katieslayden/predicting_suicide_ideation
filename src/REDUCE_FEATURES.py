'''
REDUCE_FEATURES file contains the class Reduce_Features. This is step 2 of 4 in
modeling for suicide ideation prediction from the ICPSR dataset on mental health.
All four steps are run from and return output to the COORDINATOR program.
'''
import pandas as pd

class Reduce_Features():

    def __init__(self, data_file, full_dict):
        self.full_dict = full_dict
        self.universals, _ = self.get_universals()
        self.messy_df = pd.read_csv(data_file, sep='\t', low_memory=False)

    def get_universals(self):
        universals = {}
        nonuniversals = {}
        for akey, avalue in self.full_dict.items():
            for bkey, bvalue in avalue.items():
                for ckey, cvalue in bvalue.items():
                    if cvalue[1] == True:
                        universals[ckey] = cvalue
                    else:
                        nonuniversals[ckey] = cvalue
        return universals, nonuniversals

    def feature_max(self, feature):
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

    def get_feat_max5(self):
        clean_df = pd.DataFrame()

        good_features = list(self.universal_features.keys())
        for feature in good_features:
            clean_df[feature] = self.messy_df[feature]

        feature_uniques = {}
        for feature in good_features:
            feature_uniques[feature] = list(pd.unique(clean_df[feature]))

        features_max5 = []
        for feature in good_features:
            if self.feature_max(feature) <= 5.0:
                features_max5.append(feature)

        return features_max5

    def execute_reduce(self):
        reduced_df = pd.DataFrame()
        for feature in features_max5:
            reduced_df[feature] = self.messy_df[feature]
        return reduced_df
