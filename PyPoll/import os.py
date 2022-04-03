import os
import csv

#path to open data from the Resources folder
csv_path = os.path.join("Resources", "election_data.csv")

#open csv
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

    total_votes = 0 
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

# Open csv in default read mode with context manager
    # Iterate through each row in the csv
    for row in csv_reader: 

        # Count the unique Voter ID's and store in variable  called total_votes
        total_votes +=1

        # We have four candidates if the name is found, count the times it appears and store in a list
        # We can use this values in our percent vote calculation in the print statements
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1