#importing dependencies
import os
import csv

#path to open data from the Resources folder
csv_path = os.path.join("Resources", "election_data.csv")

#open csv
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

    #create empty lists and counters to store variables
    total_votes = []
    candidates = []
    khan_votes = 0
    o_tooley_votes = 0
    correy_votes = 0
    li_votes = 0


    #loop through rows
    for row in csv_reader:
        #append relevant rows to lists
        total_votes.append(row[0])
        candidates.append(row[2])

 
        #if conditions to calculate the votes each candidates obtained
        if row[2] == "Khan":
            khan_votes +=1
        elif row[2] == "O'Tooley":
            o_tooley_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li":
            li_votes +=1
        
        #percentage votes per candidates
        percent_khan = (khan_votes/(len(total_votes))) * 100
        percent_o_tooley = (o_tooley_votes/len(total_votes)) * 100
        percent_correy = (correy_votes/len(total_votes)) * 100
        percent_li = (li_votes/len(total_votes)) * 100

    #using set function to obtain unique values
    unique_candidates = list(set(candidates))

    #create a list of candidates and votes
    candidate = ["Khan", "Li", "Correy", "O'Tooley"]
    votes = [khan_votes, li_votes, correy_votes, o_tooley_votes]

    #create a dictionary of unique candidates and corresponding votes to obtain max votes
    candidates_votes = dict(zip(candidate, votes))

    #key.get function to obtain max value from a dictionary
    winner = max(candidates_votes, key=candidates_votes.get)

    #printing results to terminal
    print("Election Results")
    print("------------------")
    print(f"Total votes: {len(total_votes)}")
    print("------------------")
    print(f"Khan: {percent_khan:.3f}% ({khan_votes})")
    print(f"Correy: {percent_correy:.3f}% ({correy_votes})")
    print(f"Li: {percent_li:.3f}% ({li_votes})")
    print(f"O'Tooley: {percent_o_tooley:.3f}% ({o_tooley_votes})")
    print("------------------")
    print(winner)
    print("------------------")

#creating output files
output_path = os.path.join("Analysis", "Results.txt")

#exporting results to text files
with open(output_path, 'w') as textfile:
    textfile.write("Election Results")
    textfile.write("\n")
    textfile.write("------------------")
    textfile.write("\n")
    textfile.write(f"Total votes: {len(total_votes)}")
    textfile.write("\n")
    textfile.write("------------------")
    textfile.write("\n")
    textfile.write(f"Khan: {percent_khan:.3f}% ({khan_votes})")
    textfile.write("\n")
    textfile.write(f"Correy: {percent_correy:.3f}% ({correy_votes})")
    textfile.write("\n")
    textfile.write(f"Li: {percent_li:.3f}% ({li_votes})")
    textfile.write("\n")
    textfile.write(f"O'Tooley: {percent_o_tooley:.3f}% ({o_tooley_votes})")
    textfile.write("\n")
    textfile.write("------------------")
    textfile.write("\n")
    textfile.write(winner)
    textfile.write("\n")
    textfile.write("------------------")

