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
    #Read rows and find months and total and add them in lists
    listprofit_losses=[]
    months=[]
    #g_profit_increase==0, g_profit_decrease==0 
    for row in csvreader:
        #print (row)
        #date=print(row[0])
        #val=print(float(row[1]))
        total+=float(row[1])
        month+=1
        previous_amount=float(row[1])
        listprofit_losses.append(int(row[1]))
        months.append(row[0])
    revenue_change = []

    for x in range(1, len(listprofit_losses)):
        revenue_change.append((int(listprofit_losses[x]) - int(listprofit_losses[x-1])))
    
    # calculate average revenue change
    revenue_average = sum(revenue_change) / len(revenue_change)
    g_profit_increase=max(revenue_change)
    g_profit_decrease=min(revenue_change)


    # Print the results
    print("Financial Analysis")
    print("=======================================================")
    print(f"Total Months : {month} ")
    print(f"Total : {total}")
    print(f"The average revenue change {revenue_average} ")
    print(f"The Greatest revenue increase " + str(months[revenue_change.index(max(revenue_change))+1])+"  " +str(g_profit_increase) )
    print(f"The Greatest revenue decrease "+ str(months[revenue_change.index(min(revenue_change))+1])+"  " + str(g_profit_decrease))

    # write in the output test
    outputpath= os.path.join ("/Users/zahra/Bootcamp/python-challenge/PyBank/analysis","Result.txt")
    #print (outputpath)
    result=open(outputpath,"w")
    result.write("Financial Analysis"+"\n")
    result.write("--------------------------------------------------------------"+"\n")
    result.write ("The total number of months "+ str(month)+"\n")
    result.write ("The net total amount of Profit/Losses  "+ str(total)+"\n")
    result.write ("The average changes in Profit/Losses "  + str(revenue_average)+"\n")
    result.write ("The greatest increase in profits "+ str(months[revenue_change.index(max(revenue_change))+1])+ " " +str(g_profit_increase)+"\n")
    result.write ("The greatest decrease in profits "+ str(months[revenue_change.index(min(revenue_change))+1])+" "+ str(g_profit_decrease)+ "\n")