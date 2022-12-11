"""Updated with functions defined to reduce repititions"""
import numpy as np

def left_to_right_check(forrest_array):
    for x in range(0,99):
        #set the current view height
        current_viewable_height = 0
        #loop through each column in the row
        for y in range(0,99):
            #check if the tree has already been seen
            if forrest_array[x,y,1] == 1:
                #if it has, check to see if it's taller than your current view height
                if forrest_array[x,y,0] > current_viewable_height:
                    #if this previously seen tree is higher than your current view height, set your view height to that of the current tree
                    current_viewable_height = forrest_array[x,y,0]
                continue
            else:
                #check if this tree is the same height as one you've already seen and continue if it is
                if forrest_array[x,y,0] == current_viewable_height:
                    continue
                #check whether the current tree is larger than your current view height
                elif forrest_array[x,y,0] > current_viewable_height:
                    #if it is, change the view log to 1 to indicate that this tree has been seen and tracked
                    forrest_array[x,y,1] = 1
                    #update your view height to that of the current tree
                    current_viewable_height = int(forrest_array[x,y,0])
                #continue if the tree is smaller than the current view height
                else:
                    continue
    return forrest_array

def top_to_bottom_check(forrest_array):
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
    return forrest_array

#Initiate a numpy arrany the size of the forrest but with a 3rd dimention which will act as a log of which trees have been seen
forrest_array = np.zeros((99,99,2),dtype=int)

#open the input data
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

#change the seen log on the outside of the forrest to 1
forrest_array[:,0,1] = 1
forrest_array[0,:,1] = 1
forrest_array[:,-1,1] = 1
forrest_array[-1,:,1] = 1

#loop through the rows
forrest_array = left_to_right_check(forrest_array)
forrest_array = top_to_bottom_check(forrest_array)

#flip the numpy array from left to right
#this makes the next left to right check actually right to left as the array is reversed along that axis.
forrest_array = np.fliplr(forrest_array)
forrest_array = left_to_right_check(forrest_array)

#flip the array from top to bottom
#this makes the next top to bottom check actually bottom to top as the array is reversed along that axis.
forrest_array = np.flipud(forrest_array)
forrest_array = top_to_bottom_check(forrest_array)

#initiate the view count
viewable_trees = 0

#sum all items in the view log dimension on the numpy array
for x in sum(forrest_array[:,:,1]):
    #update the viewable trees count with the new totals
    viewable_trees += x

#show the viewable trees count
print(viewable_trees)