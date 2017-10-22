#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle,pprint
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
values_dict = enron_data.values()
pprint.pprint(enron_data)

i = 0
poi_counter = 0
while i < len(values_dict) :
    if values_dict[i].get('poi') == True:
        poi_counter = poi_counter + 1
    i = i+1
print "POI Counter" , poi_counter

import sys
sys.path.append("../final_project/")
from poi_email_addresses import poiEmails

email_list = poiEmails()
print len(email_list)

i = 0
poi_counter = 0
while i < len(values_dict) :
    if values_dict[i].get('poi') == True:
        poi_counter = poi_counter + 1
    i = i+1
print "POI Counter" , poi_counter

sys.path.append("../final_project/")
feature_list = ["poi", "salary", "bonus"]
data_array = featureFormat( data_dictionary, feature_list )
label, features = targetFeatureSplit(data_array)


    # c=0
    # while c < len(values_dict[i].keys()) :
    #     c =c + 1
    # print c

# print enron_data[10]
