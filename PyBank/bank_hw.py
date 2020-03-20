import os
import csv

# directory path
dir_path = os.path.dirname(os.path.realpath(__file__))

bank_data = os.path.join("budget_data.csv")


#open csv
with open(bank_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header
    next(csvreader, None)
    date = []
    
    profit_losses = []
    sum_profit_losses = 0 
    revenue_change = []
      

    #total months and sum of profit/losses:
    for row in csvreader:
        date.append(row[0])
        profit_losses.append(float(row[1]))
        sum_profit_losses += int(row[1])
       
    for i in range(1,len(profit_losses)):
        revenue_change.append(profit_losses[i] - profit_losses[i-1])   
        
        avg_rev_change = sum(revenue_change)/len(revenue_change)

        max_rev_change = max(revenue_change)

        min_rev_change = min(revenue_change)

        max_rev_change_date = str(date[revenue_change.index(max(revenue_change))])
        min_rev_change_date = str(date[revenue_change.index(min(revenue_change))])
        
    total_months = len(date)


print("Financial Analysis")
print("----------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${sum_profit_losses}')
print(avg_rev_change)
print(max_rev_change_date, max_rev_change)
print(min_rev_change_date, min_rev_change)