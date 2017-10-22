#!/usr/bin/python
print "Hello python"

# """
#     This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.
#
#     Use a Naive Bayes Classifier to identify emails by their authors
#
#     authors and labels:
#     Sara has label 0
#     Chris has label 1
# """

import sys
from time import time

sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# from sklearn.naive_bayes import

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels

features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###

clf = GaussianNB()
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"
print "Prediction"
print pred
accuracy = accuracy_score(pred, labels_test)
print(accuracy)
#########################################################

sys.path.append("../visualization/")
from class_viz import prettyPicture,output_image
from sklearn.naive_bayes import GaussianNB
### draw the decision boundary with the text points overlaid
prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())



# import matplotlib.pyplot
# import pylab
#
# x = features_train
# y = features_test
#
# matplotlib.pyplot.scatter(x,y)
#
# matplotlib.pyplot.show()