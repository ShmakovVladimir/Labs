import laba_functions as lf
import matplotlib.pyplot as plt
import math
import csv 
from scipy.interpolate import interp1d
def countD(voltage: list,time: list)->lf.value:
    logVoltage = [math.log(i) for i in voltage]
    deltaLogVoltage = [logVoltage[0]-logVoltage[i] for i in range(len(logVoltage))]
    a,_ = lf.MNK(time,deltaLogVoltage)
    a.print("A deltaLog")
    V = lf.value(1200,30)
    LbyS = lf.value(5.5,0.5)
    DValue = a.value*V.value*LbyS.value/2
    DerrLbyS = abs(LbyS.error*DValue/LbyS.value)
    DerrV = abs(V.error*DValue/V.value)
    DerrA = abs(a.error*DValue/a.value)
    return lf.value(DValue/(100**2),math.sqrt(DerrA**2+DerrV**2+DerrLbyS**2)/(100**2))
def readData(path :str):
    file = open(path)
    data = csv.DictReader(file)
    time,voltage = [],[]
    for line in data:
        time.append(float(line['t (s)']))
        voltage.append(float(line['V (mV)'])/(10**3))
    return time,voltage
def count(voltage: list,time: list)->tuple:
    voltage = [math.log(i) for i in voltage]
    return lf.MNK(time,voltage)
colors = ['#ff9302','#ffb701','#5586a6','#3d5a68','#212b2d']
Pressure = [1/(40*133.3+i*40*133.3) for i in range(5)]
Diffusion = []
for i in range(5):
    t,v = readData(str(i+1)+".csv")
    voltage,time = v,t
    v.pop(0)
    while t.pop(0)<5:   v.pop(0)
    a,b = count(voltage,time)
    D = countD(voltage,time)
    Diffusion.append(D)
    print()
    print("Experiment: "+str(i+1))
    D.print('Diffuzion coefficient')
    a.print("coefficient a")
    b.print("coefficient b")
    plt.yscale('log')
    plt.errorbar(x = t,
                 y = v,
                 color = colors[i])
xT = [i*10 for i in range(0,75,5)]
plt.xticks(xT)
plt.grid()
plt.show()
plt.figure()
aLine,bLine = lf.MNK(Pressure,Diffusion)
xLine = [i/1000 for i in range(math.floor(Pressure[-1]*1000),math.ceil(Pressure[0]*1000+100))]
yLine = [aLine.value*x+bLine.value for x in xLine]
plt.errorbar(x = Pressure,
             y = [d.value for d in Diffusion],
             xerr = [0 for _ in Pressure],
             yerr = [d.error for d in Diffusion],
             fmt = "_")
plt.plot(xLine,yLine)
plt.show()



    
