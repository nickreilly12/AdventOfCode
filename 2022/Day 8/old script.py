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
print(f"Total viewable trees after left to right comparison is {total_viewable_trees}")

total_viewable_after_top_down = 0
for column in range(0,99):
    current_viewable_trees = 1
    for row in range(0,99):
        try:
            if forrest_array[row,column+1] > forrest_array[row,column]:
                current_viewable_trees += 1
            elif forrest_array[row,column+1] < forrest_array[row,column]:
                continue
        except IndexError:
            continue
    total_viewable_after_top_down += current_viewable_trees
total_viewable_trees += total_viewable_after_top_down
print(f"Current viewable trees after top to bottom comparison is {total_viewable_after_top_down}")
print(f"This brings the total viewable trees to {total_viewable_trees}")

#This is giving the same total for top to bottom and left to right comparison...that can't be right.
#I've done this all wrong...it's only comparing 2 trees at a time - I need to set a view height variable and compare each tree to that...