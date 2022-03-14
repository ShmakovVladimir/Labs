from numpy import average
import laba_functions as lf
import matplotlib.pyplot as plt

r = lf.value((1.3/2)/(10**3),0.01/(10**3))

def countP(pDataPath: str) -> list:
    data = open(pDataPath)
    pressure = []
    for i in data:
        pressure.append(lf.value(0.2*9.8*float(i),0.2*9.8*.5))
    return pressure
def countSigma(pressures: list)-> tuple:
    sigma = []
    for k,i in enumerate(pressures):
        value = i.value*r.value/2
        error = abs(i.value*r.error/2)+abs(i.error*r.value)/2
        sigma.append(lf.value(value,error))
        print()
        print(k+1)
        i.print("Разность давлений ")
        sigma[-1].print("Кф поверностного натяжения спирта ")
        print()
    result = lf.sigmaSl(sigma)
    print()
    print("Случайная ошибка"+str(result.error))
    result.error+=(average([i.error for i in sigma])/average([i.value for i in sigma]))*result.value
    print()
    result.print("Результат")
    print()
    return sigma,result
spirtSigma,res = countSigma(countP("spirtdeltaP.txt"))

    



