import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
pos = [[5.2,1.8],[4,1.75],[2.1,1.75],[1.2,1.1],[1,0.2],[0.6,0.01],[0.2,0],[0,0]]
posX = [pos[i][0] for i in range(len(pos))]
posY = [pos[i][1] for i in range(len(pos))]
print(posX)
print(posY)
xAx = np.linspace(0,5.2,100)

fCurve = interp1d(posX,posY,kind='cubic')


plt.plot(posX,posY,'o')
plt.plot(xAx,fCurve(xAx))
plt.show()
