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
        pressure.append(lf.value(p*(10**d),1*(10**-6)))
    for i in range(len(time)):
        time[i]-=time[0]
    return time,pressure


