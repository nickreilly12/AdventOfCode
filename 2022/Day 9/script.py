commands = []
with open("data.txt","r") as sourcefile:
    for row in sourcefile.read().split('-'):
        commands.append(row)

print(commands[1891])