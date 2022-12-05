def calcO2():
    with open('data','r') as sourcefile:
        oxygen_rating = [x for x in sourcefile.read().split('\n')]
    while len(oxygen_rating) > 1 == True:
        try:
            for n in range(0,12):
                import pdb;pdb.set_trace()
                count0 = sum(1 for line in oxygen_rating if line[n] == '0')
                count1 = len(oxygen_rating) - count0
                for x in oxygen_rating:
                    if count0 > count1:
                        if x[n] == "1":
                            #import pdb; pdb.set_trace()
                            #print(f"checking character {n} : ", x[n])
                            #print(f"There are more zeroes in the list so {x} is being removed from the list")
    
                            oxygen_rating.remove(x)
                            #print(oxygen_rating)
                                
                    elif count1 > count0:
                        if x[n] == "0":
                            #import pdb; pdb.set_trace()
                            #print(f"checking character {n} : ", x[n])
                            #print(f"There are more ones in the list so {x} is being removed from the list")
                            oxygen_rating.remove(x)
                            #print(oxygen_rating)
                    else:
                        if x[n] == "0":
                            #import pdb; pdb.set_trace()
                            #print(f"checking character {n} : ", x[n])
                            #print(f"There is an equal number of ones and zeroes so  {x} is being removed from the list")
                            oxygen_rating.remove(x)
                            #print(oxygen_rating)
        except IndexError:
            continue
    return oxygen_rating
def calcC02():
    with open('data','r') as sourcefile:
        co2_rating = [x for x in sourcefile.read().split('\n')]
    while len(co2_rating) > 1 == True:
        try:
            for n in range(0,12):
                count0 = sum(1 for line in co2_rating if line[n] == '0')
                count1 = len(co2_rating) - count0
                for x in co2_rating:
                    if count0 > count1:
                        if x[n] == "0":
                            #print(f"checking character {n} : ", x[n])
                            #print(f"There are more zeroes in the list so {x} is being removed from the list")
                            co2_rating.remove(x)
                            #print(co2_rating)                               
                    elif count1 > count0:
                        if x[n] == "1":
                            #print(f"checking character {n} : ", x[n])
                            #print(f"There are more ones in the list so {x} is being removed from the list")
                            co2_rating.remove(x)
                            #print(co2_rating)
                    else:
                        if x[n] == "1":
                            #print(f"checking character {n} : ", x[n])
                            #print(f"There is an equal number of ones and zeroes so  {x} is being removed from the list")
                            co2_rating.remove(x)
                            #print(co2_rating)
        except IndexError:
            continue
    return co2_rating

o2rating = calcO2()
co2rating = calcC02()
print(o2rating)
print(co2rating)

