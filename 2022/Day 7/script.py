rows = []
with open('data.txt','r') as sourcefile:
    for x in sourcefile.read().split('\n'):
        rows.append(x)

def changedirectory(current,changetype,new):
    if changetype == "..":
        currentlist = []
        for x in current.split('/'):
            currentlist.append(x)
        currentlist.remove(currentlist[len(currentlist)-1])
        new = ''
        for f in currentlist:
            new = new+'/'+f
    elif changetype == "/":
        new = '/'
    else:
        currentlist = []
        for x in current.split('/'):
            currentlist.append(x)
        currentlist.append(new)
        new = ''
        new ="/".join([str(item) for item in currentlist])
        print(new)
    return new

def listcontents(current):
    print("function to list contents")
def save_sizes_for_directory(current,size):
    print("combine current directory and sum of all sizes")

current = '/'

for row in rows:
    if '$ cd' in row:
        if '$ cd /' in row:
            current = changedirectory(current,'/','/')
            print(current)
            import pdb;pdb.set_trace()
        elif '$ cd ..' in row:
            current = changedirectory(current,'..','..')
            print(current)
            import pdb;pdb.set_trace()
        else:
            newdir = row.split(' ')[2]
            current = changedirectory(current,'new',newdir)
            print(current)
            import pdb;pdb.set_trace()

