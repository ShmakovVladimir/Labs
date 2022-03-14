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
l,d,p,q = readData('data2.txt')
a,b = lf.MNK([i.value for i in p],[i.value for i in q])
a.print("К.ф a")
b.print("К.ф б")
xT = [i for i in range(90,235,5)]
yT = [i/100000 for i in range(80,136)]
y = [a.value*x+b.value for x in xT]
plt.plot(xT,y)
plt.grid()
plt.xticks(xT)
plt.yticks(yT)
lf.plotValues(p,q)