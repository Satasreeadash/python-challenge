import os
import csv

csvpath = os.path.join('Resources','election_data.csv')
print(csvpath)

with open(csvpath, 'r', newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    csvheader = next(csvreader)

    cand_dict = {}
    for row in csvreader:
        key = row[2]
        if key in cand_dict.keys():
            cand_dict[key] = cand_dict[key] + 1
        else:
            cand_dict[key] = 1

    with open("Output.txt", 'w') as output:
        text1 = "```text" + "\n"+ "Election Results" + "\n" + "-------------------------" + "\n"
        print(text1)
        output.write(text1)
        totalvotes = sum(cand_dict.values())
        print("Total Votes: " + str(totalvotes))
        output.write("Total Votes: " + str(totalvotes) + "\n")
        for key,value in cand_dict.items():
            text2 = key + ": " + str(round((value/totalvotes)*100 ,2)) + "% " + "(" + str(value) + ")" +"\n"
            print(text2)
            output.write(text2)
        print("\n"+ "-------------------------")
        output.write("\n"+ "-------------------------" + "\n")
        winner = [(value, key) for key, value in cand_dict.items()]
        print ("Winner: " + max(winner)[1])
        output.write("Winner: " + max(winner)[1]+ "\n")
        print("-------------------------","```", sep = "\n")
        output.write("-------------------------" + "\n"+ "```")