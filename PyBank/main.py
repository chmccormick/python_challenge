# Import Modules 
import os 
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open CVS file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Create empty list that will store CSV data
    date = []
    profit = []
    
    # Add CSV data to respective lists
    for row in csvreader:
        date.append(row[0])
        profit.append(int(row[1]))

    # Answer to Question 1
    total_months = len(date)
    # Answer to Question 2
    net_total = sum(profit)
    change = []
    # Answer to Question 3
    for i in range(1,len(profit)):
        change.append(profit[i]-profit[i-1])

    average = (round(sum(change)/len(change),2))
    
    # Answer to Questions 4 & 5
    great_inc = max(change)
    increase_index = change.index(great_inc)

    great_dec = min(change)
    decrease_index = change.index(great_dec)

# Strings to be written to txt file
str1 = "Financial Analysis\n"
str2 = (f"Total Months: {total_months}\n")
str3 = (f"Total: ${net_total}\n")
str4 = (f"Average Change: ${average}\n")
str5 = (f"Greatest Increase in profits: {increase_index} (${great_inc})\n")
str6 = (f"Greatest Decrease in profits: {decrease_index} (${great_dec})\n")



# Open new text file in 'analysis' foler and write to it.
with open('analysis/output.txt', "w") as file:
    file.write(str1)
    file.write("---------------------------------\n")
    file.write(str2)
    file.write(str3)
    file.write(str4)
    file.write(str5)
    file.write(str6)

# Printed Results to terminal. 
print("Financial Analysis")
print("-" *20)
print(f"Total Months: {total_months}")
print(f"Toatl: ${net_total}")
print(f"Average change: ${average}")
print(f"Greatest Increase in profits: {increase_index} (${great_inc})")
print(f"Greatest Decrease in profits: {decrease_index} (${great_dec})")