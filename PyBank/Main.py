import os
import csv
#path=os.getcwd()
budget_path=os.path.join("/Users/zahra/Bootcamp/python-challenge/PyBank","Resources", "budget_data.csv")
#print(budget_path)

with open (budget_path,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    total=0
    month=0
    # Read the header row first
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    #Read rows and find months and total
    for row in csvreader:
        #print (row)
        #date=print(row[0])
        #val=print(float(row[1]))
        total+=float(row[1])
        month+=1

    
    print("Financial Analysis")
    print("=======================================================")
    print(f"Total Months : {month} ")
    print(f"Total : {total}")