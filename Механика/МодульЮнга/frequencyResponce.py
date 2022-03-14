import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np
division = 50*(10**(-3))
class freqAmp:
    global division
    def __init__(self,freqAmp :str):
        self.freq = float(freqAmp.split()[0]) 
        self.amp = division*float(freqAmp.split()[1])

dataPath = 'freqResponceData.txt'
data = open(dataPath)
ampbyFreq = []
freqError,ampError = [],[]
amps = []
for line in data:
    ampbyFreq.append(freqAmp(line))
    amps.append(float(division*float(line.split()[1])))
ampbyFreq.sort(key = lambda x: x.freq)



x=np.array([i.freq for i in ampbyFreq])
y=np.array([i.amp for i in ampbyFreq])
ampTimesSqr = [max(amps)/(2**.5) for _ in x]
cubic_interploation_model = interp1d(x, y, kind = "cubic")

# Plotting the Graph
X_=np.linspace(x.min(), x.max(), 500)
Y_=cubic_interploation_model(X_)

plt.plot(X_, Y_)
plt.plot(x,ampTimesSqr)
plt.title("frequency responce")
plt.xlabel("freq[hz]")
plt.ylabel("amp[V]")
#plt.xticks([i/10 for i in range(41315,41354,2)])
#plt.yticks([i/100 for i in range(20,47)])
plt.grid()
plt.show()


