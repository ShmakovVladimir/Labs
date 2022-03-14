g = 9.81
class value:
    def __init__(self,value,error) -> None:
        self.value, self.error = value,error
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
    xAverage,yAverage,xyAverage,xSqrAverage,ySqrAverage = sum(x)/4,sum(y)/4,0,0,0
    for i in range(len(x)):
        xyAverage+=x[i]*y[i]
        xSqrAverage+=x[i]**2
        ySqrAverage+=y[i]**2
    xyAverage/=4
    xSqrAverage/=4
    ySqrAverage/=4
    b_k = (xyAverage-xAverage*yAverage)/(xSqrAverage-xAverage**2)
    a_k = yAverage - b_k*xAverage

    sigmaB = (1/4)*(((ySqrAverage-yAverage**2)/(xSqrAverage-xAverage**2)-b_k**2)**.5)
    sigmaA = sigmaB*((xSqrAverage-xAverage**2)**.5)
    b,a = value(b_k,sigmaB),value(a_k,sigmaA)
    return b,a
def sigmaSl(x: list):
    speedAverage = sum([i.value for i in x])/len(x)
    sigmaSl = ((sum([(speedAverage-i.value)**2 for i in x]))**.5)/(len(x)-1)
    spAverage = value(speedAverage,sigmaSl)
    return spAverage