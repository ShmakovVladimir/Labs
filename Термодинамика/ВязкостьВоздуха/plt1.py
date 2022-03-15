import laba_functions as lf
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import math
def readData(path: str)->tuple:
    data = open(path)
    length,diam = data.readline(),data.readline()
    length = lf.value(float(length.split(" +- ")[0]),float(length.split(" +- ")[1]))
    diam = lf.value(float(diam.split(" +- ")[0]),float(diam.split(" +- ")[1]))
    data.readline()
    pressure,Q= [],[]
    for line in data:
        t,q,p = map(float,line.split())
        v = q*25/1000
        p*=(0.2*lf.const.g)
        q = v/t
        Q.append(lf.value(q,0.01*q))
        pressure.append(lf.value(p,0.02*p))
    return length,diam,pressure,Q
def viscosityCount(QbyP: lf.value,d: lf.value,l: lf.value)->lf.value:
    PbyQ = lf.value(1/(QbyP.value),QbyP.error/(QbyP.value**2))
    vis = lf.const.pi*((d.value/2)**4)*PbyQ.value/(8*l.value)
    visErrord = abs((4*vis/d.value)*d.error)
    visErrorPbyQ = abs(PbyQ.error*vis/PbyQ.value)
    visErrorL = abs(l.error*vis/l.value)
    return lf.value(vis,visErrord+visErrorPbyQ+visErrorL)
def reCount(vis: lf.value,diam: lf.value):
    Reinolds = 1.275*0.2*diam.value/(2*vis.value)
    ReVis = abs(vis.error*Reinolds/vis.value)
    ReDiam = abs(diam.error*Reinolds/diam.value)
    return lf.value(Reinolds,ReVis+ReDiam/2)
l,d,p,q = readData('data1.txt')
a,b = lf.MNK([p[3],p[3],p[4]],[q[3],q[3],q[4]])
aStart,bStart = lf.MNK([p[0],p[1],p[2]],[q[0],q[1],q[2]])
etta = viscosityCount(a,d,l)
Rein = reCount(etta,d)
f = interp1d(x=[i.value for i in p],y=[i.value for i in q],kind = 'quadratic')
xInter = [i/1000 for i in range(math.floor(p[0].value*1000+1),math.ceil(p[-1].value*1000-1))]
yInter = [f(x) for x in xInter]
a.print("a coefficient")
b.print("b coefficient")
print()
etta.print("air viscosity")
print()
Rein.print("Reinolds number")
print()
xT = [i for i in range(40,265,5)]
yT = [i/100000 for i in range(10,80)]
y = [a.value*x+b.value for x in xT]
yStart = [aStart.value*x+bStart.value for x in xT]
plt.plot(xInter,yInter)
plt.plot(xT,y,ls ='-.',linewidth = 1)
plt.plot(xT,yStart,ls ='-.',linewidth = 1)
plt.grid()
plt.xticks(xT)
plt.yticks(yT)
lf.plotValues(p,q)