import csv

orock = "A"
opaper = "B"
oscissors = "C"
lose = "X"
draw = "Y"
win = "Z"
score = 0

with open('inputs.csv','r') as sourcefile:
    reader = csv.reader(sourcefile)
    for row in reader:
        if row[0] == orock:
            if row[1] == draw:
                score += 3
                score += 1
            elif row[1] == win:
                score += 6
                score += 2
            else:
                score += 3
        if row[0] == opaper:
            if row[1] == draw:
                score += 3
                score += 2
            elif row[1] ==win:
                score += 6
                score += 3
            else:
                score += 1
        if row[0] == oscissors:
            if row[1] == draw:
                score += 3
                score += 3
            elif row[1] == win:
                score += 6
                score += 1
            else:
                score += 2
print("Your score would be ", score)
