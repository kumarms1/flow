data = [2,23,27,30,31,33,45,47,59,61,69,78,94,120]

i = 0
m = 0
j = 1
comp = 30
c = []
mc = []

while (i < len(data)):
    while( (m!=len(data)) and ((j-1)*comp <= data[m] <= j*comp) ) :
        c.append(data[m])
        m+=1
    i = m
    j+=1
    d = c.copy()
    mc.append(d)
    print(c)
    c.clear()

mcc = []
for k in mc:
    mcc.append(len(k))

print(mc)
print(mcc)

