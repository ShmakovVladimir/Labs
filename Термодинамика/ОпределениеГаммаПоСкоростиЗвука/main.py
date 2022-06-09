import matplotlib.pyplot as plt
import numpy as np
import laba_functions as lf


def getData(path: str):
    expNum,dotsNum = 5,5
    Temp = [None for _ in range(expNum)]
    freq = [[] for _ in range(expNum)]
    data = open(path)
    for i in range(expNum):
        line = data.readline()
        Temp[i] = lf.value(float(line.split()[2])+273,0.2)
        for _ in range(dotsNum):
            line = data.readline()
            freq[i].append(lf.value(float(line),1))
    return freq,Temp
def countGamma(temp: lf.value,soundSpeed: lf.value):
    molarMass = 28.97/(10**3)
    gammValue = molarMass*(soundSpeed.value**2)/(lf.const.R*temp.value)
    gammErrorC = 2*soundSpeed.error*gammValue/soundSpeed.value
    gammErrorT = temp.error*gammValue/temp.value
    return lf.value(gammValue,(gammErrorC**2+gammErrorT**2)**.5)
frequency,Temp = getData('data.txt')
length = lf.value(0.7,0.01)
soundSpeed = []
gamma =[]
for expNum in range(5):
    T,freq = Temp[expNum],frequency[expNum]
    yPlot = [lf.value(freq[i].value - freq[0].value,abs(2*freq[i].error)) for i in range(5)]
    xPlot = [lf.value(i+1,0) for i in range(5)]
    a,b = lf.MNK(xPlot,yPlot)
    xLine = np.arange(0.85,5+0.25,0.1)
    yLine = [a.value*x+b.value for x in xLine]
    fig,ax = plt.subplots()
    soundSpeed.append(lf.value(a.value*length.value*2,abs(a.error*length.value*2)+abs(2*length.error*a.value)))
    gamma.append(countGamma(T,soundSpeed[-1]))
    soundSpeed[-1].print(" Скорость звука")
    ax.set_title("Эксперимент "+str(expNum+1)+' $T = '+str(T.value)+' \pm '+str(T.error)+'$')
    plt.ylabel("Разность частот $f_{n}-f_{0}$ [Hz]")
    plt.xlabel("Номер гармоники $n$")
    plt.yticks(np.arange(0,1400,25))
    plt.xticks(np.arange(1,6,1))
    plt.grid()
    lf.plotValues(xPlot,yPlot)
    plt.plot(xLine,yLine,'--',label = (r'''Коэф наклона $\alpha = '''+str("{:.3g}".format(a.value))+".0"+' \pm '+str("{:.2g}".format(a.error))+'$'))
    ax.legend(loc = 'lower right')
    plt.show()
#lf.makeTable([xPlot,Temp,soundSpeed,gamma],
#              names=["exp","T","C_{s}",r'''\frac{C_{p}}{C_{v}}'''],
 #               measures= ['','K',r'''\frac{m}{s}''',''],
  #              path = 'stable.txt') 
plt.xlabel("Температура $K$")
plt.ylabel(r'''Скорость звука $\frac{m}{s}$''')
plt.grid()
lf.plotValues(Temp,soundSpeed)
plt.show()
