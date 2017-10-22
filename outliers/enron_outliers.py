#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop('TOTAL',0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)
print "Data Dicxt" , data_dict

sal_list = []
bon_list = []
for key,value in data_dict.items() :
    print "Nesting" , value['salary']
    sal_list.append(value['salary'])
    bon_list.append(value['bonus'])

print "sal lisaslkdfj", sal_list
tup_name_sal = zip(data_dict.keys(),sal_list,bon_list)
print "Sal List",tup_name_sal
print "Sal sorted", sorted(tup_name_sal,reverse=True,key=lambda x:x[1])

stock_list = []
for key,value in data_dict.items() :
    print "Nesting" , value["exercised_stock_options"]
    stock_list.append(value["exercised_stock_options"])

tup_name_stock = zip(data_dict.keys(),sal_list)
print "Stock List",tup_name_stock
print "Filtered",filter(lambda x: x[0] != 'NaN', tup_name_stock)
filtered = filter(lambda x: x[1] != 'NaN', tup_name_stock)
print "Stock sorted", sorted(filtered,reverse=True,key=lambda x:x[1])





### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


