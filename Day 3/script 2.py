import csv

items = []

with open('inputs.csv','r') as sourcefile:
    reader = csv.reader(sourcefile)
    for row in reader:
        items.append(row[0])

e1 = 0
e2 = 1
e3 = 2
badge = []

for n in range(0,100):
    for item in items[e1]:
        if item in items[e2]:
            if item in items[e3]:
                badge.append(item)
                break
    e1 += 3
    e2 += 3
    e3 += 3
print(badge)
numbers = []

for char in badge:
    numbers.append(ord(char) - 96)

convertednumbers = []
for number in numbers:
    if number < 0 :
        convertednumbers.append(int(number) + 58)
    else:
        convertednumbers.append(int(number))

sum = 0
for n in convertednumbers:
    sum += n

print(sum)