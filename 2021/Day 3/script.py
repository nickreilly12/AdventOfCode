with open('data', 'r') as sourcefile:
    data = [x for x in sourcefile.read().split()]

N = len(data[0])
newbinnum = []
newepsnum = []

for n in range(N):
    count0 = sum(1 for line in data if line[n] == '0')
    count1 = len(data) - count0
    if count0 > count1:
        newbinnum.append("0")
        newepsnum.append("1")
    elif count1 > count0:
        newbinnum.append("1")
        newepsnum.append("0")

bitvalue = 2048
ebitvalue = 2048
gammanum = 0
epsilonnum = 0
for x in newbinnum:
    if x == "1":
        gammanum += bitvalue
    bitvalue /= 2

for x in newepsnum:
    if x == "1":
        epsilonnum += ebitvalue
    ebitvalue /=2

print("Epsilon value is ", epsilonnum)
print("Gamma value is ", gammanum)

print("Result is ", epsilonnum * gammanum)