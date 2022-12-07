with open('data','r') as sourcefile:
    data = [x for x in sourcefile.read().split()]

numlen = len(data[0])

while len(data) > 1:
    for num in range(0,numlen):
        count0 = sum(1 for line in data if line[num] == "0")
        count1 = len(data) - count0
        delcount = 1
        dellist = []
        if count0 > count1:
            for entry in data:
                if entry[num] == "1":
                    delcount += 1
                    dellist.append(entry)
        elif count1 > count0:
            for entry in data:
                if entry[num] == "0":
                    delcount += 1
                    dellist.append(entry)
        elif count1 == count0:
            for entry in data:
                if entry[num] == "0":
                    delcount += 1
                    dellist.append(entry)
    
        for item in dellist:
            for d in data:
                if item == d:
                    data.remove(item)

print(data)

with open('data','r') as sourcefile:
    data = [x for x in sourcefile.read().split()]

numlen = len(data[0])

while len(data) > 1:
    for num in range(0,numlen):
        count0 = sum(1 for line in data if line[num] == "0")
        count1 = len(data) - count0
        delcount = 1
        dellist = []
        if count0 > count1:
            for entry in data:
                if entry[num] == "0":
                    delcount += 1
                    dellist.append(entry)
        elif count1 > count0:
            for entry in data:
                if entry[num] == "1":
                    delcount += 1
                    dellist.append(entry)
        elif count1 == count0:
            for entry in data:
                if entry[num] == "1":
                    delcount += 1
                    dellist.append(entry)
    
        for item in dellist:
            for d in data:
                if item == d:
                    data.remove(item)

print(data)
