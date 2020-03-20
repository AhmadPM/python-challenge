import os
import csv
from collections import Counter


# set directory
dir_path = os.path.dirname(os.path.realpath(__file__))

# variable for input
poll_data = os.path.join("election_data.csv")

# vanirable for outpout

poll_final = os.path.join("final_count.txt")

# lists 
candidate_count = {}


with open(poll_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header
    next(csvreader, None)
    data = list(csvreader)
    total_votes = len(data)
    

    for row in data:
        if row[2] not in candidate_count:
            candidate_count[row[2]] = 0
        candidate_count[row[2]] = candidate_count[row[2]] + 1


final_list = [ {
            'Candidate' : row,
            'Vote Count': ( (candidate_count[row]) ), 
            'Percentage of Vote': round((candidate_count[row]/total_votes) * 100, 2) 
            } for row in candidate_count]

with open("final_count.txt", 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')


print("Election Results")
print("---------------------------")
print(f'Total Votes: {total_votes}')
print("---------------------------")
print(final_list)

  

# taking list of candidate values in v 
v = list(candidate_count.values()) 
  
# taking list of candidate keys in v 
k = list(candidate_count.keys()) 
print('Winner: ', k[v.index(max(v))])


