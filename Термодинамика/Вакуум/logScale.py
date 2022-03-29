from re import L
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


time,pressure = readData('pressureByTimeData.txt')
logPressure = [lf.value(np.log(p.value),(p.error/p.value)) for p in pressure]
presbyTimeInter = interp1d([i.value for i in time],[i.value for i in logPressure],kind='cubic')
timeAxes = np.arange(start = 0,stop = time[-1].value,step = (10**-2))
pressureInterpolated = [presbyTimeInter(t) for t in timeAxes]
aLog,bLog = lf.MNK(time[3:8:1],logPressure[3:8:1])
a,b = lf.MNK(time,pressure)
yLine = [aLog.value*x+bLog.value for x in timeAxes]

aLog.print("Коэффициент a")
#plt.yscale('log')
plt.plot(timeAxes,pressureInterpolated)
plt.plot(timeAxes,yLine,"--")
plt.xlabel('Время [с]')
plt.ylabel('Логарифм Давления [ln(Па)]')
plt.xticks(np.arange(0,100,1))
plt.yticks([np.log(i/100) for i in range(1,1000)])
plt.grid()
lf.plotValues(time,logPressure)
plt.show()