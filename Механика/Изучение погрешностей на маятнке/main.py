import math
import matplotlib.pyplot as plt

class value:
    def __init__(self,value,error) -> None:
        self.value, self.error = value,error
    def print(self,name: str):
        print(name+': '+str(self.value)+' +/- '+str(self.error))
    def relErorr(self):
        return self.error/self.value
class kernel:
    def __init__(self,length,mass) -> None:
        self.l , self.m = length,mass
Kernel = kernel(value(1,0.001),value(870.9,0.1))
prism_mass = value(69.2,0.1)
Uabs,Vord,UabsErorr,VordError,Ord,Abs,OrdError,AbsError= [],[],[],[],[],[],[],[]
#для метода наименьших квадратов
UabsSquare = []
class experiment:
    global Kernel,prism_mass
    global Uabs,Vord,UabsErorr,VordError,Ord,Abs,OrdError,AbsError
    global UabsSquare
    def __init__(self,number : int,x_cm :value,x_cs :value, timeData , n = 20) -> None:
        self.number , self.x_cm , self.x_cs, self.timeData, self.n = number , x_cm , x_cs, timeData, n 
        #среднее время и случайная погрешность измерения времени:
        self.AllAboutTime()
        self.countPeriod()
        self.count_g()
        self.Info()
        self.for_graph()

    def for_graph(self):
        U = self.x_cm.value*(self.T.value**2)
        V = self.x_cs.value**2
        Uerror = U*((self.x_cm.relErorr()**2+(2*self.T.relErorr())**2)**0.5)
        Verror = V*(((2*self.x_cs.relErorr())**2)**0.5)
        Uabs.append(U)
        Vord.append(V)
        UabsErorr.append(Uerror)
        VordError.append(Verror)
        UabsSquare.append(U**2)
        Ord.append(self.T.value)
        OrdError.append(self.T.error)
        Abs.append(self.x_cm.value)
        AbsError.append(self.x_cm.error)
    def countPeriod(self):
        self.T = value(self.Time.value/self.n , self.Time.error/self.n)
    def count_g(self):
        up = ((Kernel.l.value)**2)/12 + self.x_cs.value**2
        down = self.x_cm.value*(self.T.value**2)*(1+prism_mass.value/Kernel.m.value)
        g = (math.pi**2)*4*up/down
        g_error = (((2*Kernel.l.relErorr())**2+(2*self.x_cs.relErorr())**2+self.x_cm.relErorr()**2+(2*self.T.relErorr())**2+prism_mass.relErorr()**2+Kernel.m.relErorr()**2)**0.5)*g
        self.g = value(g,g_error)

    def AllAboutTime(self):
        sigma = 0
        for i in self.timeData: sigma+=i
        tAverage = sigma/len(self.timeData)
        sigma = 0
        for i in self.timeData: sigma+=(i-tAverage)**2
        self.Time = value(tAverage,((1/(len(self.timeData)-1)*sigma)**(0.5)))
    def Info(self):
        print("Номер опыта: "+str(self.number))
        self.Time.print("Время")
        self.g.print("Ускоерение свободного падения")
        self.T.print("Период")
        print("Отклонение от табличного значения: "+str(100*abs(9.81-self.g.value)/9.81)+' %')
        print("Погрешность g в процентах: "+str(self.g.relErorr()*100)+" %")


#--------ДАННЫЕ---------
exp = []
exp.append(experiment(1,value(0.359,0.001),value(0.39,0.001),[31.29,31.23,31.11,31.5,30.96]))
exp.append(experiment(2,x_cs = value(0.3,0.001),x_cm=value(0.277,0.001),timeData=[30.34,30.41,30.24]))
exp.append(experiment(3,x_cs = value(0.09,0.001),x_cm = value(0.084,0.001),timeData=[39.75,39.75,39.62]))
exp.append(experiment(4,x_cs=value(0.05,0.001),x_cm=value(0.043,0.001),timeData=[53.3,53.29,52.95]))
exp.append(experiment(5,x_cs = value(0.25,0.001),x_cm=value(0.23,0.001),timeData=[30.61,30.71,30.7]))
exp.append(experiment(6,x_cs=value(0.48,0.001),x_cm=value(0.444,0.001),timeData=[32.58,32.58,32.8]))
exp.append(experiment(7,x_cs = value(0.36,0.001),x_cm = value(0.332,0.001),timeData=[30.91,30.85,30.78]))
exp.append(experiment(8,x_cs=value(0.16,0.001),x_cm=value(0.139,0.001),timeData=[34.08,33.82,33.91]))





g_average = 0
for i in exp:  g_average+=i.g.value
g_average/=8



print('\n'+str(g_average))
plt.style.use('ggplot')

#метод наименьших квадратов
multVU = sum([Uabs[i]*Vord[i] for i in range(len(Uabs))])
multAverage,UabsAverage,VordAverage,UabsSquareAverage = multVU/len(Uabs),sum(Uabs)/len(Uabs),sum(Vord)/len(Vord),sum(UabsSquare)/len(UabsSquare)
bLine = (multAverage-UabsAverage*VordAverage)/(UabsSquareAverage-UabsAverage**2)

aLine = VordAverage - bLine*UabsAverage

aParabolic,bParabolic,cParabolic,xpar= -1084,624,75.45974,[i/10000 for i in range(-1000,4600)]
cXparabolic,cYparabolic = [i/100 for i in range(-10,40)],[i/100 for i in range(150,310)]
ypar = [aParabolic*(i**2)+bParabolic*i+cParabolic for i in xpar]
#метод наименьших квадратов для параболы 
print("x^2: "+str(sum([i**2 for i in Abs])))
print("x: "+str(sum(Abs)))
print("y: "+str(sum(Ord)))
print("x^3: "+str(sum([i**3 for i in Abs])))
print("xy: "+str(sum([Abs[i]*Ord[i] for i in range(len(Abs))])))
print("x^4: "+str(sum([i**4 for i in Abs])))
print("x^2 y: "+str(sum([(Abs[i]**2)*Ord[i] for i in range(len(Abs))])))




print('\n'+str(bLine))
plt.errorbar(Uabs, Vord, yerr=VordError ,xerr=UabsErorr,fmt='_')
#plt.errorbar(Abs, Ord, yerr=OrdError ,xerr=AbsError,fmt='_')
for i in range(len(exp)):
    a = ''+str(i+1)
    plt.annotate(a,(Uabs[i],Vord[i]))
cX , i , cY , y ,lineY ,lineX= [] , 0 ,[],0 ,[],[]

while i<1.25: 
    if i<1:
        lineY.append(aLine+bLine*(i+0.27))
        lineX.append(i+0.27)

    cX.append(i)    
    i+=0.04


#plt.plot(lineX,lineY)
plt.plot(xpar,ypar)
while y<0.26: 
    cY.append(y) 
    y+=0.01 
#plt.xticks(cX)
#plt.yticks(cY)
#plt.xticks(cXparabolic)
#plt.yticks(cYparabolic)
plt.xlabel("U")
plt.ylabel("V")
plt.show() 