import laba_functions as lf
import matplotlib.pyplot as plt

class Ballistic_pendillum:
    def __init__(self,mass: lf.value,length: lf.value):
        self.mass,self.len = mass,length
class fExp:
    def __init__(self,massBallet: lf.value,delta: lf.value,num):
        self.m,self.delta,self.num = massBallet,delta,num
        self.pend = Ballistic_pendillum(lf.value(3.225,0.0010),lf.value(2.215,0.005))
        self.countU()
    def countU(self):
        uValue = (self.delta.value*self.pend.mass.value/self.m.value)*((lf.g/self.pend.len.value)**.5)
        sigmaDelta = self.delta.error*(self.pend.mass.value/self.m.value)*((lf.g/self.pend.len.value)**.5)
        sigmaKernelMass = self.delta.value*(self.pend.mass.error/self.m.value)*((lf.g/self.pend.len.value)**.5)
        sigmaMassUp = self.m.error*self.pend.mass.value*self.delta.value*((lf.g)**.5)
        sigmaMassDown = ((self.m.value)**2)*((self.pend.len.value)**.5)
        sigmaMass = sigmaMassUp/sigmaMassDown
        sigmaLUp = self.pend.len.error*self.pend.mass.value*((lf.g)**.5)*self.delta.value
        sigmaLDown = 2*self.m.value*(self.pend.len.value**(1.5))
        sigmaL = sigmaLUp/sigmaLDown
        uError = ((sigmaDelta)**2+sigmaKernelMass**2+sigmaMass**2+sigmaL**2)**.5
        self.u = lf.value(uValue,uError)
        self.u.print("Скорость пули",self.num)
firstExp,yy,yerror = [],[],[]
bulletMass = [0.502,0.517,0.513,0.511,0.498,0.503,0.513,0.508]
deltaX = [10,9,9,9.5]

for i in range(len(deltaX)):
    firstExp.append(fExp(lf.value(bulletMass[i]/1000,0.000005),lf.value(deltaX[i]/1000,0.0005),i+1))
#Рассчет коэффициентов наклона по МНК:
xAverage,yAverage,xyAverage,xSqrAverage,ySqrAverage = sum(bulletMass[:4])/4,sum([i.u.value for i in firstExp])/4,0,0,0
for i in range(4):
    xyAverage+=bulletMass[i]*firstExp[i].u.value
    xSqrAverage+=bulletMass[i]**2
    ySqrAverage+=firstExp[i].u.value**2
xyAverage/=4
xSqrAverage/=4
ySqrAverage/=4
b_k = (xyAverage-xAverage*yAverage)/(xSqrAverage-xAverage**2)
a_k = yAverage - b_k*xAverage
lineX = [i/10000 for i in range(5000,5190)]
lineY = [a_k+b_k*i for i in lineX]
sigmaB = (1/4)*(((ySqrAverage-yAverage**2)/(xSqrAverage-xAverage**2)-b_k**2)**.5)
sigmaA = sigmaB*((xSqrAverage-xAverage**2)**.5)
b,a = lf.value(b_k,sigmaB),lf.value(a_k,sigmaA)
b.print("Коэффициент b")
a.print("Коэффициент a")
#Построение графика
for i in firstExp:
    yy.append(i.u.value)
    yerror.append(i.u.error)
plt.errorbar(bulletMass[:4],yy,xerr=[0.000005,0.000005,0.000005,0.000005],yerr = yerror,fmt='_')
lf.sigmaSl([i.u for i in firstExp]).print("Среднее значение скорости и случайная погрешность")
for i in range(len(deltaX)):
    plt.annotate(str(i+1),(bulletMass[i],yy[i]))
plt.ylim(105,150)
plt.plot(lineX,lineY)
plt.plot(lineX,[a_k+sigmaA+(b_k+sigmaB)*i for i in lineX])
plt.plot(lineX,[a_k-sigmaA+(b_k-sigmaB)*i for i in lineX])
plt.xticks([i/1000 for i in range(500,520)])
plt.yticks([i for i in range(105,151)])
plt.grid()
plt.show()