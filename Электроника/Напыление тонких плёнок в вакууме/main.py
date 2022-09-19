import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def plotData(filePath: str)->None:
    waveLengthData, ampData = [], []
    data = open(filePath)
    for line in data:
        dataPeace = line.split("\t")
        waveLengthData.append(float(dataPeace[0].split(',')[0]))
        if len(dataPeace[0].split(','))-1:
            waveLengthData[-1]+=float(dataPeace[0].split(',')[1])/np.power(10,len(dataPeace[0].split(',')[1]))
        ampData.append(float(dataPeace[1].split(',')[0]))
    waveLengthData = np.array(waveLengthData)
    ampData = np.array(ampData)
    x = np.linspace(waveLengthData[0]+0.1,waveLengthData[-1]-0.1,len(waveLengthData)*5)
    y = interp1d(waveLengthData,ampData,kind = "quadratic")(x)
    plt.plot(x,y)
    plt.show()

plotData("2.txt")