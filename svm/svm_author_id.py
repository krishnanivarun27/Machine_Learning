#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
clf = SVC(C=100.0, kernel='rbf')
# clf = SVC(kernel='linear')
# clf.fit(features_train,labels_train)

features_train = features_train[:len(features_train)/1000]
labels_train = labels_train[:len(labels_train)/1000]

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
c = 0
for x in range(1, len(pred)):
    if pred[x] == 1:
        c = c + 1
print "Total Count = ", c

print "Pred 10 = ", pred[10]
print "Pred 26 = ", pred[26]
print "Pred 50 = ", pred[50]
print "prediction time:", round(time()-t0, 3), "s"
print "Prediction"
print pred
accuracy = accuracy_score(pred, labels_test)
print(accuracy)

#########################################################

# sys.path.append("../visualization/")
# from class_viz import prettyPicture,output_image
# from sklearn.naive_bayes import GaussianNB
# ### draw the decision boundary with the text points overlaid
# prettyPicture(clf, features_test, labels_test)
# output_image("test.png", "png", open("test.png", "rb").read())


# import matplotlib.pyplot
# import pylab
#
# x = features_train
# y = features_test
#
# matplotlib.pyplot.scatter(x,y)
#
# matplotlib.pyplot.show()
