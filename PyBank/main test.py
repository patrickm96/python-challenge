import os
import csv
import numpy as np
from statistics import mean

csvpath = os.path.join('.','Resources','budget_data.csv')

month_year = []
profit_loss= []
first_month_change = []
monthly_change = np.array([])
monthly_change2 = np.array([])
#monthly_change2 = []
#month_year_count = 0

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

#monthly_change2 = np.diff(profit_loss)
first_month_change = np.append(first_month_change, np.diff(profit_loss))

print(first_month_change)

#print(f'{monthly_change}')
#print(month_year)
#print(profit_loss)
#print(monthly_change2)
#print(first_month_change)
#print(profit_loss[row])
max_change_index = np.where(first_month_change == max(first_month_change))[0][0]
print(month_year.index('Jan-10'))
print(max_change_index)
max_change_integer = int(max_change_index)
print(max_change_integer)
print(month_year[max_change_integer])
print(profit_loss[max_change_integer])
#print(month_year, monthly_change2)
#print(row[0])
#max_change_month = np.where(month_year.index == max_change_integer)
#print(max_change_month)
#print(int(max_change_index))
#print(f'{month_year[max_change_index]}')

print("Finanical Analysis")
print("-------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_value}')
#print(f'Average Change: ${round(np.mean(monthly_change2),2)}')
#print(f'{month_year}')
#print(max(monthly_change2))
#print(min(monthly_change2))

