#
# PyBank Homework solutions
# Nelson Lubinda
#-----
# Task at hand is to create a Python script that analyzes the records to calculate each of the following:

#     The total number of months included in the dataset.

#     The net total amount of Profit/Losses over the entire period.

#     The average of the changes in Profit/Losses over the entire period.

#     The greatest increase in profits (date and amount) over the entire period.

#     The greatest decrease in losses (date and amount) over the entire period.
#------

# Import the pathlib and csv libraries for reading csv files

import os
import csv
import pandas as pd
from pathlib import Path

# Set the path for the csv file input and output files

csvfile_in = Path("../resources/budget_data.csv")
textfile_out = Path("../analysis/budget_analysis100.txt")


# Create variables and initialize for calculations

month_counter = 0
total_revenue = 0
total_revenue_change = 0

# Open current CSV with read 'r' attribute and pass to csvreader
with open(csvfile_in, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        # Skip headers
        next(csvreader, None)

        # Get data from first line

        column = next(csvreader,None)
        max_month = column[0]
        min_month = column[0]

        # Float to two decimal places using (:.2f) as in {total_revenue:.2f}

        revenue = float(column[1])
        min_revenue = revenue
        max_revenue = revenue
        previous_revenue = revenue
        month_counter = 1
        total_revenue = float(column[1])
        total_revenue_change = 0

        # Read one column and line at a time
        for column in csvreader:

            # Increase counter for number of months in dataset
            month_counter = month_counter + 1

            revenue = float(column[1])

            # Add to sum of revenue for data set
            total_revenue = total_revenue + revenue

            # Find change in revenue between this month and last month
            revenue_change = revenue - previous_revenue

            # Sum change in revenue to net change in revenue for data set and retain total_revenue_change

            total_revenue_change = total_revenue_change + revenue_change

            # Determine if change in revenue is a max or min for data set and...
            # Check if change in revenue is greater  and retain max_revenue

            if revenue_change > max_revenue:
                max_month = column[0]
                max_revenue = revenue_change

            # Check if change is less and retain min_revenue

            if revenue_change < min_revenue:
                min_month = column[0]
                min_revenue = revenue_change

            # Set previous revenue
            previous_revenue = revenue

        # Final Computation for averages revenue and revenue delta
        average_revenue = total_revenue/month_counter
        average_revenue_change = total_revenue_change/(month_counter-1)

        # Round decimal and used the float in the out put using the (:.2f) as in {total_revenue:.2f}
        total_revenue = float(total_revenue)
        average_revenue_change = float(average_revenue_change)
        max_revenue = float(max_revenue)
        min_revenue = float(min_revenue)

        # Print analysis for visual output using the new line character \n for readability
        print(f"\n")
        print(f"Financial Analysis:")
        print("-------------------------------------------------------\n")
        print(f"Total Months: {month_counter}\n")
        print(f"Total Revenue: ${total_revenue:.2f}\n")
        print(f"Average Revenue Change: ${average_revenue_change:.2f}\n")
        print(f"Greatest Increase in Revenue: {max_month} ${max_revenue:.2f}\n")
        print(f"Greatest Decrease in Revenue: {min_month} ${min_revenue:.2f}")
        print("")



        # Open write file in write mode using 'w' sending data to the textfile_out path (../budget_analysis.txt").
        txtwriter = open(textfile_out, mode = 'w')

        # Print to write file using newline character \n to make the file pleasant to read
        txtwriter.write(f"\n")
        txtwriter.write(f"Financial Analysis:\n")
        txtwriter.write("-------------------------------------------------------\n")
        txtwriter.write(f"Total Months: {month_counter}\n\n")
        txtwriter.write(f"Total Revenue: ${total_revenue:.2f}\n\n")
        txtwriter.write(f"Average Revenue Change: ${average_revenue_change:.2f}\n\n")
        txtwriter.write(f"Greatest Increase in Revenue: {max_month} ${max_revenue:.2f}\n\n")
        txtwriter.write(f"Greatest Decrease in Revenue: {min_month} ${min_revenue:.2f}\n")
        txtwriter.write("")

        txtwriter.close()
