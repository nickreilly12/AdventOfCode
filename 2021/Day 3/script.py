import csv

itemlist = []

with open('inputs.csv','r') as sourcefile:
    reader = csv.reader(sourcefile)
    for row in reader:
        itemlist.append(row[0])

