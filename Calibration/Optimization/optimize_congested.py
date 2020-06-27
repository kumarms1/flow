"""
@author: Sadman Ahmed Shanto
references for realistic params and bounds: 
    https://traffic-simulation.de/info/info_IDM.html, 
    https://tigerprints.clemson.edu/cgi/viewcontent.cgi?referer=&httpsredir=1&article=2936&context=all_theses
"""
from scipy.optimize import minimize
import highway_congested as hc
import numpy as np

#realistic_params = [2.3, 2.0, 30.0, 1.0, 4.0, 2.0]
#realistic_params = [1.3, 2.0, 30.0, 1.0, 4.0, 2.0]
realistic_params = [30.0, 1.0, 2.0]

measured_counts = np.array(hc.HighwayCongested(realistic_params).getCountsData())

#objective function
def objective(params):
    simmed_counts = np.array(hc.HighwayCongested(params).getCountsData())
    print("simmed params: ", params)
    print("error: " + str(((simmed_counts - measured_counts)**2).sum()))
    return ((simmed_counts - measured_counts)**2).sum()

#bounds
a_bounds = (0.5,2)
b_bounds = (0.5,2)
v0_bounds = (0,30)
T_bounds = (1,3)
delta_bounds = (1,5)
s0_bounds = (0.1,5)
#bnds = (a_bounds, b_bounds, delta_bounds)
bnds = (a_bounds, b_bounds, v0_bounds, T_bounds, delta_bounds, s0_bounds)

#initial guess
#guess = [ 0.5, 0.5, 20, 1, 1, 0.1] #lower bounds
guess = [20, 1, 0.1]

#optimize
sol = minimize(objective, guess, method="Nelder-Mead", bounds=bnds, options={'disp':True})
print(sol)
