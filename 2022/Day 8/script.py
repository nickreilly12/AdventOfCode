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
total_viewable_trees = 0
current_view_height = 0

for row in forrest_array:
    current_viewable_trees = 1
    for n in range(1,98):
        try:
            if int(row[n+1]) > current_view_height:
                current_view_height = int(row[n])
                current_viewable_trees += 1
            elif int(row[n+1]) < current_view_height:
                continue
        except IndexError:
            continue
        current_view_height = 0
    total_viewable_trees += current_viewable_trees

print(f"Total viewable trees after left to right comparison is {total_viewable_trees}")

total_viewable_after_top_down = 0
current_viewable_trees = 1

for column in range(1,98):
    current_view_height = 0
    for row in range(1,98):
        try:
            if int(forrest_array[row+1,column]) > current_view_height:
                current_view_height = int(forrest_array[row+1,column])
                current_viewable_trees += 1
            elif int(forrest_array[row+1,column]) < current_view_height:
                continue
        except IndexError:
            continue
    total_viewable_after_top_down = current_viewable_trees
    current_view_height = 0
total_viewable_trees += total_viewable_after_top_down

print(f"Viewable trees after top down comparison is {total_viewable_after_top_down}")
print(f"Total after top down and left to right is now {total_viewable_trees}")