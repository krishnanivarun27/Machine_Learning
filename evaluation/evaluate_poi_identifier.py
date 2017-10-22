#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 


from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = \
    cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)

### it's all yours from here forward!

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
# clf = DecisionTreeClassifier(random_state=0)
clf = DecisionTreeClassifier()
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
# print accuracy_score(pred,labels_test)
of_true_positives = [(x,y) for x, y in zip(pred,labels_test) if x == y and x == 1.0]
print "True positives on the Overfitted model: ", len(of_true_positives)

print "Round", round(0.82758620689655171,4)

from sklearn.metrics import precision_score,recall_score
print "Precision",precision_score(labels_test, pred)
print "Recall",recall_score(labels_test, pred)