"""
@author: Sadman Ahmed Shanto
references for realistic params and bounds: 
    https://traffic-simulation.de/info/info_IDM.html, 
    https://tigerprints.clemson.edu/cgi/viewcontent.cgi?referer=&httpsredir=1&article=2936&context=all_theses

trial one: optimized_params = [0.48958386, 0.5083347, 20.33326312, 0.98749962,  1.01666653,  0.10166662]
trial two: optimized_params = 
"""
from scipy.optimize import minimize
import highway_free_flow as hff
import numpy as np

#realistic_params = [0.73, 1.67, 25, 1.6, 4, 2] # a,b,v0,T,delta, s0
realistic_params = [25, 1.6, 2] # a,b,v0,T,delta, s0
#
measured_counts = np.array(hff.HighwayFreeFlow(realistic_params).getCountsData())

#objective function
def objective(params):
    simmed_counts = np.array(hff.HighwayFreeFlow(params).getCountsData())
    print("simmed params: ", params)
    print("error: " + str(((simmed_counts - measured_counts)**2).sum()))
    return ((simmed_counts - measured_counts)**2).sum()

#constraints?

#bounds
#a_bounds = (0.5,2)
#b_bounds = (0.5,2)
v0_bounds = (20,30)
T_bounds = (1,3)
#delta_bounds = (1,5)
s0_bounds = (0.1,5)
bnds = (v0_bounds, T_bounds, s0_bounds)
#bnds = (a_bounds, b_bounds, v0_bounds, T_bounds, delta_bounds, s0_bounds)

#initial guess
#guess = [ 0.5, 0.5, 20, 1, 1, 0.1] #lower bounds
guess = [20,1,0.1]

#optimize
sol = minimize(objective, guess, method="Nelder-Mead", bounds=bnds, options={'disp':True})

print(sol)
