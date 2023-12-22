with open('input.txt','r') as sourcefile:
    with open ('output.txt',"w") as dstfile:
        for row in sourcefile:
            newline = ''.join(filter(str.isdigit,row))
            digit = newline[:1] + newline[-1:]
            dstfile.write(f"{digit}\r")

total = 0

with open('output.txt','r') as sourcefile:
    for row in sourcefile:
        total += (int(row))

print(total)