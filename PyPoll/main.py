# Import modules
import os
import csv

# Create path for csv
csvpath = os.path.join("Resources", "election_data.csv")

# Create lists and variables to use for analysis
totalVotes = 0
candidates = []
votes = []
percentVotes = []

# open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # loop through rows
    for row in csvreader:
        
        # Add to our vote-counter 
        totalVotes = totalVotes + 1 
        
        # Add unique candidates to the list and their respective votes
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_index = candidates.index(row[2])
            votes.append(1)
        
        # For candidates already in the list, add the respective vote to their name
        else:
            candidate_index = candidates.index(row[2])
            votes[candidate_index] = votes[candidate_index] + 1
    
    # Append the percentVotes list and initialize for printing later 
    for vote in votes:
        percentage = round((vote/totalVotes) * 100)
        percentage = "%.3f%%" % percentage
        percentVotes.append(percentage)
    
    # Identify candidate with the most votes
    winner_index = votes.index(max(votes))
    winningCandidate = candidates[winner_index]

# Print results in terminal
print("Election Results")
print("---------------------------")
print(f"Total Votes: {str(totalVotes)}")
print("---------------------------")
for c in range(len(candidates)):
    print(f"{candidates[c]}: {str(percentVotes[c])} ({str(votes[c])})")
print("---------------------------")
print(f"Winner: {winningCandidate}")
print("---------------------------")


# Export to txt file with the results
output_path = os.path.join("analysis", "election_analysis.txt")

# Open output file and write
with open(output_path, "w") as file:
    file.write('Election Results')
    file.write('\n')
    file.write('---------------------------')
    file.write('\n')
    file.write(f'Total Votes: {str(totalVotes)}')
    file.write('\n')
    file.write('---------------------------')
    file.write('\n')
    for c in range(len(candidates)):
        file.write(f'{candidates[c]}: {str(percentVotes[c])} ({str(votes[c])})')
        file.write('\n')
    file.write('---------------------------')
    file.write('\n')
    file.write(f'Winner: {winningCandidate}')
    file.write('\n')
    file.write('---------------------------')
