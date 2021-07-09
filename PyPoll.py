# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file, with the "w" mode we will write data to the file
# with open(file_to_save, "w") as txt_file:

# Write some data to the file.
    # txt_file.write("Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here /  # Read the file object with the reader function.
     file_reader = csv.reader(election_data)

      # Print each row in the CSV file.
      # for row in file_reader:
        #print(row[0])

      # Read and print the header row.
     headers = next(file_reader)
     print(headers)