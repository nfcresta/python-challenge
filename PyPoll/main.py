# Import modules
import os
import csv

# Create path for csv
csvpath = os.path.join("Resources", "election_data.csv")

totalVotes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0

# open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    # print(f'{header}')

    # loop through rows to find votes
    for row in csvreader:
        # Add to our vote-counter 
        total_votes += 1 

        '''
        If the candidate is not on our list, add his/her name to our list, along with 
        a vote in his/her name.
        If he/she is already on our list, we will simply add a vote in his/her
        name 
        '''
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    # Add to percent_votes list 
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    # Find the winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")