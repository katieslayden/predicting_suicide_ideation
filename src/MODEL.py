'''
SETUP file contains the class Setup. This is step 1 of 4 in modeling to predict
suicide ideation using the ICPSR dataset on mental health.
All four steps are run from and return output to the COORDINATOR.py file.
'''

from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

class Make_Models(self):

    def __init__(self, X_train, y_train, X_test, y_test):
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test

    def print_scores(self, name, predictions):
        print(name, ': \n')
        print('Accuracy:', accuracy_score(self.y_test, predictions))
        print('Precision:', precision_score(self.y_test, predictions))
        print('Recall:', recall_score(self.y_test, predictions), '\n')
        return None

    # def logistic_regression(self):
    #     name = 'Logistic Regression'
    #     logreg = linear_model.LogisticRegression()
    #     model = logreg.fit(self.X_train, self.y_train)
    #     predictions = logreg.predict(self.X_test)
    #     self.print_scores(name, predictions)

    def random_forest(self):
        name = 'Random Forest'
        clf = RandomForestClassifier(bootstrap= True,
                                     class_weight= None,
                                     criterion= 'gini',
                                     max_depth= 20,
                                     max_features= 'auto',
                                     max_leaf_nodes= None,
                                     min_impurity_split= 1e-07,
                                     min_samples_leaf= 1,
                                     min_samples_split= 2,
                                     min_weight_fraction_leaf= 0.0,
                                     n_estimators= 150,
                                     n_jobs= 1,
                                     oob_score= True,
                                     random_state= 0,
                                     verbose= 0,
                                     warm_start= True)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        score = clf.score(X,y)
        oob_score = clf.oob_score_
        confusion_matrix = pd.DataFrame(
                                        confusion_matrix(y_test, y_pred),
                                        columns=['Predicted No Ideation', 'Predicted Ideation'],
                                        index=['True No Ideation', 'True Ideation']
                                        )
        return self.print_scores(name, predictions)

    def execute_models(self):
        return self.random_forest()
