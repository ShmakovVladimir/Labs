import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def countB(R:float,C:float,S:float,N:int,U:float)->float:
    return R*C*U/(S*N)
def countH(I:float,N0:float,R:float):
    return I*N0/(np.pi*2*R)
#Данные экспериментов
#Kx,Ky,Ieff,R0,2xc,2yc,2xs,2ys,N0,Ni,S,R
data = np.ndarray([[20*np.pow(10,-6),50*np.pow(10,-6),224.8*np.pow(10,-6),0.22,3.2,3.6,8.2,3.45,20,300,0.76*np.pow(10,-4),13.3*np.pow(10,-2)/(2*np.pi)]])

