import laba_functions as lf
import matplotlib.pyplot as plt
import math
def readData(path: str)->tuple:
    data = open(path)
    _,d = data.readline().split()
    _,t = data.readline().split()
    _,q = data.readline().split()
    d,q,t = map(float,[d,q,t])
    d = lf.value(d/1000,0.05/1000)
    l,p = [],[]
    data.readline()
    for line in data:
        l.append(lf.value(float(line.split()[0]),0.02))
        p.append(lf.value(float(line.split()[1])*0.2*lf.const.g,0.2*lf.const.g))
    return d,q,t,l,p
d,q,t,l,p = readData("data81.txt")
a,b = lf.MNK(l[1:len(l):1],p[1:len(p):1])
xT = [i/100 for i in range(0,150,5)]
xLine = [i/100 for i in range(math.ceil(l[1].value)*100,150)]
yLine = [p[0].value]+[a.value*i+b.value for i in xLine]
xLine = [l[0].value]+xLine
yT = [i for i in range(40,175,5)]
print("Line coef:")
a.print("a")
b.print("b")
print()
plt.xticks(xT)
plt.yticks(yT)
plt.grid()
plt.plot(xLine,yLine)
lf.plotValues(l,p)



