import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
import scipy.constants as const

def Maxswell(speed: np.ndarray,temp: float = 273,mass: float = np.power(0.1,26))->np.ndarray:
    return 4*np.pi*np.power(speed,2)*np.power(mass/(2*np.pi*const.k*temp),1.5)*np.exp(-mass*np.power(speed,2)/(2*const.k*temp))


def updateValue(value: float):
    chanse = Maxswell(speed,value)
    ax.clear()
    ax.plot(speed,chanse)
    plt.draw()
speed = np.linspace(0,5000,9000)
tempInit = 273
chanse = Maxswell(speed)

fig,ax = plt.subplots()

ax.plot(speed,chanse)
ax_slider = plt.axes([0.1,0.1,0.8,0.05],facecolor = 'red')

slider = Slider(ax_slider,"tempreture [$K$]",valmin = 100,valmax = 1000,valstep = 5)
slider.on_changed(updateValue)

plt.show()