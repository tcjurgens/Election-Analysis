# Election-Analysis
## Overview of Election Audit

This wk we were introduced to Python. While using/learning Python, we spent time reviewing election results for a US Congressional presinct in Colorado.

In this module we were asked to write a Python script capable of showing:
- the Total Votes Cast
- List of Candidates who received votes
- Number of Votes received by each Candidate
- Percentage of Votes each Candidate received
- Winner of the Election based on Popular Vote

Further-- we were asked in the challenge to show:
- Voter Turnout or each County
- the Percentage of Votes from each County (out of total count)
- the County with the highest Voter Turnout


## Election Audit Results

Below is a screenshot of the election results printed to the terminal. Total votes cast for each candidate and total votes cast in each of the counties are shown, as well as percentages of these rounded to two decimal places for better accuracy.

<img width="418" alt="Screen Shot 2021-07-18 at 10 48 45 AM" src="https://user-images.githubusercontent.com/86446641/126071721-29f9d8fc-f34c-4b6f-b5e1-9ff9c5408542.png">

it is shown that:
- total votes cast =369,711
- 3 different candidates received votes
- number and percentage of votes cast to each candidate is shown next to their names
- winner of the election based on popular vote is Diana DeGette
- voter turnout for each county is shown in parenthesis to the right of percentage of votes from each county
- And Lastly,  the county with the highest voter turnout is Denver County (82.78% of total votes, 306,055 votes)

## Election Audit Summary

It is important to point out that this script may be run for any similar election given we have a csv file of the same format. 
<img width="505" alt="Screen Shot 2021-07-18 at 11 04 45 AM" src="https://user-images.githubusercontent.com/86446641/126072193-ccfae08c-59d2-4d39-8972-f3f8a5af0ef2.png">

the first step in using this script for another election would be to import a new csv file in the file_to_load shown above. 

Above you can also see that we initialize candidate and county options/votes as empty lists and dictionaries. This is necessary so that we may easily add to these later in the script. If there were 6 candidates and 4 counties (or any arbitrary numbers) the lists/dictionaries would be appended correctly using the code snippit shown below. 

<img width="342" alt="Screen Shot 2021-07-18 at 11 02 24 AM" src="https://user-images.githubusercontent.com/86446641/126072131-5913b403-98cb-4c13-b4d2-59071ff9993a.png">

these if statements exist within a for-loop which reads each row of the data for all candidates and counties present (and summing total votes cast).

<img width="449" alt="Screen Shot 2021-07-18 at 11 10 37 AM" src="https://user-images.githubusercontent.com/86446641/126072378-1acbbdd1-eb6a-4d69-9cdf-80896d01933c.png">

Other pertinent portions of the code are for-loops of similar structure which count and print votes and vote percentages for each candidata/county present in the data file. The snippit of code pertaining to the candidate results is shown and commented on below for your convenience.

<img width="648" alt="Screen Shot 2021-07-18 at 11 12 40 AM" src="https://user-images.githubusercontent.com/86446641/126072422-abd36484-24d6-4edd-86b1-62a7835f0160.png">

Thanks! Hope that this audit has been sufficient and analysis thorough.

