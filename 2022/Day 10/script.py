with open('data','r') as sourcefile:
    data = sourcefile.read().split('\n')


def cycling(cycle, xregister, signal_strength):
    print(cycle,xregister,signal_strength)
    cycle += 1
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        signal_strength += xregister*cycle
        print(cycle,xregister,signal_strength, "\ncycle complete")
        return cycle, xregister, signal_strength
    else:
        print(cycle,xregister,signal_strength, "\ncycle complete")
        return cycle, xregister, signal_strength

cycle = 0
xregister = 1
signal_strength = 0

for command in data:
    if command == 'noop':
        cycle,xregister,signal_strength = cycling(cycle,xregister,signal_strength)
    else:
        cycle,xregister,signal_strength = cycling(cycle,xregister,signal_strength)
        cycle,xregister,signal_strength = cycling(cycle,xregister,signal_strength)
        xregister += int(command.split(' ')[1])

print(signal_strength)