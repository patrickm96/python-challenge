import os
import csv
import numpy as np
import array as arr

csvpath = os.path.join('.','PyRoll', 'Resources','election_data.csv')

ballot_id = []
county_name = []
candidate_name = []
unique_candidate_names = []


with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #print(csvreader)

    csv_header = next(csvreader)

    for row in csvreader:
        ballot_id.append(int(row[0]))
        county_name.append(row[1])
        candidate_name.append(row[2])
        total_votes = len(ballot_id)

#print(candidate_name)

unique_candidate_names = np.append(unique_candidate_names, np.unique(candidate_name))
candidate_1_name = unique_candidate_names[0]
candidate_1_vote_count = candidate_name.count(candidate_1_name)

print(candidate_1_name)
print(candidate_1_vote_count)

print(total_votes)
print(unique_candidate_names)

print("Election Results")
print("-----------------------------")
print(f'Total Votes: {total_votes}')
print("-----------------------------")