with open("input.txt", "r") as file:
    column1 = []
    column2 = []

    for line in file:
        parts = line.split()
        column1.append(int(parts[0]))
        column2.append(int(parts[1]))

count_item = []

for item in column1:
    count_item.append(column2.count(item))

sim_score = 0

for a,b in zip(column1,count_item):
    subtotal= a*b
    sim_score += subtotal

print(sim_score)
