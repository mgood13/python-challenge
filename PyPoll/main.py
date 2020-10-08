import os
import csv

electiondata = os.path.join('Resources', 'election_data.csv')
analysis = os.path.join('analysis','Election_Results.txt')

count = 0
candidates = []
votes = []



def generateoutput(months, total, average, goodday, maxprofit, badday, maxloss):
    # This function puts the output into a nice string that can be written into a file or printed to the terminal
    formatted = ('Election Results' + '\n' 
                '-------------------------' + '\n' +
                'Total Votes: ' + str(months) + '\n'
                '-------------------------' + '\n')

    return formatted


with open(electiondata, 'r') as electionfile:
    csvfile = csv.reader(electionfile, delimiter = ',')

    header = next(csvfile)

    for voter in csvfile:
        count += 1

        if voter[2] in candidates:
            # SOMETHING
            selection = candidates.index(voter[2])
            votes[selection] += 1

            print(voter[2])
        else:
            candidates.append(voter[2])
            votes.append(1)


        if count == 15:
            print(candidates)
            print(votes)
            break