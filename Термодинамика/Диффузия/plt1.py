import laba_functions as lf
import matplotlib.pyplot as plt
import math
import csv 
def cm_to_inch(value):
    return value/2.54
def readData(path :str):
    file = open(path)
    data = csv.DictReader(file)
    time,voltage = [],[]
    for line in data:
        time.append(float(line['t (s)']))
        voltage.append(float(line['V (mV)'])/(10**3))
    return time,voltage
colors = ['#ff9302','#ffb701','#5586a6','#3d5a68','#212b2d']
for i in range(5):
    t,v = readData(str(i+1)+".csv")
    voltage,time = v,t
    v.pop(0)
    while t.pop(0)<5:   v.pop(0)
    plt.yscale('log')
    plt.errorbar(x = t,
                 y = v,
                 color = colors[i])
xT = [i*10 for i in range(0,75,5)]
plt.xticks(xT)
plt.grid()
plt.show()



    
