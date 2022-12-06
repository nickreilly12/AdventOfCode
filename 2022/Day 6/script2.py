with open('data','r') as sourcefile:
    data = [x for x in sourcefile.read().split()]
position = 14
for n in range(0,4095):
    try:
        inputs = []
        for x in range(0,14):
            inputs.append(data[0][n+x])
    except IndexError:
        break
    nodupe = [*set(inputs)]
    if len(nodupe) < 14:
        position += 1
        continue
    else:
        print(f"the string is {inputs} and is in position {position}")
        break