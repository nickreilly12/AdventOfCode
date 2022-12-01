import csv

measurements = []
increaselog = ["N/A"]

with open('inputs.csv','r') as sourcefile:
    reader = csv.reader(sourcefile)
    for row in reader:
        measurements.append(row[0])

currentdepth = 0
nextdepth = 1

for measurement in measurements:
    try:
        print(measurements[nextdepth])
    except IndexError:
        continue
    if measurements[currentdepth] < measurements[nextdepth]:
        increaselog.append("increase")
        currentdepth = currentdepth + 1
        nextdepth = nextdepth + 1
    else:
        increaselog.append("decrease")
        currentdepth = currentdepth + 1
        nextdepth = nextdepth + 1

increasecount = 0

for depthchange in increaselog:
    if depthchange == "increase":
        increasecount = increasecount + 1

#this result comes out 1 less than the real total and I don't know why
print("The depth has increased ", increasecount, " times")