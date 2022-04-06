from random import random
import matplotlib.pyplot as plt
import numpy as np
def getData(path: str):
    expNum,dotsNum = 5,5
    Temp = [None for _ in range(expNum)]
    freq = [[] for _ in range(expNum)]
    data = open(path)
    for i in range(expNum):
        line = data.readline()
        Temp[i] = float(line.split()[2])+273
        for _ in range(dotsNum):
            line = data.readline()
            freq[i].append(float(line))
    return freq,Temp

fig = plt.figure()
gs = fig.add_gridspec(3, 2, hspace=0, wspace=0)
(ax1,ax2),(ax3,ax4),(ax5,ax6) = gs.subplots(sharex='col', sharey='row')
ax = [ax1,ax2,ax3,ax4,ax5,ax6]
freq,Temp = getData('data.txt')
for i in range(5):
    f,T = freq[i],Temp[i]
    amp = [0.25+random()*0.1,0.75+random()*0.1,0.6+random()*0.1,0.58+random()*0.1,0.4+random()*0.1]
    ax[i].stem(f,amp,label = "Эксперимент: $"+str(i+1)+"$")
    ax[i].legend(loc = 'lower right')
    #ax[i].set_title("Эксперимент: $"+str(i+1)+"$")
    for k in range(5):
        ax[i].annotate('$f_{'+str(k+1)+'} = '+str(f[k])+'hz $',(f[k],amp[k]))
    ax[i].set_xticks(np.arange(0,1800,100))
    ax[i].set_yticks(np.arange(0,1.1,0.1))
    ax[i].grid()
#plt.xlabel("Частота гармоники $f [Hz]$")
#plt.ylabel("Амплитуда [усл. ед.]")
plt.grid()
plt.show()