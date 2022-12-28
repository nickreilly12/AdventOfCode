with open('data','r') as sourcefile:
    data = sourcefile.read().split('\n')

cycle = 0
xregister = 1

commands = []
signal_strength = []
def cyclecheck(signal_strength,cycle,xregister):
    if cycle == 20 or 60 or 100 or 140 or 180 or 220:
        signal_strength.append(cycle*xregister)
        return signal_strength
    else:
        return(signal_strength)

for row in data:
    commands.append(row)

for command in commands:
    if command == 'noop':
        cycle += 1
        signal_strength = cyclecheck(signal_strength,cycle,xregister)
    else:
        cycle += 1
        signal_strength = cyclecheck(signal_strength,cycle,xregister)
        cycle += 1
        signal_strength = cyclecheck(signal_strength,cycle,xregister)
        #import pdb;pdb.set_trace()
        xregister += int(command.split(' ')[1])

print(signal_strength)