import matplotlib.pyplot as plt
import laba_functions as lf
#Дюраль
#duralFr,po = [4262,8646.3,12825,17260],lf.value(2650,75) 


#Медь
#duralFr,po = [3219,6420,9610,12530],lf.value(8933,150)


#Сталь
duralFr,po = [4133.1,8267,12389,16440],lf.value(7800,150)


L = lf.value(0.6,0.01)
b,a = lf.MNK([1,2,3,4],duralFr)
xl = [i/100 for i in range(450)]
yl = [b.value*x+a.value for x in xl]


b.print("Коэффициент b")
a.print("Коэффициент a")
ftimesn = sum([(duralFr[i]/(i+1)) for i in range(len(duralFr))])/len(duralFr)
u = lf.value(2*L.value*b.value,2*L.value*b.value*((b.relErorr()**2+((L.relErorr())**2))**.5))
#u = lf.value(2*0.5*ftimesn,2*1*b.value*((b.relErorr()**2+((0.01/1)**2))**.5))
u.print("Скорость звука")

E = lf.value(po.value*(u.value**2),
        po.value*(u.value**2)*(((po.relErorr()**2)+4*(u.relErorr()**2))**.5))
Epr = lf.value(round(E.value/(10**7),0),round(E.error/(10**7),0))
Epr.print("тема на 10 в 7")

plt.plot(xl,yl)
plt.errorbar(x = [1,2,3,4],
            y = duralFr,
            yerr=[10,10,10,10],
            xerr = [0,0,0,0],
            fmt="_")
plt.yticks([i for i in range(0,18000,500)])
plt.xticks([0,1,2,3,4])
plt.grid()
plt.show()

