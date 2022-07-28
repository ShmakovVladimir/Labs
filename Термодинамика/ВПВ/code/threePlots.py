import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
data = [[27.67,5.43,0.762,0.143],
        [21.3571428, 7.92857142, 3, 1.714285714],
        [20.57142857, 7.285714286, 3.928571429, 2.214285714]]

height = 6.5/100 #высота сосуда в метрах
xForInterpolation = np.linspace(height/8,height-height/8,4)
ax,fig = plt.subplots()
for i in range(3):
    yForInterpolation = data[i]
    func = interp1d(xForInterpolation,yForInterpolation,kind = 'quadratic')
    X = np.linspace(height/8,height-height/8,1000)
    Y = func(X)
    if i == 0:
        color = 'blue'
    elif i == 1:
        color = 'green'
    else:
        color = 'red'
    plt.plot(X,Y,label = 'Эксперимент '+str(i+1),color = color)
plt.xlabel('Высота [м]')
plt.ylabel('Количество молекул')
ax.legend(loc = 'upper right')
plt.show()

