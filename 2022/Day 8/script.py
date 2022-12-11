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
forrest_array[:,0,1] = 1
forrest_array[0,:,1] = 1
forrest_array[:,-1,1] = 1
forrest_array[-1,:,1] = 1

for x in range(0,99):
    current_viewable_height = 0
    for y in range(0,99):
        if forrest_array[x,y,1] == 1:
            if forrest_array[x,y,0] > current_viewable_height:
                current_viewable_height = forrest_array[x,y,0]
            continue
        else:
            if forrest_array[x,y,0] == current_viewable_height:
                continue
            elif forrest_array[x,y,0] > current_viewable_height:
                forrest_array[x,y,1] = 1
                current_viewable_height = int(forrest_array[x,y,0])
            else:
                continue

for y in range(0,99):
    current_viewable_height = 0
    for x in range(0,99):
        if forrest_array[x,y,1] == 1:
            if forrest_array[x,y,0] > current_viewable_height:
                current_viewable_height = forrest_array[x,y,0]
            continue
        else:
            if forrest_array[x,y,0] == current_viewable_height:
                continue
            elif forrest_array[x,y,0] > current_viewable_height:
                forrest_array[x,y,1] = 1
                current_viewable_height = int(forrest_array[x,y,0])
            else:
                continue

forrest_array = np.fliplr(forrest_array)

for x in range(0,99):
    current_viewable_height = 0
    for y in range(0,99):
        if forrest_array[x,y,1] == 1:
            if forrest_array[x,y,0] > current_viewable_height:
                current_viewable_height = forrest_array[x,y,0]
            continue
        else:
            if forrest_array[x,y,0] == current_viewable_height:
                continue
            elif forrest_array[x,y,0] > current_viewable_height:
                forrest_array[x,y,1] = 1
                current_viewable_height = int(forrest_array[x,y,0])
            else:
                continue

forrest_array = np.flipud(forrest_array)


for y in range(0,99):
    current_viewable_height = 0
    for x in range(0,99):
        if forrest_array[x,y,1] == 1:
            if forrest_array[x,y,0] > current_viewable_height:
                current_viewable_height = forrest_array[x,y,0]
            continue
        else:
            if forrest_array[x,y,0] == current_viewable_height:
                continue
            elif forrest_array[x,y,0] > current_viewable_height:
                forrest_array[x,y,1] = 1
                current_viewable_height = int(forrest_array[x,y,0])
            else:
                continue

viewable_trees = 0

for x in sum(forrest_array[:,:,1]):
    viewable_trees += x

print(viewable_trees)