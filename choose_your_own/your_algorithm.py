#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.svm import SVC
clf_SVC = SVC(C=100.0, kernel='rbf',probability=True)

# clf_SVC = SVC(kernel='linear',probability=True)
# clf.fit(features_train,labels_train)

# features_train_SVC = features_train[:len(features_train)/100]
# labels_train_SVC = labels_train[:len(labels_train)/100]
# clf_SVC.fit(features_train_SVC, labels_train_SVC)

clf_SVC.fit(features_train, labels_train)
pred_SVC = clf_SVC.predict(features_test)
print "SVC accuracy"
print accuracy_score(pred_SVC,labels_test)


clf = AdaBoostClassifier(base_estimator=clf_SVC,n_estimators=30,learning_rate=1.5)
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
print accuracy_score(pred,labels_test)






try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
