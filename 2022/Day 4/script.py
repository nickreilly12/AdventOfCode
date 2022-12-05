import csv

assignments = []

with open('inputs.csv') as sourcefile:
    reader = csv.reader(sourcefile, delimiter=',')
    for row in reader:
        assignments.append(int(row[0]))
        assignments.append(int(row[1]))
        assignments.append(int(row[2]))
        assignments.append(int(row[3]))

e1start = 0
e1stop = 1
e2start = 2
e2stop = 3

e1checks = []
e2checks = []
duplicates = 0

for n in range(0,1000):
    e1checks = []
    e2checks = []
    for n in range(assignments[e1start], assignments[e1stop] + 1):
        e1checks.append(n)
    e1start += 4
    e1stop += 4
    for n in range(assignments[e2start],assignments[e2stop] + 1):
        e2checks.append(n)
    e2start += 4
    e2stop += 4
    if(set(e2checks).issubset(set(e1checks))):
        duplicates += 1
    elif (set(e1checks).issubset(set(e2checks))):
        duplicates += 1
        

print(duplicates)