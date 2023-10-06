# importing my file
import os
import csv

# setting the file path for my budget data csv file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# print my path to confirm. I comment this out so it is not part of my code
#print(budget_data_csv)


# set my variables 
totalMonths = 0
totalProfitLoss = 0
netChange = 0
change = 0
months = []
newnetChange = []

# I open the file for reading and store as csv
with open(budget_data_csv, "r") as csvFile:

    # create the reader object
    csvReader = csv.reader(csvFile, delimiter=",")

    # skip the header
    csvheader = next(csvReader)

    # using next to get the first row of data and then read first row
    first_row = next(csvReader)
    totalMonths += 1
    netChange = int(first_row[1])
    totalProfitLoss += int(first_row[1])
    
       
    # I loop through the rest of the rows
    for row in csvReader:
        #add 1 to the total months
        totalMonths += 1
        #add the profit loss to the total net change
        totalProfitLoss = totalProfitLoss + int(row[1])
        #calculate the new net change by taking the current profit loss - previous net change
        change = int(row[1]) - netChange
        
        # update the new net change and then add to the list of net changes
        netChange = int(row[1])
        newnetChange.append(change)
        
        
        #add current month to the list of monthly changes
        months.append(row[0])
               
        # calculating the average net change = total of netchanges / count of net changes (len)
    avg_Change = sum(newnetChange)/len(newnetChange)


# print results
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(totalMonths)}")
print(f"Total: ${str(totalProfitLoss)}")
print(f"Average Change: ${str(avg_Change)}")
print(f"Greatest Increase in Profits:") # I struggled to calcualte these changes for increase/decrease and couldn't figure it out
print(f"Greatest Decrease in Profits:")


# setting my output path to write the txt output
outputlocation = os.path.join("Analysis", "Financial_Analysis.txt")

with open(outputlocation, "w") as txtFile:
    txtFile.write("Financial Analysis\n")
    txtFile.write("---------------------\n")
    txtFile.write(f"Total Months: {str(totalMonths)}\n")
    txtFile.write(f"Total: ${str(totalProfitLoss)}\n")
    txtFile.write(f"Average Change: ${str(avg_Change)}\n")
    txtFile.write(f"Greatest Increase in Profits:\n")
    txtFile.write(f"Greatest Decrease in Profits:\n")

# in creating the output I needed to ask for assistance from AskBCS in order to have my txt file display the information on separate lines.
# they assisted me in figuring out the '\n' portion of my code to print on separate lines.




