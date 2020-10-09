import os
import csv
import numpy

electiondata = os.path.join('Resources', 'election_data.csv')
analysis = os.path.join('analysis','Election_Results.txt')

count = 0
candidates = []
votes = []
percentages = []
finalout = ""



def generateoutput(totalvotes, candidates, earnedvotes, percentages, winner):
    # This function puts the output into a nice string that can be written into a file or printed to the terminal
    formatted = ('Election Results' + '\n' 
                '-------------------------' + '\n' +
                'Total Votes: ' + str(totalvotes) + '\n'
                '-------------------------' + '\n')
    for i in range(len(candidates)):
        formatted += str(candidates[i]) + ": " + str(percentages[i]) + "% (" + str(earnedvotes[i]) + ")\n"

    formatted += ('-------------------------' + '\n' 
                  "Winner: " + winner + '\n'
                '-------------------------'
                  )

    return formatted


with open(electiondata, 'r') as electionfile:
    csvfile = csv.reader(electionfile, delimiter = ',')

    header = next(csvfile)

    for voter in csvfile:
        count += 1

        if voter[2] in candidates:
            selection = candidates.index(voter[2])
            votes[selection] += 1

        else:
            candidates.append(voter[2])
            votes.append(1)


for i in votes:
    percentages.append(numpy.round((i/count * 100),3))

max = percentages.index(max(percentages))
winner = candidates[max]

finalout = generateoutput(count, candidates, votes, percentages, winner)
print(finalout)