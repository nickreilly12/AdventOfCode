import numpy as np

#import crate positions into numpy array
cratepositions = np.loadtxt("cratepositions.txt",dtype=str, delimiter=" ")
#create empty columns list
columns = []

#create sub list for each column in the numpy array
#ignore any zeroes
#add sub list to columns list
for n in range(0,9):
    newentry = []
    for row in cratepositions:
        if row[n] == "0":
            continue
        else:
            newentry.append(row[n])
    columns.append(newentry)

#loop through individual items in each column
#check if the item is a digit
#remove any digits
for column in columns:
    for item in column:
        if item.isdigit() == True:
            column.remove(item)


#retrieve move information from file split with new line character   
with open('moves.txt','r') as sourcefile:
    moves = [x for x in sourcefile.read().split("\n")]

#throw digits from each move line into a list
#push each item in the list into a different variable
for x in moves:
    res = [int(i) for i in x.split() if i.isdigit()]
    mv = res[0]
    fm = res[1]
    to = res[2]
    items_to_insert = columns[fm-1][:mv]
    #reverse the order of the list so they're inserted into the new list bottom first
    #this retains the order of the picked list
    items_to_insert.reverse()
    #add items to new column
    for item in items_to_insert:
        columns[to-1].insert(0,item[0])
    #remove items from old column
    for item in items_to_insert:
        columns[fm-1].remove(item[0])
for column in columns:
    print(column[0])