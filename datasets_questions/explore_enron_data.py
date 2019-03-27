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

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

print "%d people in this dataset" % len(enron_data) 

print "Each people has %d features. " % len(enron_data["SKILLING JEFFREY K"]) 

POIs = [] 
for people in enron_data: 
    if enron_data[people]["poi"]==1: 
        POIs.append(people) 
print "%d POIs in E+F datasets" % len(POIs) # sum([enron_data[people]["poi"]==1 for people in enron_data.keys()]) 

POI_list_com = open("../final_project/poi_names.txt", "r") 
names = POI_list_com.readlines()[2:] 
POIs_identified = [] 
for name in names: 
    name_reformate = name[4:-1].upper().replace(',', '') 
    POIs_identified.append(name_reformate) 
print "There are %d POIs identified from news" % len(POIs_identified) 

# print enron_data["PRENTICE JAMES"].keys()
print "James Prentice owns %f of stocks" % enron_data["PRENTICE JAMES"]["total_stock_value"]

print "Wesley Colwell sent %d emails to POIs. " % enron_data["COLWELL WESLEY"]["from_this_person_to_poi"] 

print "Jeff Skilling excised %.3f value of stock" % enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "Jeff Skilling took $ %.3f payment. " % enron_data["SKILLING JEFFREY K"]["total_payments"] 
print "Kenneth Lay took $ %.3f payment. " % enron_data["LAY KENNETH L"]["total_payments"] 
print "Andrew Fastow took $ %.3f payment. " % enron_data["FASTOW ANDREW S"]["total_payments"] 

count_salary = 0 
count_email = 0 
count_payment = 0 
for people in enron_data: 
    if enron_data[people]["salary"] != 'NaN': 
        count_salary += 1 
    if enron_data[people]['email_address'] != 'NaN': 
        count_email += 1 
    if enron_data[people]['total_payments'] != 'NaN': 
        count_payment += 1 

print "%d people have a qualified salary. " % count_salary 
print "%d people have an email address. " % count_email 

print "%d people don't have a payment info." % (len(enron_data) - count_payment)  
print "Percentage of people have \'NaN\' payments: ", (1. - count_payment/float(len(enron_data))) * 100, "%" 

count_POI_payment = 0 
for people in POIs: 
    if enron_data[people]['total_payments'] != 'NaN': 
        count_POI_payment += 1 
print "Percentage of POIs have \'NaN\' payments: %.3f " % (1 - float(count_POI_payment)/len(POIs))  
