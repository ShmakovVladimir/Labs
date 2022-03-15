import laba_functions as lf
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d
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
d,q,t,l,p = readData("data83.txt")
a,b = lf.MNK(l,p)
xT = [i/100 for i in range(0,150,5)]
xLine = [i/100 for i in range(0,150)]
yLine = [a.value*i+b.value for i in xLine]
yT = [i for i in range(40,1500,10)]
f = interp1d([i.value for i in l],[i.value for i in p],kind='quadratic')
xInterpolated = [i/1000 for i in range(math.floor(l[0].value*1000),math.ceil(l[-1].value*1000))]
yInterpolated = [f(x) for x in xInterpolated]
print("Line coef:")
a.print("a")
b.print("b")
print()
plt.xticks(xT)
plt.yticks(yT)
plt.grid()
plt.plot(xInterpolated,yInterpolated)
plt.plot(xLine,yLine,linewidth=1,ls = '-.')
lf.plotValues(l,p)



