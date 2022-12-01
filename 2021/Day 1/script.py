import csv

m = []
increaselog = ["N/A"]

with open('inputs.csv','r') as sourcefile:
    reader = csv.reader(sourcefile)
    for row in reader:
        m.append(row[0])

d1 = 0
d2 = 1
d3 = 2
d4 = 3

for depth in m:
    try:
        currentwindowsize = int(m[d1]) + int(m[d2]) + int(m[d3])
        nextwindowsize = int(m[d2]) + int(m[d3]) + int(m[d4])
    except IndexError:
        continue
    if currentwindowsize < nextwindowsize:
        increaselog.append("increase")
        d1 += 1
        d2 += 1
        d3 += 1
        d4 += 1
    else:
        increaselog.append("decrease")
        d1 += 1
        d2 += 1
        d3 += 1
        d4 += 1

import pdb;pdb.set_trace()
increasecount = 0

for item in increaselog:
    if item == "increase":
        increasecount += 1
print(increasecount)