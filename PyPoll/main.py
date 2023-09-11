
#I make sure it is cross operating system compatible
import os
import csv

# set path for file, looking at one folder up and finding csv file, and also making sure it is os compatible too
votescsv_path = os.path.join("resources", "election_data.csv")

#lists created to store data
list_candidates = []
candidates_who_received_votes = []
votes_total = []
votes_percent = []

#initialize variables
total = 0

#open and read csv, csv file has a comma delimiter, reading and skipping header
with open(votescsv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
            
    #loop through each row of data after the header
    for row in csvreader:
        #count and add total number of votes
        total = total + 1
        #add candidate names to list_candidates 
        list_candidates.append(row[2])
        #creating a list for candidates_who_received_votes
        #i is the candidates
    for i in set(list_candidates):
        candidates_who_received_votes.append(i)
        #v is for total number of votes for each candidate who received votes
        #v = list_candidates.total(i)
        #decided not to use v in percent for a clearer view of percent calculation
        votes_total.append(list_candidates.count(i))
        #percent is to calculcate the percentage of votes each candidate has won
        #also rounding with format
        percent = '{:.3f}'.format((list_candidates.count(i)/total)*100)
        votes_percent.append(str(percent) + "%") 
        
        total_winning_votes_count = max(votes_total)
        winner_candidate = candidates_who_received_votes[votes_total.index(total_winning_votes_count)]
        #to test print
        #print((total_winning_votes_count))
        #print((votes_percent))
#print
print("Election Results")
print("------------------------------------------------------------------------")
print("Total Votes: " + str(total))
print("------------------------------------------------------------------------")
for i in range(len(candidates_who_received_votes)):
    print(candidates_who_received_votes[i] + ": " + str(votes_percent[i]) + " (" + str(votes_total[i]) + ")")
print("------------------------------------------------------------------------")
print("Winner: " + winner_candidate) 
print("------------------------------------------------------------------------")

#writing analysis on a new text file
output_file = os.path.join("analysis", "PyPoll_Analysis.txt")
with open(output_file, "w") as text:

    text.write("Election Results" + "\n")
    text.write("----------------"+ "\n")
    text.write("Total Votes: "+ str(total) + "\n")
    text.write("---------------"+ "\n")
    for i in range(len(candidates_who_received_votes)):
        text.write(candidates_who_received_votes[i] + ": " + str(votes_percent[i]) + " (" + str(votes_total[i]) + ")" + "\n")
    text.write("---------------"+ "\n")
    text.write("Winner: " + winner_candidate + "\n")
    text.write("---------------"+ "\n")