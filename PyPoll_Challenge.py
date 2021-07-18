import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_results.txt")
#initialize total vote vounter
total_votes = 0
#candidate names
candidate_options = []   # empty list
candidate_votes = {}  # empty dictionary
# 1: create a county list and county votes dictionary
county_options = []
county_votes = {}    # key: county    value: votes cast
# 2: Track the largest county and county voter turnout.
largest_turnout = ""   # county w largest turnout
county_count = 0      # no. of votes in the largest_turnout county
c_winning_percentage = 0

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
        # 3. extract county name from each row
        county_name = row[1]
  
        if candidate_name not in candidate_options:
            # adds name of all candidates who received votes to candidate_options
            candidate_options.append(candidate_name)   
            # begins tracking candidate votes
            candidate_votes[candidate_name] = 0
        # adds a vote to ea. candidates count
        candidate_votes[candidate_name] += 1

        if county_name not in county_options:      # SHOULD be 4/5 contained here
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1
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

     # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        c_vote = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        c_vote_percentage = float(c_vote)/float(total_votes) *100
        # 6d: Print the county results to the terminal.
        county_results = (f"County Votes\n{county_name}: {c_vote_percentage:.2f}% ({c_vote:,})\n")
        print(county_results)
        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (c_vote > county_count) and (c_vote_percentage > c_winning_percentage):
            couunty_count = county_votes
            c_winning_percentage = c_vote_percentage
            largest_turnout = county_name
    # 7: Print the county with the largest turnout to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_turnout}\n"
        f"-------------------------\n")
    print(winning_county_summary)
    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

    # Save the final candidate vote count to the text file.
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
