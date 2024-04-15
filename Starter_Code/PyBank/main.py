# Import os module
import os
import csv

# Create csvpath
csvpath = os.path.join('..', 'Resources','budget_data.csv')

# Create block for TOTAL MONTHS
def total_months(csvreader):
    month_count = 0
    for row_lp in csvreader:
        month_count += 1
    return month_count

# Create block for NET PROFIT
def net_profitloss(csvreader):
    profit = 0
    loss = 0 
    for row_lp in csvreader:
        value = int(row_lp[1])
        if value > 0:
            profit += value
        else:
            loss += value
    return profit, loss
    
# Use the def block 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    next(csvreader)
    total_months_count = total_months(csvreader)

    csvfile.seek(0)
    next(csvreader)
    total_profit, total_loss = net_profitloss(csvreader)
    net_total = total_profit + total_loss

# PRINT STATION
print(f'Total Months: {total_months_count}')
# print(f'Total Profit: {total_profit}')
# print(f'Total Loss: {total_loss}')
print(f'Net Total: ${net_total}')

