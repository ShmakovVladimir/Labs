import laba_functions as lf
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np

def readData(path: str)->tuple:
    data = open(path,'r')
    data.readline()
    time,pressure = [],[]
    for line in data:
        t,p,d = map(float,line.split())
        time.append(lf.value(t,0.5))
        pressure.append(lf.value(lf.const.mmHg*p*(10**d),lf.const.mmHg*1*(10**-6)))
    for i in range(len(time)-1,-1,-1):
        time[i].value-=time[0].value
    return time,pressure
def countQ(alpha: lf.value,W: lf.value)->lf.value:
    V = lf.value(1.21,0.1)
    Ppr = lf.value(8.3*lf.const.mmHg*(10**(-5)),0.1*lf.const.mmHg*(10**(-5)))
    QdVal = Ppr.value*W.value-V.value*alpha.value
    QeV = abs(V.error*alpha.value)
    QeA = abs(V.value*alpha.error)
    QeW = abs(W.error*Ppr.value)
    QeP = abs(Ppr.error*W.value)
    return lf.value(QdVal,np.sqrt(QeV**2+QeA**2+QeW**2+QeP**2))
def exp1():
    time,pressure = readData('pressureByTimeData.txt')
    timeByPres = interp1d([i.value for i in time],[i.value for i in pressure],kind = 'cubic')
    timeAxes = np.arange(start = 0,stop = time[-1].value,step = (10**-2))
    pressureInterpolated = [timeByPres(t) for t in timeAxes]
    plt.xlabel('Время [с]')
    plt.ylabel('Давление [Па]')
    plt.xticks(np.arange(0,100,1))
    plt.yticks(np.arange(0,0.2,0.005))
    plt.grid()
    plt.plot(timeAxes,pressureInterpolated)
    lf.plotValues(time,pressure)
    lf.makeTable([time,pressure],["t","P"],['c','Pa'])
    plt.show()
def exp2():
    time,pressure = readData('pressureBytimeData2.txt')
    timeByPres = interp1d([i.value for i in time],[i.value for i in pressure],kind = 'cubic')
    timeAxes = np.arange(start = 0,stop = time[-1].value,step = (10**-2))
    pressureInterpolated = [timeByPres(t) for t in timeAxes]
    a,b = lf.MNK(time[4:len(time)-5:1],pressure[4:len(time)-5:1])
    yLine = [a.value*x+b.value for x in timeAxes]
    Q = countQ(a,lf.value(0.78289807,0.041316071))
    a.print("KoefNaklona")
    print()
    Q.print("[litr*Pa]")
    plt.plot(timeAxes,yLine,'--')
    plt.xlabel('Время [с]')
    plt.ylabel('Давление [Па]')
    plt.xticks(np.arange(0,100,2))
    plt.yticks(np.arange(0,0.2,0.005))
    plt.grid()
    plt.plot(timeAxes,pressureInterpolated)
    lf.plotValues(time,pressure)
    lf.makeTable([time,pressure],["t","P"],['c','Pa'],'table2.txt')
    plt.show()

