#Election Analysis using Python from entirety of Module 3 





#old way to open file 
# import csv 
#file_to_load = 'c:/Users/shean/OneDrive/Documents/Analytics folder/Module_3_Python/Resources/election_results.csv'
# Open the election results and read the file.
#election_data = open(file_to_load, 'r')


# Close the file.

#election_data.close()
# Open the election results and read the file
#with open(file_to_load) as election_data:

     # To perform analysis.
     #print(election_data)
#'
#new way to open files

#import csv
#import os

# Assign a variable for the file to load and the path.
   #Doesnt work :/
#file_to_load = os.path.join("Resources", "election_results.csv")

#works:)
#file_to_load = 'c:/Users/shean/OneDrive/Documents/Analytics folder/Module_3_Python/Resources/election_results.csv'

# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
    # print(election_data)

#'
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = 'c:/Users/shean/OneDrive/Documents/Analytics folder/Module_3_Python/Resources/analysis.txt'
# Using the open() function with the "w" mode we will write data to the file.
#with open(file_to_save, 'w') as txt_file

     # Write some data to the file.

#' 
# Add our dependencies.
#import csv
#import os
# Assign a variable to load a file from a path.
#file_to_load = 'c:/Users/shean/OneDrive/Documents/Analytics folder/Module_3_Python/Resources/election_results.csv'
# Assign a variable to save the file to a path.
#file_to_save = 'c:/Users/shean/OneDrive/Documents/Analytics folder/Module_3_Python/Resources/analysis.txt'

# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
 #   file_reader = csv.reader(election_data) 
#gave errors
#for row in file_reader:

        #print(row)
    #ran fine
  #  headers = next(file_reader)
   # print(headers)

#' to determine the total number of votes cast in the election

#import csv 
#import os

#Assigning a variable to load a file from a path 
#file_to_load = 'c:/Users/shean/OneDrive/Documents/Analytics folder/Module_3_Python/Resources/election_results.csv'
#Assiging a variable to save the file to a path 
#file_to_save = 'c:/Users/shean/OneDrive/Documents/Analytics folder/Module_3_Python/Resources/analysis.txt'

#initializing total vote count 
#total_votes = 0 

#Open results and read the file 
#with open(file_to_load) as election_data: 
    #file_reader = csv.reader(election_data) 

    #Reading the header row 
    #headers = next(file_reader) 

#Print each row in the file 
    #for row in file_reader: 
        #total_votes += 1 
#printing total votes 
#print (total_votes) 

#'  retrieve the names of the individual candidates in the election.

#import csv 

#Assigning a variable to load a file from a path 
#file_to_load = 'c:/Users/shean/OneDrive/Documents/Analytics folder/Module_3_Python/Resources/election_results.csv'
#Assiging a variable to save the file to a path 
#file_to_save = 'c:/Users/shean/OneDrive/Documents/Analytics folder/Module_3_Python/Resources/analysis.txt'

#initializing total vote count 
#total_votes = 0 

# Candidate Names
#candidate_options = ['Charles Casper Stockham', 'Diana DeGette']

#Open results and read the file 
#with open(file_to_load) as election_data: 
    #file_reader = csv.reader(election_data) 

    #Reading the header row 
    #headers = next(file_reader) 

#Print each row in the file 
    #for row in file_reader: 
        #total_votes += 1 

    # Print the candidate name from each row.
        #candidate_name = row[2]

# If the candidate does not match any existing candidate...
    #if candidate_name not in candidate_options:
# Add the candidate name to the candidate list.
        #candidate_options.append(candidate_name) 
# Print the candidate list.
#print(candidate_options)

#' to count the votes for each candidate

import csv 
from collections import Counter

#Assigning a variable to load a file from a path 
file_to_load = 'c:/Users/shean/OneDrive/Documents/Analytics folder/Module_3_Python/Resources/election_results.csv'
#Assiging a variable to save the file to a path 
file_to_save = 'c:/Users/shean/OneDrive/Documents/Analytics folder/Module_3_Python/Resources/analysis.txt'

#initializing total vote count 
total_votes = 0 

# Candidate Names
candidate_options = []

#Declaring the empty dictionary.
candidate_votes = {} 

#Open results and read the file 
with open(file_to_load) as election_data: 
    file_reader = csv.reader(election_data) 

    #Reading the header row 
    headers = next(file_reader) 

#Print each row in the file 
    for row in file_reader: 
        total_votes += 1 

    # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
        # To begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
         # Add a vote to that candidate's count.
    candidate_votes[candidate_name] +=1
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count and percentage.
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print each candidate, their voter count, and percentage to the
    # terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #counter = Counter(total_votes)
# Print the candidate vote dictionary.
#print(counter)
 # Determine winning vote count, winning percentage, and candidate.
    winning_count = votes
    winning_candidate = candidate_name
    winning_percentage = vote_percentage
    if (votes > winning_count) and (vote_percentage > winning_percentage):
      
# Print the winning candidates' results to the terminal.
        print(
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

#print(winning_candidate_summary)
