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


time,pressure = readData('pressureBytimeData2.txt')
timeByPres = interp1d([i.value for i in time],[i.value for i in pressure],kind = 'cubic')
timeAxes = np.arange(start = 0,stop = time[-1].value,step = (10**-2))
pressureInterpolated = [timeByPres(t) for t in timeAxes]
plt.xlabel('Время [с]')
plt.ylabel('Давление [Па]')
plt.xticks(np.arange(0,100,2))
plt.yticks(np.arange(0,0.2,0.005))
plt.grid()
plt.plot(timeAxes,pressureInterpolated)
lf.plotValues(time,pressure)
lf.makeTable([time,pressure],["t","P"],['c','Pa'])
plt.show()

