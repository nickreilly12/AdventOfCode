import re

# Define the regex pattern
pattern = r"mul\((\b([0-9]|[1-9][0-9]|[1-9][0-9]{2})\b),(\b([0-9]|[1-9][0-9]|[1-9][0-9]{2})\b)\)"

# Read the content of the file
with open('input.txt', 'r') as file:
    content = file.read()

# Find all matches of the pattern
matches = re.finditer(pattern, content)

# Extract the full matches and perform multiplication
results = []
for match in matches:
    full_match = match.group(0)
    x = int(match.group(1))
    y = int(match.group(3))
    result = x * y
    results.append(result)

print(sum(results))