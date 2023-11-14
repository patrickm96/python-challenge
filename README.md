# python-challenge
Module 3

The following resources were referenced in order to complete this challenge:
1. Find difference value 1 and value 2 (numpy.diff) - https://stackoverflow.com/questions/13602170/how-do-i-find-the-difference-between-two-values-without-knowing-which-is-larger
2. Calculate mean/average of list values - https://www.geeksforgeeks.org/numpy-mean-in-python/#
3. Python round number function - https://www.programiz.com/python-programming/methods/built-in/round
4. Return value based on position in list - https://www.tutorialspoint.com/How-to-get-the-second-to-last-element-of-a-list-in-Python
5. Convert array return value to list value - https://stackoverflow.com/questions/49882068/convert-np-where-array-to-list
6. Return list index/position based on maximum. minimum and specific value in list - https://stackoverflow.com/questions/27260811/python-find-position-of-element-in-array
7. Convert number calculation to percentage format - https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-36.php
8. Identify unique values in a list - https://www.geeksforgeeks.org/python-get-unique-values-list/#
9. If statements in for loops - Eli Rosenberg (Instructor) covered this during class.
10. Read & write input/output files - Eli Rosenberg (Instructor) covered this during class.

PyBank Instructions
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period

Your analysis should align with the following results:

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
In addition, your final script should both print the analysis to the terminal and export a text file with the results.

PyPoll Instructions
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote

Your analysis should align with the following results:

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
In addition, your final script should both print the analysis to the terminal and export a text file with the results.
