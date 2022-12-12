import numpy as np
import logging

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
        up_view, down_view, left_view, right_view, scenic_score = 0,0,0,0,0
        logging.warning("checking left at {}{}".format(x,y))
        if y == 0:
            left_view = 0
        elif y == 1:
            left_view = 1
        else:
            cancel_loop = False
            while cancel_loop == False:
                for a in range(y-1,-1,-1):
                    if forrest_array[x,a,0] >= forrest_array[x,y,0]:
                        left_view += 1
                        cancel_loop = True
                    elif forrest_array[x,a,0] < forrest_array[x,y,0]:
                        left_view += 1
        logging.warning("Checking right at {}{}".format(x,y))
        if y == 98:
            right_view = 0
        elif y == 97:
            right_view = 1
        else:
            cancel_loop = False
            while cancel_loop == False:
                for a in range(y+1,99):
                    if forrest_array[x,a,0] >= forrest_array[x,y,0]:
                        right_view += 1
                        cancel_loop = True
                    elif forrest_array [x,a,0] < forrest_array[x,y,0]:
                        right_view += 1
        logging.warning("Checking up at {}{}".format(x,y))
        if x == 0:
            up_view == 0
        elif x == 1:
            up_view == 1
        else:
            cancel_loop = False
            while cancel_loop == False:
                for a in range(x-1,-1,-1):
                    if forrest_array[a,y,0] >= forrest_array[x,y,0]:
                        up_view += 1
                        cancel_loop = True
                    elif forrest_array[a,y,0] < forrest_array[x,y,0]:
                        up_view += 1
        logging.warning("Checking down at {}{}".format(x,y))
        if x == 98:
            down_view = 0
        elif x == 97:
            down_view = 1
        else:
            cancel_loop = False
            while cancel_loop == False:
                for a in range(x+1,99):
                    if forrest_array[a,y,0] >= forrest_array[x,y,0]:
                        down_view += 1
                        cancel_loop = True
                    elif forrest_array[a,y,0] < forrest_array[x,y,0]:
                        down_view += 1
        scenic_score = up_view * down_view * left_view * right_view
        forrest_array[x,y,1] = scenic_score