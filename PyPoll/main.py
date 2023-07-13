import os
import csv
import numpy as np
import array as arr

csvpath = os.path.join('.','PyPoll', 'Resources','election_data.csv')

ballot_id = []
county_name = []
candidate_name = []
unique_candidate_names = []
vote_counts = []


with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #print(csvreader)

    csv_header = next(csvreader)

    for row in csvreader:
        ballot_id.append(int(row[0]))
        county_name.append(row[1])
        candidate_name.append(row[2])
        total_vote_count = len(ballot_id)

unique_candidate_names = np.append(unique_candidate_names, np.unique(candidate_name))
candidate_1_name = unique_candidate_names[0]
candidate_2_name = unique_candidate_names[1]
candidate_3_name = unique_candidate_names[2]

candidate_1_vote_count = 0
candidate_2_vote_count = 0
candidate_3_vote_count = 0

#print(candidate_1_vote_count + 1)

for i in candidate_name:
    if i == candidate_1_name:
        candidate_1_vote_count = candidate_1_vote_count + 1
    elif i == candidate_2_name:
        candidate_2_vote_count = candidate_2_vote_count + 1
    elif i == candidate_3_name:
        candidate_3_vote_count = candidate_3_vote_count + 1

#candidate_1_vote_count = candidate_name.count(candidate_1_name)

vote_counts.append(candidate_1_vote_count)
vote_counts.append(candidate_2_vote_count)
vote_counts.append(candidate_3_vote_count)

#print(vote_counts)
#max_vote_counts = str(np.where(vote_counts == max(vote_counts))[0][0])
#print(max_vote_counts)
#max_vote_counts_integer = int(max_vote_counts)
#max_votes_winner = unique_candidate_names[max_vote_counts_integer]

max_vote_count_index = vote_counts.index(max(vote_counts))

#print(max_vote_count_index)
candidate_winner = unique_candidate_names[max_vote_count_index]

#print(candidate_1_name)
#print(candidate_1_vote_count)
#print(candidate_2_vote_count)
#print(candidate_3_vote_count)

candidate_1_vote_percent = "{:.3%}".format(candidate_1_vote_count / total_vote_count)
candidate_2_vote_percent = "{:.3%}".format(candidate_2_vote_count / total_vote_count)
candidate_3_vote_percent = "{:.3%}".format(candidate_3_vote_count / total_vote_count)

#print(candidate_1_vote_percent)

#print(total_votes)
#print(unique_candidate_names)

print("Election Results")
print("-----------------------------")
print(f'Total Votes: {total_vote_count}')
print("-----------------------------")
print(f'{candidate_1_name}: {candidate_1_vote_percent} ({candidate_1_vote_count})')
print(f'{candidate_2_name}: {candidate_2_vote_percent} ({candidate_2_vote_count})')
print(f'{candidate_3_name}: {candidate_3_vote_percent} ({candidate_3_vote_count})')
print("-----------------------------")
print(f'Winner: {candidate_winner}')
