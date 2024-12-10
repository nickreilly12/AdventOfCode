def is_monotonic(lst):
    increasing = all(y < x for x, y in zip(lst, lst[1:]))
    decreasing = all(x < y for x, y in zip(lst, lst[1:]))
    return increasing or decreasing

def check_range(lst):
    return all(abs(x - y) <= 3 for x, y in zip(lst, lst[1:]))

def is_safe(lst):
    return is_monotonic(lst) and check_range(lst)

def can_be_safe_by_removing_one(lst):
    for i in range(len(lst)):
        new_lst = lst[:i] + lst[i+1:]
        if is_safe(new_lst):
            return True
    return False

safe = 0
unsafe = 0
with open("input.txt", "r") as file:
    for line in file.readlines():
        levels = [int(n) for n in line.split()]
        if is_safe(levels) or can_be_safe_by_removing_one(levels):
            safe += 1
        else:
            unsafe += 1

print(f"There are {unsafe} unsafe reports and {safe} safe reports.")
print(f"The checksum is: {unsafe + safe}")