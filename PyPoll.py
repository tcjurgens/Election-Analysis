import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_results.txt")
#initialize total vote vounter
total_votes = 0
#candidate names
candidate_options = []   # empty list
candidate_votes = {}  # empty dictionary
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    # print each row in the CSV file
    for row in file_reader:
        # add to the total vote count
        total_votes += 1
        # get candidate name for each row
        candidate_name = row[2] 
 
        if candidate_name not in candidate_options:
            # adds name of all candidates who received votes to candidate_options
            candidate_options.append(candidate_name)   
            # begins tracking candidate votes
            candidate_votes[candidate_name] = 0
        # adds a vote to ea. candidates count
        candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")   # prints election results to the terminal , 'end=' equal to an empty string
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # below retrieves vote count and vote percentage
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes) *100
        # print ea. candidates votes/pct/etc. to the terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.2f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.2f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
