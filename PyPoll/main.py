#Import modules
import os
import csv
import numpy as np

#Path to .csv file
csvpath = os.path.join('.', 'PyPoll', 'Resources','election_data.csv')

#List for Ballot IDs
ballot_id = []
#List for County Names
county_name = []
#List for Candidate Names
candidate_name = []
#Unique list of candidate names
unique_candidate_names = []
#List for vote counts for each candidate
vote_counts = []

#Open .csv file
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #Skip header in .csv file
    csv_header = next(csvreader)
    #Populate lists
    for row in csvreader:
        ballot_id.append(int(row[0]))
        county_name.append(row[1])
        candidate_name.append(row[2])
        #Get count of votes
        total_vote_count = len(ballot_id)
#Create list of unique candidate names
unique_candidate_names = np.append(unique_candidate_names, np.unique(candidate_name))

#Create identifiers for each candidate
candidate_1_name = unique_candidate_names[0]
candidate_2_name = unique_candidate_names[1]
candidate_3_name = unique_candidate_names[2]

#Vote count for each candidate starts at 0
candidate_1_vote_count = 0
candidate_2_vote_count = 0
candidate_3_vote_count = 0

#Count number of times each candidate's name is listed
for i in candidate_name:
    if i == candidate_1_name:
        candidate_1_vote_count = candidate_1_vote_count + 1
    elif i == candidate_2_name:
        candidate_2_vote_count = candidate_2_vote_count + 1
    elif i == candidate_3_name:
        candidate_3_vote_count = candidate_3_vote_count + 1

#Populate vote_counts list with number of votes for each candidate in order of unique_candidate_names list
vote_counts.append(candidate_1_vote_count)
vote_counts.append(candidate_2_vote_count)
vote_counts.append(candidate_3_vote_count)

#Get index/position of max number in vote_counts list
max_vote_count_index = vote_counts.index(max(vote_counts))

#Return name from unique_candidate_names list that is in the position of max number in vote_counts list
candidate_winner = unique_candidate_names[max_vote_count_index]

#Calculate vote percentage for each candidate
candidate_1_vote_percent = "{:.3%}".format(candidate_1_vote_count / total_vote_count)
candidate_2_vote_percent = "{:.3%}".format(candidate_2_vote_count / total_vote_count)
candidate_3_vote_percent = "{:.3%}".format(candidate_3_vote_count / total_vote_count)

#Print results
print("Election Results")
print("-----------------------------")
print(f'Total Votes: {total_vote_count}')
print("-----------------------------")
print(f'{candidate_1_name}: {candidate_1_vote_percent} ({candidate_1_vote_count})')
print(f'{candidate_2_name}: {candidate_2_vote_percent} ({candidate_2_vote_count})')
print(f'{candidate_3_name}: {candidate_3_vote_percent} ({candidate_3_vote_count})')
print("-----------------------------")
print(f'Winner: {candidate_winner}')

#Export to analysis folder as .txt file
output_path = os.path.join('.', 'PyPoll', 'Analysis','pypoll_results.txt')

#Write text file
with open(output_path, 'w') as txtfile:
    txtwriter = csv.writer(txtfile)
    txtwriter.writerow(['Election Results'])
    txtwriter.writerow(['-----------------------------'])
    txtwriter.writerow([f'Total Votes: {total_vote_count}'])
    txtwriter.writerow(['-----------------------------'])
    txtwriter.writerow([f'{candidate_1_name}: {candidate_1_vote_percent} ({candidate_1_vote_count})'])
    txtwriter.writerow([f'{candidate_2_name}: {candidate_2_vote_percent} ({candidate_2_vote_count})'])
    txtwriter.writerow([f'{candidate_3_name}: {candidate_3_vote_percent} ({candidate_3_vote_count})'])
    txtwriter.writerow(['-----------------------------'])
    txtwriter.writerow([f'Winner: {candidate_winner}'])
