import csv

hpos = 0
vpos = 0
aim = 0

with open('inputs.csv','r') as sourcefile:
    reader = csv.reader(sourcefile)
    for row in reader:
        if row[0] == "forward":
            hpos += int(row[1])
            vpos += (aim * int(row[1]))
        elif row[0] == "backwads":
            hpos -+ int(row[1])
        elif row[0] == "up":
            aim -= int(row[1])
        elif row[0] == "down":
            aim += int(row[1])
        else:
            continue
print("Your current horizontal position is ",hpos, " and you current vertical position is ", vpos, " and your aim is ", aim)
print(vpos*hpos)