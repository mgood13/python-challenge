import os
import csv

electiondata = os.path.join('Resources', 'election_data.csv')
analysis = os.path.join('analysis','Election_Results.txt')


def generateoutput(months, total, average, goodday, maxprofit, badday, maxloss):
    # This function puts the output into a nice string that can be written into a file or printed to the terminal
    formatted = ('Financial Analysis' + '\n' 
                '--------------------' + '\n' +
                'Total Months: ' + str(months) + '\n'
                'Total: $' + str(total) + '\n'
                'Average Change: $' + str(average) + '\n'
                'Greatest Increase in Profits: ' + goodday + " ($" + str(maxprofit) + ")" + '\n'
                'Greatest Decrease in Profits: ' + badday + " ($" + str(maxloss) + ")")

    return formatted


with open(electiondata, 'r') as electionfile:
    csvfile = csv.reader(electionfile, delimiter = ',')
