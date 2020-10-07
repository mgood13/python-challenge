import os
import csv


budgetdata = os.path.join('Resources', 'budget_data.csv')

with open(budgetdata,'r') as budgetfile:
    csvfile = csv.reader(budgetfile, delimiter = ',')

    for i in csvfile:
        print(i)