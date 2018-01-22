'''
SETUP file contains the class Clean. This is step 2 of 4 in modeling to predict
suicide ideation using the ICPSR dataset on mental health.
All four steps are run from and return output to the COORDINATOR.py file.
'''
from sklearn.model_selection import train_test_split

class Clean():
    def __init__(self, dirty_df):
        self.dirty_df = dirty_df
        self.suicidality_features = ['V01995', 'V01997', 'V01999', 'V02044', 'V02003', 'V02004', 'V02009', 'V02023', 'V02025', 'V02027', 'V02029', 'V02031', 'V02032', 'V02035', 'V02036', 'V02041']

    def clean_up(self):
        df = self.dirty_df.drop(self.dirty_df[self.dirty_df['V01993'] == ' '].index)
        mask = {str(num): num for num in range(200000)}
        mask[' '] = 0
        mask['-9'] = -9
        mask['-8'] = -8
        mask[None] = 0

        for idx, feature in enumerate(list(df)):
            df[feature] = df[feature].map(mask)

        df.drop(suicidality_features, axis=1, inplace=True)
        df = df.dropna(axis=1)
        return df

    def to_matrix(self):
        df = self.clean_up()
        X_df = df.loc[:, df.columns != 'V01993']
        y_df = df['V01993'].map({5:0, 1:1, -9:0, -8:0})
        X = X_df.as_matrix()
        y = y_df.as_matrix()
        return X, y

    def train_test(self):
        X, y = self.to_matrix()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        return X_train, X_test, y_train, y_test

    def execute_clean(self):
        return self.train_test()
# label_ideation = 'V01993'
# TOTAL suicidality_features = ['V01992','V01994','V01995','V01996','V01997','V01998','V01999','V02000','V02044','V02045','V02001','V02002','V02003','V02004','V02005','V02009','V02010','V02023','V02024','V02025','V02026','V02027','V02028','V02029','V02030','V02031','V02032','V02033','V02034','V02035','V02036', 'V02037', 'V02041', 'V02042']
# suicidality_features = ['V01995', 'V01997', 'V01999', 'V02044', 'V02003', 'V02004', 'V02009', 'V02023', 'V02025', 'V02027', 'V02029', 'V02031', 'V02032', 'V02035', 'V02036', 'V02041']
