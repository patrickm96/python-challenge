#Import modules
import os
import csv
import numpy as np
from statistics import mean

#Path to .csv file
csvpath = os.path.join('.', 'PyBank', 'Resources','budget_data.csv')

#List for month and year
month_year = []
#List for profit/loss for each month and year
profit_loss= []
#First monthly change value is 0 as there is no previous month/value
monthly_change = [0]

#Open .csv file
with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    #Skip .csv file header
    csv_header = next(csvreader)

    for row in csvreader:
        #Populate lists
        month_year.append(row[0])
        profit_loss.append(int(row[1]))
        #Calculate number of rows
        total_months = len(month_year)
        #Calculate total of profit/loss column
        total_value = sum(profit_loss)

#Calculate difference in profit/loss from month-to-month
monthly_change_all = np.diff(profit_loss)
#Add month-to-month profit/loss differences to monthly_change list for average calculation
monthly_change = np.append(monthly_change, np.diff(profit_loss))
#Calculate index/position of maximum month-to-month profit/loss differences
max_change_index = np.where(monthly_change == max(monthly_change))[0][0]
#Convert max index/position to integer
max_change_integer = int(max_change_index)
#Return month-year from month_year list that is in the position of maximum number in monthly_change list
max_change_month = month_year[max_change_integer]
#Calculate index/position of minimum month-to-month profit/loss differences
min_change_index = np.where(monthly_change == min(monthly_change))[0][0]
#Convert min index/position to integer
min_change_integer = int(min_change_index)
#Return month-year from month_year list that is in the position of minimum number in monthly_change list
min_change_month = month_year[min_change_integer]

#Print results
print("Finanical Analysis")
print("-----------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_value}')
print(f'Average Change: ${round(np.mean(monthly_change_all),2)}')
print(f'Greatest Increase in Profits: {max_change_month} (${max(monthly_change)})')
print(f'Greatest Decrease in Profits: {min_change_month} (${min(monthly_change)})')

#Export to analysis folder as .txt file
output_path = os.path.join('.', 'PyBank', 'Analysis','pybank_results.txt')

#Write text file
with open(output_path, 'w') as txtfile:
    txtwriter = csv.writer(txtfile)
    txtwriter.writerow(['Financial Analysis'])
    txtwriter.writerow(['-----------------------------'])
    txtwriter.writerow([f'Total Months: {total_months}'])
    txtwriter.writerow([f'Total: ${total_value}'])
    txtwriter.writerow([f'Average Change: ${round(np.mean(monthly_change_all),2)}'])
    txtwriter.writerow([f'Greatest Increase in Profits: {max_change_month} (${max(monthly_change)})'])
    txtwriter.writerow([f'Greatest Decrease in Profits: {min_change_month} (${min(monthly_change)})'])
