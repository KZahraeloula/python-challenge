import os  #import os moldule
import csv #import csv module
budget_path=os.path.join("/Users/zahra/Bootcamp/python-challenge/PyBank","Resources", "budget_data.csv") # set a variable that holds the path of csv file
with open (budget_path,'r') as csvfile:  # open the csv file in a reding mode
    csvreader = csv.reader(csvfile)      # set up a csv reader variable
    total=0                              #holds the total amount of profit/losses
    month=0                              #holds the total number of months
    csv_header = next(csvfile)           # skip the header row first
    #Read rows and find months and total and add them in lists
    listprofit_losses=[]                 #create an empty list to hold the profit and losses 
    months=[]                            #create an empty list to hold the months
    #g_profit_increase==0, g_profit_decrease==0 
    for row in csvreader:                #create a loop fto read rows in the csv
        total+=float(row[1])             # add the value of profit and losses into the total variable
        month+=1                         #increment the variable month to have the total month at the end of the loop
        listprofit_losses.append(int(row[1]))  # add values of profit/losse in the listprofit_losses
        months.append(row[0])                   #add months into the months list, I will use that list to find the months correspondant to the gratest amount increase/decrease
    revenue_change = []                  #create an empty list to store the revenue change

    for x in range(1, len(listprofit_losses)):       # loop for revenue change, start at the second value to be able to do the dif between the first two values
        revenue_change.append((int(listprofit_losses[x]) - int(listprofit_losses[x-1]))) # add the different of value between the value X and X-1 witch is the previous one
     
    revenue_average = sum(revenue_change) / len(revenue_change)  # calculate average revenue change
    g_profit_increase=max(revenue_change)                        #find the greatest value in the revenue_change list
    g_profit_decrease=min(revenue_change)                        #find the smallest value in the revenue_change list


    # Print the results
    print("Financial Analysis")
    print("=======================================================")
    print(f"Total Months : {month} ")
    print(f"Total : {total}")
    print(f"The average revenue change {revenue_average} ")
    # print the greates increase with the correspondant amount using index to bring the value that has that index in the months list (+1 because we have 1 less in the revenue change beacause of the difference) 
    print(f"The Greatest revenue increase " + str(months[revenue_change.index(max(revenue_change))+1])+"  " +str(g_profit_increase) )
 # print the greates decrease with the correspondant amount using index to bring the value that has that index in the months list (+1 because we have 1 less in the revenue change beacause of the difference) 
    print(f"The Greatest revenue decrease "+ str(months[revenue_change.index(min(revenue_change))+1])+"  " + str(g_profit_decrease))

    # write in the output test
    outputpath= os.path.join ("/Users/zahra/Bootcamp/python-challenge/PyBank/analysis","Result.txt") # define the output path and output file name and extension in outputpath variable
    result=open(outputpath,"w")   #open the result txt file in writing mode
    result.write("Financial Analysis"+"\n")    # print and return to the line 
    result.write("--------------------------------------------------------------"+"\n")
    result.write ("The total number of months "+ str(month)+"\n")
    result.write ("The net total amount of Profit/Losses  "+ str(total)+"\n")
    result.write ("The average changes in Profit/Losses "  + str(revenue_average)+"\n")
     # print the greatest increase/decrease with the correspondant amoant using index to bring the value that has that index in the months list (+1 because we have 1 less in the revenue change beacause of the difference) 
    result.write ("The greatest increase in profits "+ str(months[revenue_change.index(max(revenue_change))+1])+ " " +str(g_profit_increase)+"\n")
    result.write ("The greatest decrease in profits "+ str(months[revenue_change.index(min(revenue_change))+1])+" "+ str(g_profit_decrease)+ "\n")