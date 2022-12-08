import numpy as np

with open("data.txt",'r') as sourcefile:
    datalist = [x for x in sourcefile.read().split()]

totallist = []
for row in datalist:
    rowlist = []
    for n in range(0,99):
        rowlist.append(row[n])
    totallist.append(rowlist)

forrest_array = np.asarray(totallist)
#numpy column
#print(forrest_array[:,0])
#numpy row
#print(forrest_array[0,:])

total_viewable_trees = 0

for row in forrest_array:
    current_viewable_trees = 1
    for n in range(0,99):
        try:
            if row[n+1] > row[n]:
                current_viewable_trees +=1
            elif row[n+1] < row[n]:
                continue
        except IndexError:
            continue
    total_viewable_trees += current_viewable_trees
#left to right comparison
print(total_viewable_trees)

for n in range(0,99):
    for row in forrest_array:
        current_viewable_trees = 1
        for column in row[n]:
            try:
                if row[n+1] > row[n]:
                    current_viewable_trees+=1
                elif row[n+1] < row[n]:
                    continue
            except IndexError:
                continue
    total_viewable_trees += current_viewable_trees

#add top to bottom comparison
print(total_viewable_trees)