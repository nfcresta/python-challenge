#Import Modulse
import os
import csv

# create path for csv to read from
csvpath = os.path.join("Resources", "budget_data.csv")

# create empty lists
totalMonths = []
totalPL = []
monthlyChange = []

# Open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Print first title of analysis
    print("Financial Analysis")
    print('-------------------------------')

    # iterate through rows
    for row in csvreader:

        # calculate total nuber of months included in the dataset
        totalMonths.append(row[0])
    
        # calculate total Profit/Losses to find the average change
        totalPL.append(int(row[1]))

    # get monthly change in profits
    for c in range(len(totalPL) - 1):
        
        # find difference between months and append to the monthlyChange
        monthlyChange.append(totalPL[c+1] - totalPL[c])

# get maximum and minimum change
max_increase = max(monthlyChange)
max_decrease = min(monthlyChange)

# get maximum and minimum change (use plus one at the end of formula to get the actual month where change occurred)
greatest_increase_M = monthlyChange.index(max(monthlyChange)) + 1
greatest_decrease_M = monthlyChange.index(min(monthlyChange)) + 1

# print results in terminal
print(f'Total Months: {len(totalMonths)}')
print(f'Total: ${sum(totalPL)}')
print(f'Average Change: ${round(sum(monthlyChange)/len(monthlyChange), 2)}')
print(f'Greatest Increase in profits: {totalMonths[greatest_increase_M]} (${str(max_increase)})')
print(f'Greatest Decrease in profits: {totalMonths[greatest_decrease_M]} (${(str(max_decrease))})')


# Export a txt file with the results
output_path = os.path.join("analysis", "financial_analysis.txt")

# open output file and write
with open(output_path, "w") as file:
    file.write('Financial Analysis')
    file.write('\n')
    file.write('--------------------------------')
    file.write('\n')
    file.write(f'Total Months: {len(totalMonths)}')
    file.write('\n')
    file.write(f'Total: ${sum(totalPL)}')
    file.write('\n')
    file.write(f'Average Change: ${round(sum(monthlyChange)/len(monthlyChange),2)}')
    file.write('\n')
    file.write(f'Greatest Increase in Profits: {totalMonths[greatest_increase_M]} (${(str(max_increase))})')
    file.write('\n')
    file.write(f'Greatest Decrease in Profits: {totalMonths[greatest_decrease_M]} (${(str(max_decrease))})')
