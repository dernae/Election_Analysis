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
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = 'c:/Users/shean/OneDrive/Documents/Analytics folder/Module_3_Python/Resources/election_results.csv'
# Assign a variable to save the file to a path.
file_to_save = 'c:/Users/shean/OneDrive/Documents/Analytics folder/Module_3_Python/Resources/analysis.txt'

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data) 
#gave errors
#for row in file_reader:

        #print(row)
    #ran fine
    headers = next(file_reader)
    print(headers)