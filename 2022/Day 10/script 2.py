import pdb
with open('data','r') as sourcefile:
    data = sourcefile.read().split('\n')

cycle = 1
xreg = 2
def set_xreg(xreg):
    xregl = xreg - 1
    xregr = xreg + 1
    return xregl, xregr
xregl,xregr = set_xreg(xreg)
crt = []

def draw(crt,cycle,xreg,xregl,xregr):
    if cycle == xreg or cycle == xregl or cycle == xregr:
        crt.append('#')
        return crt
    else:
        crt.append('.')
        return crt

for command in data:
    if command == 'noop':
        crt = draw(crt,cycle,xreg,xregl,xregr)
        cycle += 1
        if cycle > 40:
            cycle -= 40
    else:
        crt = draw(crt,cycle,xreg,xregl,xregr)
        cycle += 1
        if cycle > 40:
            cycle -= 40
        crt = draw(crt,cycle,xreg,xregl,xregr)
        cycle += 1
        if cycle > 40:
            cycle -= 40
        xreg += int(command.split(' ')[1])
        xregl,xregr = set_xreg(xreg)
    
print(crt[0],crt[1],crt[2],crt[3],crt[4],crt[5],crt[6],crt[7],crt[8],crt[9],crt[10],crt[11],crt[12],crt[13],crt[14],crt[15],crt[16],crt[17],crt[18],crt[19],crt[20],crt[21],crt[22],crt[23],crt[24],crt[25],crt[26],crt[27],crt[28],crt[29],crt[30],crt[31],crt[32],crt[33],crt[34],crt[35],crt[36],crt[37],crt[38],crt[39])
print(crt[40],crt[41], crt[42], crt[43], crt[44], crt[45], crt[46], crt[47], crt[48], crt[49], crt[50], crt[51], crt[52], crt[53], crt[54], crt[55], crt[56], crt[57], crt[58], crt[59], crt[60], crt[61], crt[62], crt[63], crt[64], crt[65], crt[66], crt[67], crt[68], crt[69], crt[70], crt[71], crt[72], crt[73], crt[74], crt[75], crt[76], crt[77], crt[78], crt[79])
print(crt[80], crt[81], crt[82], crt[83], crt[84], crt[85], crt[86], crt[87], crt[88], crt[89], crt[90], crt[91], crt[92], crt[93], crt[94], crt[95], crt[96], crt[97], crt[98], crt[99], crt[100], crt[101], crt[102], crt[103], crt[104], crt[105], crt[106], crt[107], crt[108], crt[109], crt[110], crt[111], crt[112], crt[113], crt[114], crt[115], crt[116], crt[117], crt[118], crt[119])
print(crt[120], crt[121], crt[122], crt[123], crt[124], crt[125], crt[126], crt[127], crt[128], crt[129], crt[130], crt[131], crt[132], crt[133], crt[134], crt[135], crt[136], crt[137], crt[138], crt[139], crt[140], crt[141], crt[142], crt[143], crt[144], crt[145], crt[146], crt[147], crt[148], crt[149], crt[150], crt[151], crt[152], crt[153], crt[154], crt[155], crt[156], crt[157], crt[158], crt[159])
print(crt[160], crt[161], crt[162], crt[163], crt[164], crt[165], crt[166], crt[167], crt[168], crt[169], crt[170], crt[171], crt[172], crt[173], crt[174], crt[175], crt[176], crt[177], crt[178], crt[179], crt[180], crt[181], crt[182], crt[183], crt[184], crt[185], crt[186], crt[187], crt[188], crt[189], crt[190], crt[191], crt[192], crt[193], crt[194], crt[195], crt[196], crt[197], crt[198], crt[199])
print(crt[200], crt[201], crt[202], crt[203], crt[204], crt[205], crt[206], crt[207], crt[208], crt[209], crt[210], crt[211], crt[212], crt[213], crt[214], crt[215], crt[216], crt[217], crt[218], crt[219], crt[220], crt[221], crt[222], crt[223], crt[224], crt[225], crt[226], crt[227], crt[228], crt[229], crt[230], crt[231], crt[232], crt[233], crt[234], crt[235], crt[236], crt[237], crt[238], crt[239])