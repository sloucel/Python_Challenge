# Election Results

# Import 
import os
import csv

# Create csvpath
csvpath = os.path.join('..', 'Resources','election_data.csv')

# Create block for TOTAL VOTES
def total_votes(csvreader):
    vote_count = 0
    for row_lp in csvreader:
        vote_count += 1
    return vote_count

# Create block for UNIQUE CANDIDATES
def count_unique_candidates(csvreader):
    # Create a list
    unique_candidates = []
    for row_lp in csvreader:
        # Check if file has a third element (index 2)
        if len(row_lp) > 2:
            candidate_name = row_lp[2]
            # Append candidates name to unique_candidates list
            if candidate_name not in unique_candidates:
                unique_candidates.append(candidate_name)
    return unique_candidates

# Create block for VOTE COUNT
def count_votes(csvreader):
    # Create dictionary to store unique votes
    candidate_votes = {}
    next(csvreader)
    for row_lp in csvreader:
        # Check if file has a third element (index 2)
        if len(row_lp) > 2:
            candidate_name = row_lp[2]
            # Checks if candidates name is in dictionary, if use add
            if candidate_name in candidate_votes:
                candidate_votes[candidate_name] += 1
            # If not already in the list, add 1
            else:
                candidate_votes[candidate_name] = 1
    #returns the dictionary
    return candidate_votes


# Open file and use define function blocks from above. 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    next(csvreader)
    total_votes_cast = total_votes(csvreader)

    csvfile.seek(0)
    unique_candidates = count_unique_candidates(csvreader)

    csvfile.seek(0)
    candidate_votes = count_votes(csvreader)

#Calculatue the winner
max_votes = 0
for candidate_name, vote_count in candidate_votes.items():
    # Check if the current candidate has more votes than the current maximum
    if vote_count > max_votes:
        # update max votes and set the winning candidate 
        max_votes = vote_count
        winner = candidate_name

# PRINT STATION    
print("Election Results")
print("------------------------------------")
print(f'Total Votes: {total_votes_cast}')
print("------------------------------------")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes_cast) * 100
    print(f'{candidate}: {percentage:.3f}% ({votes})')
print("------------------------------------")
print(f"Winner: {winner}")

## Export results to a new csv file and place in the the Analysis Folder
### Output_path
output_path = os.path.join("..", 'Analysis', 'election_results.txt')

##  Create a def block to simplify export .
def candidate_data(txtfile, candidate, votes, total_votes_cast):
    percentage = (votes / total_votes_cast) * 100
    txtfile.write(f"Candidate: {candidate}, Percentage of Votes: {percentage:.3f}%, Total Votes: {votes}\n")


with open(output_path, "w") as txtfile:
    # Write header
    txtfile.write("Candidate, Percentage of Votes, Total Votes\n")
    # Write data for each candidate
    for candidate, votes in candidate_votes.items():
        candidate_data(txtfile, candidate, votes, total_votes_cast)

print("Data has been written to", output_path)
# python main.py