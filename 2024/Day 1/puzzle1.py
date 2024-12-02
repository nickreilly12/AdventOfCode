with open("input.txt", "r") as file:
    column1 = []
    column2 = []

    for line in file:
        parts = line.split()
        column1.append(int(parts[0]))
        column2.append(int(parts[1]))

column1.sort()
column2.sort()

distances = []

for a,b in zip(column1,column2):
    if a>b:
        res = a-b
    else:
        res = b-a
    distances.append(res)

total = 0
for distance in distances:
    total += distance

print(total)