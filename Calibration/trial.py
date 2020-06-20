import numpy as np
import random

data = ["a","b","noise","T","v0","delta","s0"]

def createIDM(index, num, defaulData):
    IDMParamSet = defaulData[:]
    if index == 0: #a
        options = list(np.linspace(1,5,num))
        while len(options)!=0:
            IDMParamSet[index] = options.pop(0)
            print(IDMParamSet)
    elif index == 1: #b
        options = list(np.linspace(1,5,num))
        while len(options)!=0:
            IDMParamSet[index] = options.pop(0)
            print(IDMParamSet)
    elif index == 2:  #noise
        options = list(np.linspace(0,2,num))
        while len(options)!=0:
            IDMParamSet[index] = options.pop(0)
            print(IDMParamSet)
    elif index == 3:  #v0
        options = list(np.linspace(15,30,num))
        while len(options)!=0:
            IDMParamSet[index] = options.pop(0)
            print(IDMParamSet)
    elif index == 4:  #T
        options = list(np.linspace(1,4,num))
        while len(options)!=0:
            IDMParamSet[index] = options.pop(0)
            print(IDMParamSet)
    elif index == 5:  #delta
        options = list(np.linspace(2,6,num))
        while len(options)!=0:
            IDMParamSet[index] = options.pop(0)
            print(IDMParamSet)
    elif index == 6:  #s0
        options = list(np.linspace(1,5,num))
        while len(options)!=0:
            IDMParamSet[index] = options.pop(0)
            print(IDMParamSet)
    return IDMParamSet

"""
index = determine which parameter to change
num = 1) how many sets of that one change that needs to create
      2) how a certain range is broken up
algo:
    save defaulData as a local var
    create an array of size num using linspace for given index
    for i in range(num):
        lvar[index] = givar.pop()
        print(lvar)
"""

num = 2

for i in range(len(data)):
    createIDM(i,num,data)

