from cProfile import label
import laba_functions as lf
import matplotlib.pyplot as plt
import math
import csv 
from scipy.interpolate import interp1d
def countD(voltage: list,time: list)->tuple:
    logVoltage = [math.log(i) for i in voltage]
    a,_ = lf.MNK(time,logVoltage)
    processTime = lf.value(-1/a.value,abs(a.error/(a.value**2)))
    V = lf.value(1200,30)
    LbyS = lf.value(5.5,0.5)
    DValue = V.value*LbyS.value/(2*processTime.value)
    DerrLbyS = abs(LbyS.error*DValue/LbyS.value)
    DerrV = abs(V.error*DValue/V.value)
    DerrT = abs(processTime.error*DValue/processTime.value)
    return lf.value(DValue/(100**2),math.sqrt(DerrT**2+DerrV**2+DerrLbyS**2)/(100**2)),processTime
def countLength(D: lf.value)->lf.value:
    HeMolar = 0.004
    T = lf.value(20+273,1)
    vAverageVal = math.sqrt(8*lf.const.R*T.value/(math.pi*HeMolar))
    vAverageErr = T.error*0.5*vAverageVal/T.value
    vAverage = lf.value(vAverageVal,vAverageErr)
    length = lf.value(3*D.value/vAverage.value,
    math.sqrt((3*D.error/vAverage.value)**2+(3*D.value*vAverage.error/(vAverage.value**2))**2))
    return length
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
    D, processTime = countD(voltage,time)
    Diffusion.append(D)
    length = countLength(D)
    print()
    print()
    print("Experiment: "+str(i+1))
    a.print("coefficient a")
    b.print("coefficient b")
    print()
    D.print('Diffuzion coefficient')
    processTime.print("process time")
    print()
    length.print("Freedom dist")
    print()
    print("_____________________________________________________________")
    plt.yscale('log')
    plt.errorbar(x = t,
                 y = v,
                 color = colors[i],
                 label = 'Давление '+str(40+i*40)+ ' [торр]')
xT = [i*10 for i in range(0,75,5)]
yT = [math.log(i/10000) for i in range(1,1000,10)]
plt.xlabel("время [с]")
plt.ylabel("Логарифм напряжения [log(мв)]")
plt.xticks(xT)
plt.yticks(yT)
plt.legend()
plt.grid()
plt.show()
plt.figure()
aLine,bLine = lf.MNK(Pressure,Diffusion)
xLine = [i/1000 for i in range(math.floor(Pressure[-1]*1000),math.ceil(Pressure[0]*1000+100))]
yLine = [aLine.value*x+bLine.value for x in xLine]
xTline = [i/50000 for i in range(0,30)]
yTline = [i/10000 for i in range(0,50)]
plt.xticks(xTline)
plt.yticks(yTline)
plt.ylabel("Коэффициент диффузии [м^2/c]")
plt.xlabel('Обратное давление [Па^-1]')
plt.grid()
plt.errorbar(x = Pressure,
             y = [d.value for d in Diffusion],
             xerr = [0 for _ in Pressure],
             yerr = [d.error for d in Diffusion],
             fmt = "_")
plt.plot(xLine,yLine)
plt.show()



    
