
import laba_functions as lf
import matplotlib.pyplot as plt
import math
Wy,Mx = [],[]
freqs = []
class Cyl:
    def __init__(self):
        self.T = lf.sigmaSl([lf.value(4.025,0.001),lf.value(4.019,0.001),lf.value(4.030,0.001)])
        self.r = lf.value(7.8/200,0.1/100)
        self.m = lf.value(1618/1000,.5/1000)
        self.I = lf.value(self.m.value*(self.r.value**2)/2,(self.m.value*(self.r.value**2)/2)*(((self.m.relErorr()**2) + 4*(self.r.relErorr()**2))**.5))
        self.I.print("Момент инерции цилиндра")
cylynder = Cyl()
class rot:
    def __init__(self):
        self.T = lf.sigmaSl([lf.value(3.194,0.001),lf.value(3.193,0.001),lf.value(3.195,0.001)])
        Iv = cylynder.I.value*((self.T.value/cylynder.T.value)**2)
        Ie = Iv*((cylynder.I.relErorr()**2 + 4*(self.T.relErorr()**2)+4*(cylynder.T.relErorr()**2))**.5)
        self.I = lf.value(Iv,Ie)
        self.I.print("Момент инерции ротора")
rotor = rot()
class experiment:
    global Wy,Mx,freqs
    def __init__(self,num: int,mass: lf.value,quantity: int,time: lf.value):
        self.length = lf.value(0.12,0.001)
        self.num,self.mass,self.q,self.time = num,mass,quantity/2,time
        self.countPeriod()
        self.countWo()
        self.countM()
        self.countFreq()
        self.countWc()
        freqs.append(self.Freq)
        self.countMtr()
        Wy.append(self.Wo)
        Mx.append(self.M)
        self.print()
    def print(self):
        print()
        print("Номер эксперемнета: "+str(self.num))
        print()
        self.Wo.print("Угловая скорость регулярной процессии")
        self.M.print("Момент силы")
        self.Freq.print("Частота")
        self.Wc.print("Угловая скорость опускания")
        self.Mtr.print("Момент силы трения")
        print()
    def countPeriod(self):
        Tv = self.time.value/self.q
        Te = self.time.error/self.q
        self.T = lf.value(Tv,Te)
    def countWo(self):
        Wv = 2*math.pi*self.q/self.time.value
        We = 2*math.pi*self.q*self.T.relErorr()/self.T.value
        self.Wo = lf.value(Wv,We)
    def countM(self):
        Mv = self.mass.value*lf.g*self.length.value
        Me = Mv*(((self.mass.relErorr()**2)+(self.length.relErorr()**2))**.5)
        self.M = lf.value(Mv,Me)
    def countFreq(self):
        frV = self.M.value/(self.Wo.value*rotor.I.value*2*math.pi)
        frE = frV*(((self.M.relErorr()**2)+(self.Wo.relErorr()**2)+(rotor.I.relErorr()**2))**.5)
        self.Freq = lf.value(frV,frE)
    def countWc(self):
        self.Wc = lf.value(math.pi/(18*self.time.value),self.time.error*math.pi/((18*self.time.value)**2))
    def countMtr(self):
        MtrV = self.Wc.value*self.Freq.value*2*math.pi*rotor.I.value
        MtrE = MtrV*((0.1**2+self.Freq.relErorr()**2+rotor.I.relErorr()**2)**.5)
        self.Mtr = lf.value(MtrV,MtrE)
    
exp,DATA = [],open('data.txt')
DATA.readline()
for line in DATA:
    num,mass,q,time = line.split(' ')
    mass = lf.value(float(mass.split(',')[0]),float(mass.split(',')[1]))
    num,q = int(num),int(q)
    time = lf.value(float(time.split(',')[0]),float(time.split(',')[1]))
    exp.append(experiment(num,mass,q,time))
b_k,a_k = lf.MNK([i.value for i in Mx],[i.value for i in Wy])
lx = [i/100 for i in range(45)]
ly = [(b_k.value)*i+a_k.value for i in lx]

print()
b_k.print("Коэффициент b")
a_k.print("Коэффициент a")
print()
lf.sigmaSl(freqs).print("Среднее значение частоты")
plt.plot(lx,ly)
#plt.plot(lx,[(b_k.value+b_k.error)*i+(a_k.value+a_k.error) for i in lx], linestyle = '-.',color = 'Red')
#plt.plot(lx,[(b_k.value-b_k.error)*i+a_k.value+a_k.error for i in lx], linestyle = '-.',color = 'Red')
#plt.plot(lx,[(b_k.value+b_k.error)*i+(a_k.value-a_k.error) for i in lx], linestyle = '-.',color = 'Red')
#plt.plot(lx,[(b_k.value-b_k.error)*i+a_k.value-a_k.error for i in lx], linestyle = '-.',color = 'Red')
plt.xticks([i/100 for i in range(0,45,2)])
plt.yticks([i/100 for i in range(25)])
plt.grid()
plt.errorbar(x=[i.value for i in Mx],y=[i.value for i in Wy],yerr = [i.error for i in Wy],xerr=[i.error for i in Mx],fmt='_')
for i in range(len(exp)):
    plt.annotate(str(exp[i].num),(Mx[i].value,Wy[i].value) )
#plt.annotate(str(len(exp)),(Mx[len(exp)-1].value,Wy[len(exp)-1].value-20*Wy[len(exp)-1].error) )
plt.show()
        