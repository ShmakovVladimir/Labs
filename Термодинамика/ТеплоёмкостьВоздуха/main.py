import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import pandas as pd


def expData(expNum: int)->dict:
    data_1 = {"Сила тока": np.array([115,127,141,156,171])*(10**(-3)),
            "Напряжение": np.array([4,4.51,5,5.5,6]),
            "ЭДС": np.array([70,89,110,135,164]),
            "Расход": 0.21*(10**(-3))}
    data_2 = {"Сила тока": np.array([114,127,137,141,151,163,168,175])*(10**(-3)),
            "Напряжение": np.array([4.05,4.51,4.85,5.03,5.36,5.78,5.95,6.21]),
            "ЭДС": np.array([129,172,196,212,242,281,300,327]),
            "Расход": 0.105*(10**(-3))}
    with open('results/data1.txt','w') as f:
        f.write(pd.DataFrame(data_1).to_markdown())
    with open('results/data2.txt','w') as f:
        f.write(pd.DataFrame(data_2).to_markdown())
    if expNum-1:
        return data_2
    return data_1

def countHeatCapasity(data: dict):
    airDensity = 1.2754
    beta = 40.7
    deltaTemp = data["ЭДС"]/beta #разность температур
    massPerSecond = airDensity*data["Расход"] #масса воздуха, протекающая через калориметр в единицу времени
    power = data["Напряжение"]*data["Сила тока"] #мощность нагревателя

    MNK = linregress(power,deltaTemp*massPerSecond)
    xLine = np.linspace(power[0],power[-1],1000)
    yLine = MNK.slope*xLine+MNK.intercept
    print(MNK.slope)

    HeatCapasity = MNK.slope*32*(10**3)
    print(HeatCapasity)

    fig,ax = plt.subplots()
    plt.plot(xLine,yLine,':',label = r'МНК $\alpha = ' + str(MNK.slope)+'\pm'+str(MNK.stderr)+'$')
    plt.errorbar(power,deltaTemp*massPerSecond,fmt='o')
    plt.xticks(np.linspace(xLine[0],xLine[-1],len(power)*5))
    plt.yticks(np.linspace(yLine[0],yLine[-1],len(power)*5))
    ax.legend(loc = 'lower right')
    plt.show()

for expNum in [1,2]:
    countHeatCapasity(expData(expNum))
