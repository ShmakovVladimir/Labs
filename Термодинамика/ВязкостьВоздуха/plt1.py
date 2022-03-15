import laba_functions as lf
import matplotlib.pyplot as plt

def readData(path: str)->tuple:
    data = open(path)
    length,diam = data.readline(),data.readline()
    length = lf.value(float(length.split(" +- ")[0]),float(length.split(" +- ")[1]))
    diam = lf.value(float(diam.split(" +- ")[0]),float(diam.split(" +- ")[1]))
    data.readline()
    pressure,Q= [],[]
    for line in data:
        t,q,p = map(float,line.split())
        v = q*20/1000
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
l,d,p,q = readData('data2.txt')
a,b = lf.MNK([i.value for i in p],[i.value for i in q])
etta = viscosityCount(a,d,l)
a.print("a coefficient")
b.print("b coefficient")
print()
etta.print("air viscosity")
print()
xT = [i for i in range(90,235,5)]
yT = [i/100000 for i in range(60,111)]
y = [a.value*x+b.value for x in xT]
plt.plot(xT,y)
plt.grid()
plt.xticks(xT)
plt.yticks(yT)
lf.plotValues(p,q)