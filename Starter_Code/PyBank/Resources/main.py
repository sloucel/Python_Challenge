#Financial Analysis
## Import os module
import os
import csv

## Create csvpath
csvpath = os.path.join('..', 'Resources','budget_data.csv')

## Create block to calculate the the TOTAL MONTHS
def total_months(csvreader):
    month_count = 0
    for row_lp in csvreader:
        month_count += 1
    return month_count

## Create block to calculate the NET PROFIT
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

## Create block for AVERAGE CHANGE
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

## Create block for MIN MAX CHANGE
def calc_max_min_change(csvreader):
    max_change = None
    min_change = None
    max_change_date = None
    min_change_date = None
    prev_value = None
    prev_date = None

    next(csvreader)  # Skip header row
    
    for row_lp in csvreader:
        date = row_lp[0]
        value = float(row_lp[1])
        if prev_value is not None:
            change = value - prev_value
            if max_change is None or change> max_change:
                max_change = change
                max_change_date = date
            if min_change is None or change < min_change:
                min_change = change
                min_change_date = date
        prev_value = value
        prev_date = date
    return max_change, max_change_date, min_change, min_change_date

## Open file and use define function blocks from above. 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    next(csvreader)
    total_months_count = total_months(csvreader)

    csvfile.seek(0)
    next(csvreader)
    total_profit, total_loss = net_profitloss(csvreader)
    net_total = total_profit + total_loss

    csvfile.seek(0)
    next(csvreader)
    average_change = calc_average_change(csvreader)

    csvfile.seek(0)
    max_increase, max_increase_date, min_decrease, min_decrease_date = calc_max_min_change(csvreader)


## PRINT STATION
print("Financial Analysis")
print("------------------------------------")
print(f'Total Months: {total_months_count}')
##### print(f'Total Profit: {total_profit}')
##### print(f'Total Loss: {total_loss}')
print(f'Net Total: ${net_total}')
average_change_form = round(average_change, 2)
print(f'Average Change: ${average_change_form}')
max_increase_form = int(max_increase)
print(f'Greatest Increase in Profits: {max_increase_date} (${max_increase_form})')
min_decrease_form = int(min_decrease)
print(f'Greatest Decrease in Profits: {min_decrease_date} (${min_decrease_form})')

## Export results to a new csv file and place in the the Analysis Folder
### Output_path
output_path = os.path.join("..", 'Analysis', 'financial_analysis.txt')

with open(output_path, "w") as txtfile:
    txtfile.write('Total Months: {}\n'.format(total_months_count))
    txtfile.write('Net Total: {}\n'.format(net_total))
    txtfile.write('Average Change: {}\n'.format(average_change))
    txtfile.write('Greatest Increase Date: {}\n'.format(max_increase_date))
    txtfile.write('Greatest Increase Amount: {}\n'.format(max_increase))
    txtfile.write('Greatest Decrease Date: {}\n'.format(min_decrease_date))
    txtfile.write('Greatest Decrease Amount: {}\n'.format(min_decrease))

print("Data has been written to", output_path)
