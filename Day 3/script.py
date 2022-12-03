import csv
duplicateitems = []

with open('inputs.csv','r') as sourcefile:
    reader = csv.reader(sourcefile)
    for row in reader:
        contents = row[0]
        char = []
        half = int(len(contents)/2 // 1)
        compartment1 = contents[:half]
        compartment2 = contents[half:]
        for item in compartment1:
            if item in compartment2:
                char.append(item)
        duplicateitems.append(char[0])

numbers = []

for char in duplicateitems:
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