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

    with open ("output.txt","w" ) as output:
        text1= "```text"+ "\n" +"Financial Analysis" +"\n" +"----------------------------"+ "\n"
        print(text1)
        output.write(text1)
        print("Total Months: "+ str(len(months)))
        output.write("Total Months: "+ str(len(months)) + "\n")
        print("Total: $" + str(total))
        output.write("Total: $" + str(total)+"\n")
        print("Average Change $" + str(avg_change))
        output.write("Average Change $" + str(avg_change)+"\n")
        print("The greatest increase in Profits: "+ months[max] + " ($" + str(max_profit) + ")")
        output.write("The greatest increase in Profits: "+ months[max] + " ($" + str(max_profit) + ")" +"\n")
        print("The greatest decrease in Profits: "+ months[min] + " ($" + str(min_loss) + ")")
        print("```")
        output.write("The greatest decrease in Profits: "+ months[min] + " ($" + str(min_loss) + ")" +"\n" +"```")
    
        