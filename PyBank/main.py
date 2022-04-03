#importing dependencies
import os
import csv

#path to open data from the Resources folder
csv_path = os.path.join("Resources", "budget_data.csv")

#open csv
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)

    #create empty lists to store variables
    total_months = []   
    total_profit = []
    monthly_change = []
    
    #loop through rows
    for row in csv_reader:
        #append relevant rows to lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    
    #calculation for monthly profit change
    for i in range(len(total_profit)-1):
        monthly_change.append(total_profit[i+1]-total_profit[i])

        #the max/mim increase of monthly profit change and the corresponding month that it occurred in
        greatest_increase = max(monthly_change)
        month_increase = total_months[monthly_change.index(max(monthly_change)) + 1]

        greatest_decrease = min(monthly_change)
        month_decrease = total_months[monthly_change.index(min(monthly_change)) + 1]

   
    #printing results to terminal
    print("Financial Analysis")
    print("------------------------")
    print(f"Total Months: {len(total_months)}")
    print(f"Total: {sum(total_profit)}")
    print(f"Average Change: {round(sum(monthly_change)/len(monthly_change), 2)}")
    print(f"Greatest Increase in Profits: {month_increase} (${(greatest_increase)})")
    print(f"Greatest Decrease in Profits: {month_decrease} (${(greatest_decrease)})")

#creating output files
output_path = os.path.join("Analysis", "Results.txt")

#exporting results to text files
with open(output_path, 'w') as textfile:
    textfile.write("Financial Analysis")
    textfile.write("\n")
    textfile.write("....................")
    textfile.write("\n")
    textfile.write(f"Total Months: {len(total_months)}")
    textfile.write("\n")
    textfile.write(f"Total: {sum(total_profit)}")
    textfile.write("\n")
    textfile.write(f"Average Change: {round(sum(monthly_change)/len(monthly_change), 2)}")
    textfile.write("\n")
    textfile.write(f"Greatest Increase in Profits: {month_increase} (${(greatest_increase)})")
    textfile.write("\n")
    textfile.write(f"Greatest Decrease in Profits: {month_decrease} (${(greatest_decrease)})")

    