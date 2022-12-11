import numpy as np

forrest_array = np.zeros((99,99,2),dtype=int)

with open("data.txt",'r') as sourcefile:
    datalist = [x for x in sourcefile.read().split()]

#turn the input data into a list for easy import into numpy
totallist = []
for row in datalist:
    rowlist = []
    for n in range(0,99):
        rowlist.append(row[n])
    totallist.append(rowlist)

#pull the list above into numpy
forrest_array[:,:,0] = np.asarray(totallist) 

#loop through x axis
for x in range(0,99):
    #loop through y acis
    for y in range(0,99):
        scenic_score = 0
        #loop to move up
        for a in range(y,0):
            current_scenic_score = 0
            while forrest_array[x,a,0] < forrest_array[x,y,0]:
                current_scenic_score += 1
            scenic_score += current_scenic_score
        for a in range(y,99):
            current_scenic_score = 0
            while forrest_array[x,a,0] < forrest_array[x,y,0]:
                current_scenic_score += 1
            scenic_score *= current_scenic_score
        for a in range(x,0):
            current_scenic_score = 0
            while forrest_array[a,y,0] < forrest_array[x,y,0]:
                current_scenic_score += 1
            scenic_score *= current_scenic_score
        for a in range(x,99):
            current_scenic_score = 0
            while forrest_array[a,y,0] < forrest_array[x,y,0]:
                current_scenic_score += 1
            scenic_score *= current_scenic_score
        forrest_array[x,y,1] = scenic_score

print(forrest_array[:,:,1])