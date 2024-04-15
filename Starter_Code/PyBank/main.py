# Import os module
import os

# Import csv module
import csv

# Create csvpath
csvpath = os.path.join('..', 'Resources','budget_data.csv')

# Create block to calculate the the total number of months
def total_months(csvreader):
    month_count = 0
    for row_lp in csvreader:
        month_count += 1
    return month_count
    
# Use the def block 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    next(csvreader)
    total_months_count = total_months(csvreader)
