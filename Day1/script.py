import csv
runningtotal = 0
totallist=[]
with open('inputs.csv','r') as sourcefile:
    reader = csv.reader(sourcefile)
    for row in reader:
        if row[0] == "NEW":
            totallist.append(runningtotal)
            runningtotal = 0
        else:
            currentvalue = int(row[0])
            runningtotal = runningtotal + currentvalue

totallist.sort(reverse=True)
print(totallist[0])