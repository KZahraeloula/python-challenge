# python-challenge
# By Bank Challenge
# location of the code within the reposetory
The code is in PyBank/Main.py
# Description of the project
This is a financial analysis where there is data of Profit/loss by month, Using Python language to import modules as (os and csv) to access the CSV file located in PyBank/Ressources and has an output of printing the analysis either in the console and generating a text file named result located in PyBank/analysis

# Explanation of code 
the main idea is to read the CSV file and  create a list of months and a list of profit_losses (listprofit_losses), during that process (loop) we increment a counter in order to find the number of months (months)and we add up the value to find the Total amount of profit_losses

In order to find the changes in profit-losses and the average, I will create a new list called revenue_change, wher we store the differences of change after reading the listprofit_losses list created above.
once I have the list completed, I will calculate the average of change, max and min values and print in the terminal

Writing in the output text file 
I will use the CSV module to create/access the file resuls in PyBank/analysis and write using the command "file.write" 

# --------------------------------------------------------------------------------------------------------------------
# Py Poll Challenge
# location of the code within the reposetory
The code is in PyPoll/Main.py
# Description of the project
This is an analysis of votes where there is data of number of voters and candidate they vote for, Using Python language to import modules as (os and csv) to access the CSV file located in PyPoll/Ressources and has an output of printing the vote analysis either in the console and generating a text file named result located in PyPoll/analysis

# Explanation of code 
The idea of the code is to creat a dictionnary that holds the candidate name and the number of votes that each one got
using csv reader and a loop.
I can have the max number fron that dictionnary and find out the key for that number so I get tha name of the winner 
Writing in the output text file 
I will use the CSV module to create/access the file resuls in PyBank/analysis and write using the command "file.write"