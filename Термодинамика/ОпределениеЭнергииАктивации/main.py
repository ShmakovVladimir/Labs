import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stat
import pandas as pd

def readData(path: str,option = 'Metal')->tuple:
    data = open(path)
    line = data.readline()
    temp,diam = [],[]
    time1,time2 = [],[]
    for line in data:
        d,T,t1,t2 = map(float,line.split())
        if option == "Metal":
            if d<1.5:
                time1.append(t1)
                time2.append(t2)
                temp.append(T)
                diam.append(d)
        elif d>1.5:
            time1.append(t1)
            time2.append(t2)
            temp.append(T)
            diam.append(d)
    return np.array(temp)+273,np.array(diam),np.array(time1),np.array(time2)-np.array(time1)

def countViscosity(diam: np.array,time: np.array):
    length = 0.1 #длина трубки в метрах
    diam*=0.001 
    radius = diam/2 #радиус шарика в метрах
    radiusError = 0.01*0.001 #погрешность измереня радиуса - сотая миллиметра
    lengthError = 0.005 #погрешность линейки
    timeError = 0.7 #погрешность измерения времени вручную
    speed = length*np.power(time,-1)
    speedError = speed*lengthError/length+speed*timeError/time
    g = 9.81
    glycerolDensity = 1260 #плотность глицерина
    ballDensity = [] #плотность шариков из стали и стекла
    for i in time:
        if i<1.5:
            ballDensity.append(7.8*1000)
        else:
            ballDensity.append(2.5*1000)
    ballDensity = np.array(ballDensity)
    viscosity = 2*g*np.power(radius,2)*(ballDensity-glycerolDensity)/(speed*9)
    viscosityError = np.abs(viscosity*2*radiusError/radius) + np.abs(viscosity*speedError/speed)
    print(viscosity)
    print(viscosityError)
    return viscosity,viscosityError

def countActivationEnergy(temp: np.array,viscosity: np.array,filePath: str):
    boltsman = (10**(-23))*1.38
    cff = stat.linregress(1/temp,np.log(viscosity))
    W = boltsman*cff.slope
    Werr = boltsman*cff.stderr
    print(W)
    print(Werr)
    with open(filePath,'w') as f:
        f.write("Activation Energy: "+"$"+str(W)+r"\pm"+str(Werr)+"$")
    



metalT,metalD,time1,metalTime = readData('data.txt')
metalViscosity,metalViscosityError = countViscosity(metalD,metalTime) #считаем что скорость устанавливается после прохождения второй метки
glassT,glassD,time1,glassTime = readData('data.txt','glass')
glassViscosity,glassViscosityError = countViscosity(glassD,glassTime)

countActivationEnergy(glassT,glassViscosity,'ЭнергияАктивацииСтекло.txt')
countActivationEnergy(metalT,metalViscosity,'ЭнергияАктивацииМеталл.txt')

metalMNK = stat.linregress(1/metalT,np.log(metalViscosity)) #метод наименьших квадратов для металлических шариков
glassMNK = stat.linregress(1/glassT,np.log(glassViscosity)) #метод наименьших квадратов для стеклянных шариков

#Создание таблиц

metalData = {"Материал": r"Сталь $\ro = 7.8 g/cm^3$",
             r"$1/T$": 1/metalT,
             "$D$": metalD,
             "Время падения": metalTime,
             "$ln(\eta)$": np.log(metalViscosity)}
metalDataFrame = pd.DataFrame(data = metalData)
metalDataFrame.to_latex("metal.tex", index=False, caption="Металлические шарики",escape = False)
glassData = {"Материал": r"Стекло $\ro = 2.5 g/cm^3$",
             r"$1/T$": 1/glassT,
             "$D$": glassD,
             "Время падения": glassTime,
             "$ln(\eta)$": np.log(glassViscosity)}
glassDataFrame = pd.DataFrame(data = glassData)
glassDataFrame.to_latex("glass.tex", index=False, caption="Стеклянные шарики",escape = False)


#Построение графиков
fig,ax = plt.subplots()
ax.set_title(r"Зависимость $ln(\eta)$ от $\frac{1}{T}$")

plt.errorbar(1/metalT, #график для металлических шариков
             np.log(metalViscosity),
             xerr = 0.1*np.power(metalT,-2),
             yerr = metalViscosityError/metalViscosity,
             fmt="_",
             label = r"Металлические шарики")
plt.errorbar(1/glassT, #график для стеклянных шариков
             np.log(glassViscosity),
             xerr = 0.1*np.power(glassT,-2),
             yerr = glassViscosityError/glassViscosity,
             fmt="_",
             label = r"Стеклянные шарики")
xAxes = np.linspace(0.0030,0.0035,1000)

#Построение лучших прямых
plt.plot(xAxes,
         glassMNK.slope*xAxes+glassMNK.intercept,
         ':',
         label = r"МНК - стекло $a = "+str(int(round(glassMNK.slope/100,0)*100))+r"\pm"+str(int(round(glassMNK.stderr/100,0)*100))+"$")
plt.plot(xAxes,
         metalMNK.slope*xAxes+metalMNK.intercept,
         ":",
         label = r"МНК - металл $a = "+str(int(round(metalMNK.slope/100,0)*100))+r"\pm"+str(int(round(metalMNK.stderr/100,0)*100))+"$")

plt.xticks(np.arange(0.0030,0.0035,0.00005))
plt.yticks(np.arange(0,-5,-0.5))
ax.set_xlabel("$1/T$ [$K^{-1}$]")
ax.set_ylabel("$ln(\eta)$")
plt.grid()
ax.legend(loc = 'lower right',prop = {'size': 15})
plt.show()