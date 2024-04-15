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
    
# Create block for AVERAGE CHANGE
def calc_average_change(csvreader):
    differences = [ ]
    prev_value = None
    for row_lp in csvreader:
        if csvreader.line_num == 1:
            continue
        try: value = float(row_lp[1])
        except ValueError:
            continue
        if prev_value is not None:
            difference = value - prev_value
            differences.append(difference)
        prev_value = value
    average_change = sum(differences) / len(differences)
    return average_change

# Use the def block with open command 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    next(csvreader)
    total_months_count = total_months(csvreader)

    csvfile.seek(0)
    next(csvreader)
    total_profit, total_loss = net_profitloss(csvreader)
    net_total = total_profit + total_loss

    csvfile.seek(0)
    average_change = calc_average_change(csvreader)

# PRINT STATION
print(f'Total Months: {total_months_count}')
# print(f'Total Profit: {total_profit}')
# print(f'Total Loss: {total_loss}')
print(f'Net Total: ${net_total}')
average_change_form = round(average_change, 2)
print(f'Average Change: ${average_change_form}')

