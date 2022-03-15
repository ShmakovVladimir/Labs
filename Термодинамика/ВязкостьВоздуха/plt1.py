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
        v = q*25/1000
        p*=(0.2*lf.const.g)
        q = v/t
        Q.append(lf.value(q,0.01*q))
        pressure.append(lf.value(p,0.02*p))
    return length,diam,pressure,Q
def viscosityCount(PbyQ: lf.value,d: lf.value,l: lf.value)->lf.value:
    vis = lf.const.pi*(d.value**2)*PbyQ.value/(16*8*l.value)
    visErrord = abs((4*vis/d.value)*d.error)
    visErrorPbyQ = abs(PbyQ.error*vis/PbyQ.value)
    visErrorL = abs(l.error*vis/l.value)
    return lf.value(vis,visErrord+visErrorPbyQ+visErrorL)
l,d,p,q = readData('data2.txt')
a,b = lf.MNK([i.value for i in p],[i.value for i in q])
etta = viscosityCount(a,d,l)
a.print("К.ф a")
b.print("К.ф б")
print()
etta.print("Вязкость возудха")
print()
xT = [i for i in range(90,235,5)]
yT = [i/100000 for i in range(80,136)]
y = [a.value*x+b.value for x in xT]
plt.plot(xT,y)
plt.grid()
plt.xticks(xT)
plt.yticks(yT)
lf.plotValues(p,q)