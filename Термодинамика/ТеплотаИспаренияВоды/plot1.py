import matplotlib.pyplot as plt
from scipy import interpolate
import laba_functions as lf
 
upData = open('upData.txt')
downData = open('downData.txt')

def calculatePressure(h1: lf.value,h2: lf.value) -> lf.value:
    return lf.value(135960*abs(h1.value-h2.value),
                    2*135960*h1.error)


def getData(data):
    temp,pres = [],[]
    for line in data:
        t,h11,h21 = map(float,line.split())
        h1= lf.value(h11/(10**3),0.05/(10**3))
        h2 = lf.value(h21/(10**3),0.05/(10**3))
        temp.append(lf.value(t+273,0.05))
        pres.append(calculatePressure(h1,h2))
    return temp,pres
def plot1(temp,pres):
    a,b = lf.MNK([i.value for i in temp],
                 [i.value for i in pres])
    x = [i/1000 for i in range(290000,311000)]
    y = [(a.value)*i+b.value for i in x]
    return a,b,x,y
def countL(T: list,P: list,a: lf.value) -> list:
    L = []
    for i in range(len(T)):
        value = (T[i].value**2)*lf.const.R*a.value/(P[i].value)
        sigmaF = 2*value*T[i].error/T[i].value
        sigmaS = a.error*value/a.value
        sigmaT = P[i].error*value/P[i].value
        error = abs(sigmaF)+abs(sigmaS)+abs(sigmaT)
        L.append(lf.value(value/(1000*lf.const.MH2O),error/(1000*lf.const.MH2O)))
    return L
def printAllData(T: list,P: list,L: list) ->None:
    for k,i in enumerate(L):
        i.print("Теплота Испарения "+str(k+1))
        T[k].print("Температура")
        P[k].print("Давление")
        print()


Tup,Pup = getData(upData)
aUp,bUp,xUp,yUp = plot1(Tup,Pup)
Tdown,Pdown = getData(downData)
aDown,bDown,xDown,yDown = plot1(Tdown,Pdown)

Lup = countL(Tup,Pup,aUp)
Ldown = countL(Tdown,Pdown,aDown)
LupResult = lf.sigmaSl(Lup)
LdownResult = lf.sigmaSl(Ldown)
s1,s2 = 0,0
for i in Lup:
    if i.value<=LupResult.value+210:
        s1+=1
        s2+=1
    elif i.value<=LupResult.value+420:
        s2+=1

    

    
#вывод данных
print("1 cигма: "+str(100*round(s1/len(Lup),2)))
print("2 cигма: "+str(100*round(s2/len(Lup),2)))
print("_________________________")
printAllData(Tup,Pup,Lup)
aUp.print("Коэффициент A повышение температуры")
bUp.print("Коэффициент B повышение температуры")
print()
print("___________________________")
print()
printAllData(Tdown,Pdown,Ldown)
aDown.print("Коэффициент A понижение температуры")
bDown.print("Коэффициент B понижение температуры")
print()
print("_________________________________")
print()
print("Итог:")
print()
LupResult.print("При повышении")
print()
LdownResult.print("При понижении")

#построение графика
forXTicks = [i for i in range(290,311)]
forYTicks = [i for i in range(2800,5450,50)]
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

    

