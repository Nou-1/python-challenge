import os
import csv

csv_path = os.path.join("Resources", "budget_data.csv")


with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)

    total_months = []   
    total_profit = []
    monthly_change = []
    

    for row in csv_reader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    
    for i in range(len(total_profit)-1):
        monthly_change.append(total_profit[i+1]-total_profit[i])
    
        greatest_increase = max(monthly_change)
        month_increase = total_months[monthly_change.index(max(monthly_change)) + 1]

        greatest_decrease = min(monthly_change)
        month_decrease = total_months[monthly_change.index(min(monthly_change)) + 1]

   

    print("Financial Analysis")
    print("....................")
    print(f"Total Months: {len(total_months)}")
    print(f"Total: {sum(total_profit)}")
    print(f"Average Change: {round(sum(monthly_change)/len(monthly_change), 2)}")
    print(f"Greatest Increase in Profits: {month_increase} (${(greatest_increase)})")
    print(f"Greatest Decrease in Profits: {month_decrease} (${(greatest_decrease)})")


output_path = os.path.join("Analysis", "Results.txt")

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

    