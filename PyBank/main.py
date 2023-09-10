#locating csv file
file=open("./Resources/budget_data.csv", "r")
next(file)
#defining variables
count=0
total=0
sum_change_profit=0
greatest_increase_profit_amount=0
greatest_increase_profit_date=""
greatest_decrease_profit_amount=0
greatest_decrease_profit_date=""

for line in file:
    count=count+1
    line=line.strip()
    line=line.split(",")
    date=line[0]
    profit=line[1]
    profit=int(profit)
    #finding the net total amount of profit/losses
    if count>1:
        change_in_profit=profit-previous_profit
        sum_change_profit=sum_change_profit+change_in_profit
        #finding the greatest increase in profits
        if change_in_profit>greatest_increase_profit_amount:
            greatest_increase_profit_amount=change_in_profit
            greatest_increase_profit_date=date
            #finding the greatest decrease in profits
        if change_in_profit<greatest_decrease_profit_amount:
            greatest_decrease_profit_amount=change_in_profit
            greatest_decrease_profit_date=date
    total=total+profit
    previous_profit=profit
print("Financial Analysis")
print("---------------------")
print("Total Months:",count)
print("Total: ",total)
#calculating the avarage change
average=sum_change_profit/(count-1)
average=round(average,2)
print("Average Change: ",average)
print ("Greatest Increase in Profits: ",greatest_increase_profit_date, greatest_increase_profit_amount)
print ("Greatest Decrease in Profits: ",greatest_decrease_profit_date, greatest_decrease_profit_amount)