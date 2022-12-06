with open('data','r') as sourcefile:
    data = [x for x in sourcefile.read().split()]

p1 = 0
p2 = 1
p3 = 2
p4 = 3
position = 4

for x in data[0]:
    if x == data[0][p2]: 
        p1 += 1
        p2 += 1
        p3 += 1
        p4 += 1
        position += 1
        continue 
    elif x == data[0][p3]:
        p1 += 1
        p2 += 1
        p3 += 1
        p4 += 1
        position += 1
        continue
    elif x == data[0][p4]:
        p1 += 1
        p2 += 1
        p3 += 1
        p4 += 1
        position += 1
        continue
    elif data[0][p2] == data[0][p3]:
        p1 += 1
        p2 += 1
        p3 += 1
        p4 += 1
        position += 1
        continue
    elif data[0][p2] == data[0][p4]:
        p1 += 1
        p2 += 1
        p3 += 1
        p4 += 1
        position += 1
        continue
    elif data[0][p3] == data[0][p4]:
        p1 += 1
        p2 += 1
        p3 += 1
        p4 += 1
        position += 1
        continue
    else:
        print(f"the start-of-packet marker is : {data[0][p1]}{data[0][p2]}{data[0][p3]}{data[0][p4]}\nIt appears after {position} characters")
        break