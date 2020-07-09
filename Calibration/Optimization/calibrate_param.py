"""
@author: Sadman Ahmed Shanto

pseudocode:
    inputs: sensible_magnitude_for_paramter, max_magnitude, initial_guess_for_parameter, decimal_precision
    algorithm:
        1) find magnitude for which error percentage condition is true
            -> decreasing integer power method
        2) once magnitude is found. determine largest integer for which error percentage condition still true.
            -> start with biggest int in the magnitude
            -> binary search jumping in magnitude range
        3) once largest integer is found, determine the decimal points bounded by the decimal_precision for which error percentage condition is true.
            -> treat the decimal point numbers as integers with decimal_precision range
            -> start with biggest int in the magnitude in decimal_precision range
            -> binary search jumping in magnitude range
"""

import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import highway_free_flow as hff
import time, random, csv, os, sys

#realistic sim
realistic_params = [25, 1.6] # a,b,delta
real_sim = hff.HighwayFreeFlow(realistic_params)
measured_counts = np.array(real_sim.getCountsData())
measured_velocity = np.array(real_sim.getVelocityData())


def getErrorPecentage():
    pass

def checkErrorPercentCondition():
    pass

def findMaxInt():
    pass

