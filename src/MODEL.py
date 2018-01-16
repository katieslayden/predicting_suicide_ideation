'''
SETUP file contains the class Setup. This is step 4 of 4 in modeling for
suicide ideation prediction from the ICPSR dataset on mental health.
All four steps are run from and return output to the COORDINATOR program.
'''

from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

class Make_Models(self):

    def __init__(self, df):
        self.X = df.loc[:, df.columns != 'suicide_ideation']
        self.y = df['suicide_ideation']
        self.X_train, self.y_train, self.X_test, self.y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    def print_scores(self, name, predictions):
        print(name, ': \n')
        print('Accuracy:', accuracy_score(self.y_test, predictions))
        print('Precision:', precision_score(self.y_test, predictions))
        print('Recall:', recall_score(self.y_test, predictions), '\n')
        return None

    def linear_regression(self):
        # self.print_scores(name, predictions)
        pass

    def logistic_regression(self):
        name = 'Logistic Regression'
        logreg = linear_model.LogisticRegression()
        model = logreg.fit(self.X_train, self.y_train)
        predictions = logreg.predict(self.X_test)
        self.print_scores(name, predictions)

    def decision_tree(self):
        name = 'Decision Tree'
        # self.print_scores(name, predictions)
        pass

    def random_forest(self):
        name = 'Random Forest'
        # self.print_scores(name, predictions)
        pass

    def KNN(self):
        name = 'KNN'
        # self.print_scores(name, predictions)
        pass

    def execute_models(self):
        self.linear_regression()
        self.logistic_regression()
        self.decision_tree()
        self.random_forest()
        self.KNN()
        return None 
