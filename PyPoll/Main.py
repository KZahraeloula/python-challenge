import os       #import os module
import csv      #import csv module
path=os.path.join("/Users/zahra/Bootcamp/python-challenge/PyPoll","Resources","election_data.csv") # set a variable that holds the path of csv file
number_votes=0      #set a variable to get the total number of votes
with open(path, mode='r') as pollfile:      # open the csv file on reading mode 
    summary_vote={}                         #set a dictionnariy summary_vote to hold 
    candidate=""                            #a string variable for candidate name
    csv_reader=csv.reader(pollfile)         #Accessing the csv file in reading mode
    csv_header=next(csv_reader)             #skipping the header
    #build dictiannary of candidate and number of votes 
    for row in csv_reader:   #loop to read the CSV
        number_votes+=1     #count the number of voter
        candidate=row[2] #Initializing candidate variable
        #loop to buile the dictiannary with name of candidate and how many time ot appears
        if candidate in summary_vote:     # if the candidate is already added in the dict ,
            summary_vote[candidate]+=1    #incremant the value by 1
        else:                             #if it doesn't exist 
            summary_vote[candidate]=1     #set the value at 1
    print("Election Results")             #print
    print("--------------------------------------------------------------")
    print(f"Total Votes {number_votes}") #print the total number of voters
    
    for candidate in summary_vote:      #loop into the dict to print candidate names,percentage of vote for each one and number of votes too
        print(candidate , "{:0.000%}".format((summary_vote[candidate]/number_votes)), " (" ,summary_vote[candidate],")")   
        

    max_value = max(summary_vote.values())          # find the max value of number of votes
    print("--------------------------------------------------------------")
    for candidate in summary_vote:                  #loop to find the key in the dictionary that has the max value of votes
        if summary_vote[candidate] == max_value:    #when the value read in the loop =the max_value fuound im line 27
            print ("Winner : "+candidate)           #print the correspandante name of candidate
            
       # write in the output file
    outputpath= os.path.join ("/Users/zahra/Bootcamp/python-challenge/PyPoll/analysis","Result.txt") # define the output path and output file name and extension in "outputpath" variable
    result=open(outputpath,"w")   #open the result txt file in writing mode
    result.write("Election Results "+"\n")    # print and return to the line 
    result.write("--------------------------------------------------------------"+"\n")
    for candidate in summary_vote:      #loop into the dict to print candidate names,percentage of vote for each one and number of votes too
        result.write(candidate +" "+ str("{:0.000%}".format((summary_vote[candidate]/number_votes))) + " (" + str(summary_vote[candidate])+")" + "\n")#write the names , percentge and count of vote by candidate
    result.write("--------------------------------------------------------------"+"\n") #write
    for candidate in summary_vote:                  #loop to find the key in the dictionary that has the max value of votes
        if summary_vote[candidate] == max_value:    #loop into the summary_vote dioctionnary to find the key of the max_value
            result.write("The Winner is :"+ candidate )        