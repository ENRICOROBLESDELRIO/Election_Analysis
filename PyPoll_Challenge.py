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

# Initialize a total vote counter.
total_votes = 0

# Candidate Options - to create an empty list 
candidate_options = []

# Declare the empty dictionary to count the votes by each candidate. 
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

# Winning Candidate and Winning Count Tracker

# Declare a variable that holds an empty string value for the winning candidate.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
winning_county = ""
winning_count_county = 0
winning_percentage_county = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here /  # Read the file object with the reader function.
     file_reader = csv.reader(election_data)

    # Read the header row.
     headers = next(file_reader)
     
    # Print each row in the CSV file.
     for row in file_reader:

     # Add to the total vote count, or total_votes += 1
        total_votes = total_votes + 1

     # Print the candidate name from each row.
        candidate_name = row[2]

     # 3: Extract the county name from each row.
        county_name = row[1]

    # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1 

         # 4a: Write an if statement that checks that the
         # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)    

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0 

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

    # Save the results to our text file.
     with open(file_to_save, "w") as txt_file: 

            # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

     # 6a: Write a for loop to get the county from the county dictionary.
        for county_name in county_votes:

            # 6b: Retrieve the county vote count.
            votes_county = county_votes[county_name]

            # 6c: Calculate the percentage of votes for the county.
            votes_percentage_county = float(votes_county) / float(total_votes) * 100

            # 6d: Print the county results to the terminal.
            county_results = (
                 f"County Votes:\n"
                 f"{county_name}: {votes_percentage_county:.1f}% ({votes_county:,})\n")
            print(county_results)

            # 6e: Save the county votes to a text file.
            txt_file.write(county_results)

            # 6f: Write an if statement to determine the winning county and get its vote count.
            if (votes_county > winning_count_county):
                winning_count_county = votes_county
                winning_county = county_name

        # 7: Print the county with the largest turnout to the terminal.
        county_winner_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
        print(county_winner_summary)

        # 8: Save the county with the largest turnout to a text file.
        txt_file.write(county_winner_summary)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
        for candidate_name in candidate_votes:

            # Retrieve vote count of a candidate in a variable.
            votes = candidate_votes[candidate_name]

            # Calculate the percentage of votes.
            votes_percentage = float(votes) / float(total_votes) * 100 

            # Print the candidate name and percentage of votes.
            candidate_results = (f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n\n")

            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

            # Determine winning vote count and candidate
            # Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (votes_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent =
                # vote_percentage.   
                winning_count = votes 
                winning_percentage = votes_percentage
                # Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name

        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        print(winning_candidate_summary)  
        # Save the winning candidate's name to the text file.
        txt_file.write(winning_candidate_summary)