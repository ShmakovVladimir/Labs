import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

def readData(path):
    data = open(path)
    layerSum = np.array([0 for _ in range(4)])
    expQ = 0
    for line in data:
        expQ+=1
        layer = np.array(list(map(int,line.split("  "))))
        layerSum = layer+layerSum
    layerSum = layerSum/expQ
    print(layerSum)
    return layerSum


height = 6.5/100 #высота сосуда в метрах

# data = readData('dataV2.txt')
data = np.array([20.57,7.29,3.93,2.214])
heightAxes = np.linspace(0,height,1000)
moleculsAxes = []
for i in range(4):
    moleculsAxes += [data[i]]*(len(heightAxes)//4)

xForInterpolation = np.linspace(height/8,height-height/8,4)




func = interp1d(xForInterpolation,data,kind = 'quadratic')

X = np.linspace(height/8,height-height/8,1000)
Y = func(X)
fig,ax = plt.subplots()
ax.set_title("Три четверти максимальной температуры")
plt.xlabel('Высота [м]')
plt.ylabel('Количество молекул')
plt.plot(heightAxes,moleculsAxes,'-', label = 'Эксперемнтальный график')

plt.plot(X,Y,'--',label = "Интерполяция")
ax.legend(loc = 'upper right')
plt.show()
