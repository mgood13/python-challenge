import os
import csv


budgetdata = os.path.join('Resources', 'budget_data.csv')
count = 0
profit = 0
currentpl = 0
previouspl = 0
changes = []
totalpl = 0
avgpl = 0.0



with open(budgetdata, 'r') as budgetfile:
    csvfile = csv.reader(budgetfile, delimiter = ',')

    # Remove the headers and store them just in case
    header = next(csvfile)

    for i in csvfile:
        # Count will hold on to the number of lines that we find in the file
        count += 1



        if count == 1:
            # Special case for the first loop
            # Initial change is set to 0 to avoid skewing average change on the high side
            # Store the previous line's profit/loss for calculation of change in next iteration
            changes.append(0)
            previouspl = float(i[1])
            currentpl = 0

        else:
            # Grab the current profit loss then calculate average and move current to previous
            currentpl = float(i[1])
            changes.append(currentpl-previouspl)
            print(currentpl-previouspl)
            previouspl = currentpl


        profit = profit + currentpl

    for j in changes:
        totalpl += j

    # Here we use count - 1 instead of just count because we don't want to count the initial row
    # We only count the rows where we get a real change
    # Also round because we don't really need those extra 11 decimal places
    avgpl = round(totalpl / (count-1), 2)
    print(avgpl)
