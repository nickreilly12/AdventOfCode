def is_monotonic(list):
    increasing = all(y < x for x, y in zip(list, list[1:]))
    decreasing = all (x < y for x, y in zip(list, list[1:]))
    return increasing or decreasing

def check_range(list):
    return all (abs(x - y) <=3 for x, y in zip(list,list[1:]))

safe = 0
unsafe = 0
with open("input.txt", "r") as file:
    for line in file.readlines():
        levels = []
        for n in line.split():
            levels.append(int(n))
        import pdb;pdb.set_trace()
        if is_monotonic(levels) != True:
            unsafe += 1
        elif check_range(levels) != True:
            unsafe += 1
        else:
            safe += 1

print(f"There are {unsafe} unsafe reports and {safe} safe reports.")
print(f"the checksum is : ", int(unsafe)+int(safe))