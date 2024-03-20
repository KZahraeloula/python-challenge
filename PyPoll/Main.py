import os
import csv
path=os.path.join("/Users/zahra/Bootcamp/python-challenge/PyPoll","Resources","election_data.csv")
print (path)
number_votes=0
with open(path, mode='r') as pollfile:
    summary_vote={}
    candidate=""
    #reading the rows
    csv_reader=csv.reader(pollfile)
    #skipping the header
    next(csv_reader,None)
    #build dictiannary of candidate and number of votes
   
    #loop to read the CSV
    for row in csv_reader:
        #count the number of voter
        number_votes+=1
        candidate=row[2] #Initializing candidate
        #loop to buile the dictiannary with name of candidate and number of occurance 
        if candidate in summary_vote:
            summary_vote[candidate]+=1
        else: 
            summary_vote[candidate]=1
        
    print(f"the number of voters {number_votes}")
    for candidate in summary_vote:
        print(candidate , "{:0.000%}".format((summary_vote[candidate]/number_votes)), " (" ,summary_vote[candidate],")")   

    #max_value = max(zip(summary_vote.keys(),summary_vote.values()))
    #max_value = max(zip(summary_vote.values(),summary_vote.keys()))
    max_value = max(summary_vote.values())
    print (max_value)
    #Keymax = max( summary_vote.keys())
    #print(Keymax)
    
