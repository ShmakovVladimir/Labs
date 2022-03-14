import matplotlib.pyplot as plt
from scipy import interpolate
import laba_functions as lf
import math
upData = open('upData.txt')
downData = open('downData.txt')
def calculatelnPresure(h1: lf.value,h2: lf.value) -> lf.value:
    return lf.value(math.log(135960*abs(h1.value-h2.value)),
                    2*h1.error/(abs(h1.value-h2.value)))
    
def getData(data):
    temp,pres = [],[]
    for line in data:
        t,h11,h21 = map(float,line.split())
        h1 = lf.value(h11/(10**3),0.05/(10**3))
        h2 = lf.value(h21/(10**3),0.05/(10**3))
        temp.append(lf.value(1/(t+273),0.05/((t+273)**2)))
        #temp.append(lf.value(1/(t),0.05/((t)**2)))
        pres.append(calculatelnPresure(h1,h2))
    return temp,pres
def plot2(temp,pres):
    a,b = lf.MNK([i.value for i in temp],
                 [i.value for i in pres])
    x = [i/100000 for i in range(300,380)]
    y = [(a.value)*i+b.value for i in x]
    return a,b,x,y
def countL(a: lf.value):
    return lf.value(-a.value*lf.const.R/(1000*lf.const.MH2O),
                    -lf.const.R*a.error/(1000*lf.const.MH2O))
def printAll(T: list,P: list):
    for k,i in enumerate(T):
        i.print("1/Т "+str(k))
        P[k].print("ln(P) "+str(k))

Tup,Pup = getData(upData)
aUp,bUp,xUp,yUp = plot2(Tup,Pup)
Tdown,Pdown = getData(downData)
aDown,bDown,xDown,yDown = plot2(Tdown,Pdown)


lUp = countL(aUp)
lDown = countL(aDown)



printAll(Tup,Pup)
aUp.print("Коэффициент A повышение температуры")
print()
bUp.print("Коэффициент B повышение температуры")
print()
lUp.print("Температура испарения при повышении")
print()
print("______________________________________")
printAll(Tdown,Pdown)
print()
aDown.print("Коэффициент А понижение температуры")
print()
bDown.print("Коэффициент В понижение температуры")
print()
lDown.print("Температура испарения при понижении")


forXTicks = [i/100000 for i in range(300,380)]
forYTicks = [i/40 for i in range(75*4,90*4)]
plt.xticks(forXTicks)
plt.yticks(forYTicks)
plt.grid()
plt.plot(xUp,yUp,color = 'red')
plt.errorbar(x = [x.value for x in Tup],
             y =[y.value for y in Pup],
             xerr = [ex.error for ex in Tup],
             yerr = [ey.error for ey in Pup],
             fmt = '_',
             color = 'orange')
plt.errorbar(x = [x.value for x in Tdown],
             y =[y.value for y in Pdown],
             xerr = [ex.error for ex in Tdown],
             yerr = [ey.error for ey in Pdown],
             fmt = '_',
             color = 'purple')
plt.plot(xDown,yDown,color = 'blue')
plt.show()

    

