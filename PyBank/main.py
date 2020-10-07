import os
import csv


budgetdata = os.path.join('Resources', 'budget_data.csv')
count = 0
profit = 0



with open(budgetdata, 'r') as budgetfile:
    csvfile = csv.reader(budgetfile, delimiter = ',')

    # Remove the headers and store them just in case
    header = next(csvfile)

    for i in csvfile:
        # Count will hold on to the number of lines that we find in the file
        count += 1
        profit = profit + float(i[1])

    print(profit)