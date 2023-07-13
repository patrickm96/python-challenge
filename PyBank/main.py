import os
import csv
import numpy as np
from statistics import mean

csvpath = os.path.join('.', 'PyBank', 'Resources','budget_data.csv')

month_year = []
profit_loss= []
#Change is 0 for first month/row as there is no previous month
monthly_change = [0]


with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #change = numpy.diff(profit_loss)

    for row in csvreader:
        month_year.append(row[0])
        profit_loss.append(int(row[1]))
        #monthly_change.append(numpy.diff(profit_loss))
        #first_month_change += 1
        #if first_month_change 
        total_months = len(month_year)
        total_value = sum(profit_loss)
        #monthly_change.append(profit_loss[row+1] - profit_loss[row])
        #monthly_change2 = np.diff(profit_loss)
        #avg_monthly_change = np.mean(monthly_change2)

monthly_change_all = np.diff(profit_loss)
monthly_change = np.append(monthly_change, np.diff(profit_loss))

#print(f'{monthly_change}')
#print(month_year)
#print(profit_loss)
#Test monthly change 
#print(monthly_change)
#print(first_month_change)
#print(profit_loss[row])
max_change_index = np.where(monthly_change == max(monthly_change))[0][0]
#print(month_year.index('Jan-10'))
#print(max_change_index)
max_change_integer = int(max_change_index)
max_change_month = month_year[max_change_integer]
#print(max_change_integer)
#print(max_change_month)

min_change_index = np.where(monthly_change == min(monthly_change))[0][0]
#print(month_year.index('Jan-10'))
#print(min_change_index)
min_change_integer = int(min_change_index)
min_change_month = month_year[min_change_integer]
#print(min_change_integer)
#print(min_change_month)

print("Finanical Analysis")
print("-----------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_value}')
print(f'Average Change: ${round(np.mean(monthly_change_all),2)}')
print(f'Greatest Increase in Profits: {max_change_month} (${max(monthly_change)})')
print(f'Greatest Decrease in Profits: {min_change_month} (${min(monthly_change)})')