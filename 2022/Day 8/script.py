import numpy as np

forrest_array = np.zeros((99,99,2),dtype=int)

with open("data.txt",'r') as sourcefile:
    datalist = [x for x in sourcefile.read().split()]

totallist = []
for row in datalist:
    rowlist = []
    for n in range(0,99):
        rowlist.append(row[n])
    totallist.append(rowlist)

forrest_array[:,:,0] = np.asarray(totallist)

current_viewable_height = 0
Viewable_trees = 0

current_checklist = []
for x in forrest_array[:,0,0]:
    current_checklist.append(x)

print(current_checklist)

