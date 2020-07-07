import numpy as np
import random

x = np.array([1,2,3,4,53,21])

def eror(vals, isCounts, stdv):
    if isCounts:
        y = np.round(np.random.normal(vals,stdv))
        return np.where(y<0, 0, y) 
    else:
        y = np.random.normal(vals,stdv)
        return np.where(y<0, 0, y) 

print(eror(x, True, 3))
print(eror(x, False, 4))
