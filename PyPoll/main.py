# Import Modules 
import os
import csv
import operator

# Set path for file 
csvpath = os.path.join("Resources", "election_data.csv")

# Open CSV file , skip header row
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Empty Dictionary to tally each candidate's votes
    results = {}

    # Loop through rows: If candidate name is in results dictionary, add 1 to corresponding value, 
    #   otherwise set corresponding value to 1
    for row in csvreader:
        candidate = row[2]
        if candidate in results.keys():
            results[candidate] += 1
        else:
            results[candidate] = 1

# Answer to question 1 
total_votes = sum(results.values())

# Answer to question 5
sorted_results = dict(sorted(results.items(), key= operator.itemgetter(1), reverse=True))
winner = list(sorted_results.keys())[0]

candidate_votes = []

for key,val in results.items():
    candidate_votes.append(f"{key}: {round((val/total_votes *100),3)}% ({val})\n")


with open ("analysis/output.txt", "w") as file:
    file.write("Election Results\n")
    file.write("--------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("--------------------------\n")
    for candidate in candidate_votes:
        file.write(candidate)
    file.write("\n")
    file.write("--------------------------\n")
    file.write(f"Winner: {winner}")   

print("Election Results")
print("-" *20)
print(f"Total Votes: {total_votes}")
print("-" *20)
for candidate in candidate_votes:
        print(candidate)
print("-" *20)
print(f"Winner: {winner}")