import matplotlib.pyplot as plt
import math
class Constants:
    def __init__(self):
        self.atmPressure = 101325
        self.HGdensity = 13600
        self.g = 9.81
        self.mmHg = 133.3223684 #миллиметр ртутного столба
        self.R = 8.31446261815324
        self.MH2O = 18/(10**3)
class value:
    def __init__(self,value,error) -> None:
        self.value, self.error = value,error
    def __isub__(self,other)->None:
        self.value-=other.value
        self.error+=other.error
    def print(self,name: str,num = -1):
        if num == -1:
            print(name+': '+str(self.value)+' +/- '+str(self.error))
        else:
            print('Эксперимент: '+str(num)+' '+name+': '+str(self.value)+' +/- '+str(self.error))
    def relErorr(self):
        return self.error/self.value
    def round(self):
        error = str(self.error)
        i = j = 0
        while i<len(error) and error[i]!='.':   i+=1
        while i+j<len(error) and error[i+j]!='0':   j+=1
        return value(round(self.value,j+i),round(self.error,j+i))
def MNK(x,y):
    fMemA = len(x)*sum([x[i]*y[i] for i in range(len(x))])
    sMemA = sum(x)*sum(y)
    tMemA = len(x)*sum([x[i]**2 for i in range(len(x))])
    lMemA = sum(x)**2
    a = (fMemA-sMemA)/(tMemA-lMemA)
    fMemB = sum(y)
    sMemB = a*sum(x)
    b = (fMemB-sMemB)/len(x)
    yAverage = sum(y)/len(y)
    ySqrAverage = sum([y[i]**2 for i in range(len(y))])/len(y)
    xAverage = sum(x)/len(x)
    xSqrAverage = sum([x[i]**2 for i in range(len(x))])/len(x)
    sigma = len(x)*(ySqrAverage-(yAverage**2)-(a**2)*(xSqrAverage-(xAverage**2)))/(len(x)-2)
    sigmaSqrA = sigma/(len(x)*(xSqrAverage-(xAverage**2)))
    sigmaSqrB = sigmaSqrA*xSqrAverage
    a,b = value(a,(sigmaSqrA**.5)),value(b,(sigmaSqrB**.5))
    return a,b
def sigmaSl(x: list):
    speedAverage = sum([i.value for i in x])/len(x)
    sigmaSl = ((sum([(speedAverage-i.value)**2 for i in x]))**.5)/(len(x)-1)
    spAverage = value(speedAverage,sigmaSl)
    return spAverage
def plotValues(x: list,y: list,grid = False,xTick = 20,yTick=20):
    if grid:
        plt.xticks([i for i in range(math.floor(min([i.value/xTick for i in x]))*xTick,math.floor(max([i.value for i in x]))*xTick)])
        plt.yticks([i for i in range(math.floor(min([i.value/yTick for i in y]))*yTick,math.floor(max([i.value for i in y]))*yTick)])
        plt.grid()
    plt.errorbar(x = [i.value for i in x],
                 y = [i.value for i in y],
                 xerr = [i.error for i in x],
                 yerr = [i.error for i in y],
                 fmt = '_')
    plt.show()
const = Constants()
