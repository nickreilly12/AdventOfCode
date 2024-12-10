import re

def parse_and_calculate(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Regular expression to find all "mul(x,y)" patterns
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    
    # Initialize variables
    total_sum = 0
    enabled = True
    
    # Split the content by "do()" and "don't()"
    parts = re.split(r"(do\(\)|don't\(\))", content)
    import pdb;pdb.set_trace()
    
    for part in parts:
        if part == "do()":
            enabled = True
        elif part == "don't()":
            enabled = False
        else:
            if enabled:
                matches = pattern.findall(part)
                for match in matches:
                    x, y = map(int, match)
                    total_sum += x * y
    
    return total_sum

# Path to the input file
file_path = 'input.txt'

# Calculate the sum of all enabled multiplications
result = parse_and_calculate(file_path)

print(f"The sum of all enabled multiplications is: {result}")