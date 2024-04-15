# Import os module
import os

# Import csv module
import csv

# Create csvpath
csvpath = os.path.join('..', 'Resources','budget_data.csv')

# Use the def block 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    next(csvreader)
