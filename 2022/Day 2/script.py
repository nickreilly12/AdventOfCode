import csv

orock = "A"
opaper = "B"
oscissors = "C"
mrock = "X"
mpaper = "Y"
mscissors = "Z"
score = 0

with open('inputs.csv','r') as sourcefile:
    reader = csv.reader(sourcefile)
    for row in reader:
        if row[1] == mrock:
            score += 1
            if row[0] == oscissors:
                score += 6
            elif row[0] == orock:
                score += 3
        elif row[1] == mpaper:
            score += 2
            if row[0] == opaper:
                score += 3
            elif row[0] == orock:
                score +=6
        elif row[1] == mscissors:
            score += 3
            if row[0] == oscissors:
                score += 3
            elif row[0] == opaper:
                score += 6
print("Your score would be ", score)
