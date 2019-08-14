import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

months = []
total = 0
profit_loss = []
inc_profit = []


with open (csvpath , newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(float(row[1]))
        total = total + int(row[1])

    for i in range ( 1,len(profit_loss)):
        inc_profit.append(profit_loss[i]-profit_loss[i-1])

    avg_change = round(sum(inc_profit)/len(profit_loss),2)
    max_profit = max(inc_profit)
    min_loss = min(inc_profit)

    for i in range(len(inc_profit)):
        if inc_profit[i] == max_profit:
            max = i + 1
        if inc_profit[i] == min_loss:
            min = i + 1

    print("```text")
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: "+ str(len(months)))
    print("Total: $" + str(total))
    print("Average Change $" + str(avg_change))
    print("The greatest increase in Profits: "+ months[max] + " ($" + str(max_profit) + ")")
    print("The greatest decrease in Profits: "+ months[min] + " ($" + str(min_loss) + ")")
    print("```")
    
        