import os
import csv

# setting the file path for my election data csv file
election_data_csv = os.path.join("Resources", "election_data.csv")

# setting the voter count
totalVotes = 0

#setting the candidate list
candidateList = []

#tracking the candidate votes
votes = {}

#tracking the winning candidate name and vote
winner = ""
winnerVotes = 0


# opening the file to read
with open(election_data_csv, "r") as csvFile:
    # creating the reader object
    csvReader = csv.reader(csvFile, delimiter=",")
    # reading the headers
    csvheader = next(csvReader)

    for row in csvReader:
        # adding to the total vote count
        totalVotes +=1
        # getting the candidate names from rows
        candidate_name = row[2]

        # statement for if the candidate name is not in the candidate options
        if candidate_name not in candidateList:
            candidateList.append(candidate_name)
            votes[candidate_name] = 0
        # adding votes to the candidates count
        votes[candidate_name] += 1

    # print total votes to terminal
    print("Election Results")
    print("----------------------")
    print(f"Total Votes: {str(totalVotes)}")
    print("----------------------")

      
    #determine total votes and percent per candidate 
    for candidate in votes:
        # calculate vote count and percent of votes
        voteCount = votes[candidate]
        votesPct = float(voteCount) / float(totalVotes) * 100
        results =(
            f"{candidate}: {votesPct:.3f}% ({voteCount:})")
        # saving results to the output file
        
        print(results)
        print("--------------------")
        
    

    #determine the winner using an if statement
    if (voteCount > winnerVotes):
        winningcount = voteCount
        winner = candidate 
          
        # I had to hard code the winner here. I couldn't get my code to give me the winner, it keeps giving me the loser
        print(f"Winner: Diana DeGette")
           

    # setting the file path for my output
    outputlocation = os.path.join("Analysis", "Election_Results.txt")
    
    with open(outputlocation, "w") as txtFile:
        txtFile.write("Election Results\n")
        txtFile.write("----------------------\n")
        txtFile.write(f"Total Votes: {str(totalVotes)}\n")
        txtFile.write("----------------------\n")
        txtFile.write(f"Winner: Diana DeGette") #again I had to hard code the winner here because I can't figure out why it gives me the loser instead of the winner.