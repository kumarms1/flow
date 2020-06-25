# Optimization Routine

### High Level Algorithm
```
define realistic IDM params #IDM params have the form [a,b,v0,T,delta,s0]
get counts data using the realistic IDM params and store as an array (measured_counts)
define an initial guess for the IDM params
define the upper and lower bounds for each IDM param
define the objective function as follows:
      #since the counts data are an array of form [count1, count2, ... ]
      error = ((simmed_counts - measured_counts)**2).sum()
start the optimization routine using the Nelder-Mead solver to minimize the objective function.
```

### Choice of Solver

I ran a toy simulation to test out which solver was the most efficient and accurate solver out of all the solvers that don't require a Jacobian.


# Results and Interpretation:

## For initial guess of [ 0.5, 0.5, 20, 1, 1, 0.1] % a,b,v0,T,delta, s0

The optimization terminated successfully with the following output:

```bash
Current function value: 1.000000
         Iterations: 32
         Function evaluations: 129
 final_simplex: (array([[ 0.49537037,  0.50752315, 20.2037037 ,  0.97777778,  1.01666667,
         0.10037037],
       [ 0.49537135,  0.50752917, 20.20367335,  0.97778033,  1.01666452,
         0.10037028],
       [ 0.49537178,  0.50752219, 20.20371275,  0.97778456,  1.01666701,
         0.10037073],
       [ 0.49537146,  0.50752468, 20.2036393 ,  0.97777676,  1.01666675,
         0.10037109],
       [ 0.49537351,  0.5075245 , 20.20372156,  0.9777715 ,  1.01666681,
         0.1003708 ],
       [ 0.49537027,  0.50752537, 20.20369171,  0.97777785,  1.01666707,
         0.10037064],
       [ 0.49537208,  0.50752337, 20.20374954,  0.97777986,  1.01666533,
         0.10037079]]), array([1., 1., 1., 1., 1., 1., 1.]))
           fun: 1.0
       message: 'Optimization terminated successfully.'
          nfev: 129
           nit: 32
        status: 0
       success: True
             x: array([ 0.49537037,  0.50752315, 20.2037037 ,  0.97777778,  1.01666667,
        0.10037037])
```

### Expected Parameters
```python
realistic_params = [0.73, 1.67, 25, 1.6, 4, 2] # a,b,v0,T,delta, s0
```
While, the optimization did find solution it is most certainly a local one, since the optimized parameter set of  [0.49537037,  0.50752315, 20.2037037 ,  0.97777778,  1.01666667, 0.10037037] is far from that of the expected set.

This suggests that the search space is bumpy with multiple minimas.

## For initial guess of [ 1,1.5,30,1,4,2] (i.e. the default Flow IDM parameters)

The optimization routine went on for 2 hours before I force quit it, the log output showed that it was stuck at the same set of values for a long period of time.

## Optimizing only T and v0 parameters

The optimization terminated successfully with the following output:

```bash
Optimization terminated successfully.
         Current function value: 1.000000
         Iterations: 22
         Function evaluations: 74
 final_simplex: (array([[20.06770833,  0.99053819,  0.10315104],
       [20.06772868,  0.99053786,  0.10314911],
       [20.06771596,  0.99052993,  0.10315052],
       [20.06765705,  0.99052955,  0.10315066]]), array([1., 1., 1., 1.]))
           fun: 1.0
       message: 'Optimization terminated successfully.'
          nfev: 74
           nit: 22
        status: 0
       success: True
             x: array([20.06770833,  0.99053819,  0.10315104])
```

While, the optimization did find solution it is most certainly a local one, since the parameters don't match the expected parameter set. The simulation however ran a lot faster. This result confirms the initial hypothesis of the search space being very bumpy.
