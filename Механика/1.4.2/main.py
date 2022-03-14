import matplotlib.pyplot as plt
import math
from enum import Enum



class value:
    def __init__(self,value,error) -> None:
        self.value, self.error = value,error
    def print(self,name: str):
        print(name+': '+str(self.value)+' +/- '+str(self.error))
    def relErorr(self):
        return self.error/self.value