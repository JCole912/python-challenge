#locating csv file
file = open("./Resources/election_data.csv", "r")
next(file)
#defining variables
count=0
vote={}
#tallying up the votes via for loop
for line in file:
    count=count+1
    line=line.strip()
    line=line.split(",")
    #defining canddiate names, who are in column 3
    candidate=line[2]
    #tallying all candidate votes
    if candidate in vote:
        vote[candidate]=vote[candidate]+1
    else:
        vote[candidate]=1
print("Election Results")
print("---------------")
print("Total Votes:",count)
print("---------------")
max_votes_candidate=""
max_votes_number=0
#calculating the electoral winner via for loop
for candidate in vote:
    print(f"{candidate} {100*vote[candidate]/count:.2f}% ({vote[candidate]})")
    if vote[candidate]>max_votes_number:
        max_votes_number = vote[candidate]
        max_votes_candidate=candidate
print("---------------")
print("Winner:", max_votes_candidate)
print("---------------")