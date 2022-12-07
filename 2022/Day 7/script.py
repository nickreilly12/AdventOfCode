rows = []
with open('data.txt','r') as sourcefile:
    for x in sourcefile.read().split('\n'):
        rows.append(x)

directory_size = {}

def changedirectory(current,changetype,new):
    if changetype == "..":
        currentlist = []
        for x in current.split('/'):
            currentlist.append(x)
        currentlist.remove(currentlist[len(currentlist)-1])
        for x in currentlist:
            if x == "":
                currentlist.remove(x)
        new = ''
        for f in currentlist:
            new = new+'/'+f
        if new == '':
            new = '/'
    elif changetype == "/":
        new = '/'
    else:
        currentlist = []
        for x in current.split('/'):
            currentlist.append(x)
        currentlist.append(new)
        #print(currentlist)        
        for x in currentlist:
            if x == "":
                currentlist.remove(x)
        new ="/".join([str(item) for item in currentlist])
        if new[0] != "/": new = "/" + new
    return new

def save_sizes_for_directory(current,size):
    directory_size[current] = [size]

current = '/'

for row in rows:
    if '$ cd' in row:
        if '$ cd /' in row:
            current = changedirectory(current,'/','/')
            #print(current)
        elif '$ cd ..' in row:
            current = changedirectory(current,'..','..')
            #print(current)
        else:
            newdir = row.split(' ')[2]
            current = changedirectory(current,'new',newdir)
            #print(current)
    elif '$ ls' in row:
        continue
    elif 'dir' in row:
        continue
    else:
        #this is saving each row individually rather than totalling each file into one value...
        save_sizes_for_directory(current+'/'+row.split(' ')[1],int(row.split(' ')[0]))

#All files and their sizes have been imported into a single dictionary. I just need to work out how to sum them up...
       
for key,value in directory_size.items():
    print(key,value)