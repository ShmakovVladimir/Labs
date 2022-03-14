from numpy import average
import laba_functions as lf
import matplotlib.pyplot as plt
r = lf.value((1.3/2)/(10**3),0.01/(10**3))
ZEROpressure = "5 105 90 103 110"
def countPressure(TempAndPressure: str)-> tuple:
    variables = TempAndPressure.split()
    temp = lf.value(float(variables[0]),0.07)
    pressures = [lf.value(float(variables[i]),0) for i in range(1,len(variables))]
    pressure = lf.sigmaSl(pressures)
    return temp,pressure
def countSigma(dataPath: str):
    data = open(dataPath)
    _,Pzero = countPressure(ZEROpressure)
    Pzero.print("ДавлениеСнаружи")
    pressures,temp,sigma = [],[],[]
    for i in data:
        t,p = countPressure(i)
        #p.value-=Pzero.value
        #p.error+=Pzero.error
        pressures.append(p)
        temp.append(t)
        sigma.append(lf.value(p.value*r.value/2,abs(p.value*r.error/2)+abs(p.error*r.value)/2))
        print()
        t.print("Температура")
        p.print("Разность Давлений")
        sigma[-1].print("Сигма")
        print()
    return temp,sigma
t,s = countSigma("WaterTempAndPressure.txt")
a,b = lf.MNK([i.value for i in t],[i.value for i in s])
aUp,bUp = lf.MNK([i.value+i.error for i in t],[i.value+i.error for i in s])
aDown,bDown = lf.MNK([i.value-i.error for i in t],[i.value-i.error for i in s])
a.print("К/ф a")
b.print("К/Ф b")
q=[]
for i in t:
    print()
    q.append(lf.value(-i.value*a.value,(i.error*a.value+i.value*a.error)/5))
    q[-1].print("Теалота")
    print()
lf.plotValues(t,q)
# x = [i/10 for i in range(290,620)]
# yNorm = [a.value*i+b.value for i in x]
# yUp = [(aUp.value)*i+b.value for i in x]
# yDown = [(aDown.value)*i+b.value for i in x]
# plt.xticks([x[i] for i in range(0,len(x),10)])
# plt.yticks([i/1000 for i in range(63,71)])
# plt.grid()
# plt.plot(x,yNorm,color='purple')
# #plt.plot(x,yUp,color = 'red')
# #plt.plot(x,yDown,color = 'blue')
# lf.plotValues(t,s)



