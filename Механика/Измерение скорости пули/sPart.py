import laba_functions as lf
import matplotlib.pyplot as plt
from math import pi
class peng:
    def __init__(self,mass1: lf.value,mass2: lf.value,periodWithMass: lf.value,periodNoMass: lf.value,R: lf.value,r: lf.value,d: lf.value):
        self.m1,self.m2,self.wM,self.noM = mass1,mass2,periodWithMass,periodNoMass
        self.R,self.r,self.d = R,r,d
        self.count_inertion()
    def count_inertion(self):
        sigmaM1 = self.m1.error*(1+self.m2.value)*(self.R.value**2)
        sigmaM2 = self.m2.error*(1+self.m1.value)*(self.R.value**2)
        sigmaR = 2*self.R.error*self.R.value*(self.m1.value+self.m2.value)
        self.I = lf.value((self.R.value**2)*(self.m1.value+self.m2.value),(sigmaM1**2+sigmaM2**2+sigmaR**2)**.5)
        self.I.print("Момент инерции")
tm10,tm15 = 60*3/10,(4*60+28)/15 #время 10 и 15 колебаний маятника с грузами
tn10,tn15 = (60*2+3)/10,(60*3+12)/15 #время 10 и 15 колебаний маятника без грузов
periodWithMass = lf.value((tm10+tm15)/2,(0.5*((tm10-(tm10+tm15)/2)**2+(tm15-(tm10+tm15)/2)**2))**.5)
periodNoMass = lf.value((tn10+tn15)/2,(0.5*((tn10-(tn10+tn15)/2)**2+(tn15-(tn10+tn15)/2)**2))**.5)
periodWithMass.print("Период маяника с грузами")
periodNoMass.print("Период маятника без грузов")

pen = peng(lf.value(713.9/1000,2/1000),lf.value(714.1/1000,2/1000),periodWithMass,periodNoMass,lf.value(0.335,0.005),lf.value(0.225,0.001),lf.value(0.45,0.005))

bulletMass = [0.498,0.503,0.513,0.508]
amps = [10.75,11,10.75,10.875]
speed = []
for i in range(len(bulletMass)):
    m = bulletMass[i]/1000
    x = amps[i]/1000
    u = 10*(4*pi*x*pen.m1.value*(pen.R.value**2)*pen.wM.value)/(2*pen.d.value*m*pen.r.value*(pen.wM.value**2-pen.noM.value**2))
    ut1Up = 2*pi*x*pen.m1.value*(pen.R.value**2)*pen.d.value*m*pen.r.value*(pen.wM.value**2+pen.noM.value**2)
    ut1Down = ((pen.wM.value**2-pen.noM.value**2)*pen.r.value*pen.m1.value*pen.d.value*2)**2
    sigmat1 = pen.wM.error*ut1Up/ut1Down
    ut2Up = pen.wM.value*pen.noM.value*pen.m1.value*2*pi*x*(pen.R.value**2)
    ut2Down = pen.d.value*pen.m1.value*pen.r.value*(pen.wM.value**2-pen.noM.value**2)
    sigmat2 = pen.noM.error*ut2Up/ut2Down
    uerror = (sigmat1**2+sigmat2**2+(u**2)*((0.0005/x)**2+pen.m1.relErorr()**2+pen.R.relErorr()**2+pen.d.relErorr()**2+pen.r.relErorr()**2))**.5
    speed.append(lf.value(u,uerror))
    speed[i].print("Скорость пули",i+5)
speedAverage = sum([i.value for i in speed])/len(speed)
sigmaSl = ((sum([(speedAverage-i.value)**2 for i in speed]))**.5)/len(speed)
spAverage = lf.value(speedAverage,sigmaSl)
spAverage.print("Среднее значения и случайная погрешность")
b,a = lf.MNK(bulletMass,[i.value for i in speed])
b.print("Коэффициент b")
a.print("Коэффициент a")
lineX = [i/10000 for i in range(4970,5190)]
lineY = [a.value+b.value*i for i in lineX]
plt.errorbar([i for i in bulletMass],[i.value for i in speed],xerr=[0.00005,0.00005,0.00005,0.00005],yerr=[i.error for i in speed],fmt='_')
plt.ylim(105,128)
plt.xticks([i/1000 for i in range(497,520)])
plt.yticks([i for i in range(105,128)])
plt.grid()
plt.plot(lineX,lineY)
plt.show()



