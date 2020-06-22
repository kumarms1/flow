# Idea

For a fixed set of parameters (road length, simulation time, inflow rate and inflow speed), we generate microsimulation data for a given set of IDM parameters (a,b,T,s0,v0,noise,delta) and use this data to calculate a macroscopic quantity (counts/density/flow) and then use the sets of macroscopic data and one given batch of IDM paramters to predict the other sets of IDM paramters and calculate the error/accuracy statistics for any given calibration models.

# Methodology
Simulate a scenario for a given default set of IDM parameters
Simulate the same scenario varying one paramater from the default set -> 5 times
Analyze how the macroscopic quantity varies with each paramater set
Establish a relationship (if any exists)
Use this relationship to predict a random set of IDM paramters

# Usage

## To generate random IDM paramters
```bash
python generate_data.py num_of_simulations csvName.csv
```
The generate_data.py script allows the random generation of IDM paramters within certain bounds, it also allows more controlled fine tuning of which parameter needs to be changed and which needs to be kept constant. The command shown creates a data file - csvName.csv - which has num_of_simulations variations of a single parameter for each parameter in the IDM.


## To run multiple sims
```bash
. automate.sh num_of_sims csvFileName.csv dataDirectory
```
The above command will generate the IDM parameter data, run the corresponding simulation for that data set and create the microsimulation csv files in the data/dataDirectory directory and the resultant macroscopic data in the data/macroData directory. 

## To retrieve macroscopic data
```bash
python3 getMacroData.py name_of_data_dir csvFileName fidelity params_file.csv
```

## To create analysis plots
```bash
python3 graph.py dataFile fidelity numSimsPerPar
```

```
Some Naming Conventions:
Make sure the name of the csvName is in the format IDMParams_exp(some number).csv 
Make sure the name of the dataDirectory is in the format exp(some number)_data 

```

# Preliminary Results for Free Flow Regime

The simulation was conducted on a one lane road of length 1600 meters for 300 seconds with vehicles with inflow speed 26.8 and flow 2006. The default IDM parmaters were [a,b,v0,noise,v0,T,delta,s0] = [1.0, 1.5, 0, 30.0, 4.0, 1.0, 2.0].
## Counts Data:

<table>
  <tr>
    <td>Counts data: 15 seconds fidelity</td>
    <td>Counts data: 30 seconds fidelity</td>
    <td>Counts data: 60 seconds fidelity</td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_15/a_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_30/a_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_60/a_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_15/b_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_30/b_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_60/b_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_15/v0_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_30/v0_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_60/v0_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_15/T_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_30/T_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_60/T_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_15/delta_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_30/delta_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_60/delta_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_15/s0_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_30/s0_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_60/s0_params_counts.png" width=400 height=320></td>
  </tr>
 </table>

## Insights
"a": doesn't affect macro data

"b": doesn't affect macro data

"v0": shows positive relationship with macro data (max value)

"T": shows inverse relationship with macro data (max value and gradient)

"delta": paramaters affect on macro data is a function of the fidelity. Certain threshold over which all values converge.

"s0": quantum phenomenon. There are certain values that lead to disparate effects on macro data.

## Average Speed Data:

<table>
  <tr>
    <td>Average Speed data: 15 seconds fidelity</td>
    <td>Average Speed data: 30 seconds fidelity</td>
    <td>Average Speed data: 60 seconds fidelity</td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_15/a_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_30/a_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_60/a_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_15/b_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_30/b_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_60/b_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_15/v0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_30/v0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_60/v0_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_15/T_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_30/T_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_60/T_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_15/delta_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_30/delta_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_60/delta_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_15/s0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_30/s0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp7freeFlow/fidelity_60/s0_params_velocity.png" width=400 height=320></td>
  </tr>
 </table>

## Insights
"a": good close fit. Spread only observable at lower fidelity (longer data taking time)

"b": good close fit. Spread only observable at lower fidelity (longer data taking time)

"v0": distinct effect on macro data

"T": certain optimal value observed at T=1 and incremental increases tend towards some fixed macro data point. Sensitive around the optimal value or lower value

"delta": similar behavior trend as T, incremental increases in delta tend towards some fixed macro data point. Sensitive around the lower values

"s0": incremental increases in s0 lead to larger decreases in macro data

## Overall Observations
"a" and "b" do not contribute to any macro data. v0 helps identify both macro data from the param set, T is good for counts data and not so much for speed, delta shows different behavior for counts at different fidelities and is not helpful to distinguish paramater values from; for speed data, delta is somewhat distinguishable at lower values but converges at higher param values, s0 looks different at different fidelities for counts data and shows some evidence for different macro results past a threshold param value.  

# Preliminary Results for Congested (with Waves) Regime

The simulation was conducted on a one lane road of length 1600 meters for 500 seconds with vehicles with inflow speed 24.1, flow 2215, congestion speed 10 and boundary cell lenght 100 m. The default IDM parmaters were [a,b,v0,noise,v0,T,delta,s0] = [2.3,2.0,0.1,30.0,4.0,1.0,2.0]

## Counts Data:

<table>
  <tr>
    <td>Counts data: 15 seconds fidelity</td>
    <td>Counts data: 30 seconds fidelity</td>
    <td>Counts data: 60 seconds fidelity</td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_15/a_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_30/a_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_60/a_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_15/b_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_30/b_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_60/b_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_15/v0_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_30/v0_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_60/v0_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_15/T_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_30/T_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_60/T_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_15/delta_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_30/delta_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_60/delta_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_15/s0_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_30/s0_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_60/s0_params_counts.png" width=400 height=320></td>
  </tr>
 </table>

## Insights
"a": no effect. same as free flow.

"b": no effect. same as free flow.

"v0": similar behavior to free flow.

"T": similar behavior to free flow.

"delta": similar behavior to free flow.

"s0": all params lead to similar macro data results, unlike free flow there is no distinct behavior at s0 = 5



## Average Speed Data:

<table>
  <tr>
    <td>Average Speed data: 15 seconds fidelity</td>
    <td>Average Speed data: 30 seconds fidelity</td>
    <td>Average Speed data: 60 seconds fidelity</td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_15/a_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_30/a_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_60/a_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_15/b_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_30/b_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_60/b_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_15/v0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_30/v0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_60/v0_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_15/T_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_30/T_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_60/T_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_15/delta_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_30/delta_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_60/delta_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_15/s0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_30/s0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp8congestedWaves/fidelity_60/s0_params_velocity.png" width=400 height=320></td>
  </tr>
 </table>

## Insights
"a": similar to free flow with a little more spread at lower fidelities. 

"b": similar to free flow with a little more spread at lower fidelities. 

"v0": similar to free flow 

"T": similar to free flow at higher fidelities, at lower fidelities greater scatter of initial macro points wrt to T params compared to free flow. 

"delta": similar to free flow 

"s0": closer scatter compared to free flow

## Overall Observations
Most parameters don't help in identifying the regime, the only observable difference was the distict behavior for macro data at s0 = 5 in the two regime and the greater initial scatter of velocity fot T params in congested with waves regime compared to free flow.


# Preliminary Results for Congested (no Waves) Regime

The simulation was conducted on a one lane road of length 1600 meters for 500 seconds with vehicles with inflow speed 24.1, flow 2215, congestion speed 10 and boundary cell lenght 100 m. The default IDM parmaters were [a,b,v0,noise,v0,T,delta,s0] =  [2.3,2.0,0.1,30.0,4.0,1.0,2.0]

## Counts Data:

<table>
  <tr>
    <td>Counts data: 15 seconds fidelity</td>
    <td>Counts data: 30 seconds fidelity</td>
    <td>Counts data: 60 seconds fidelity</td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_15/a_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_30/a_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_60/a_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_15/b_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_30/b_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_60/b_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_15/v0_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_30/v0_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_60/v0_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_15/T_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_30/T_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_60/T_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_15/delta_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_30/delta_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_60/delta_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_15/s0_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_30/s0_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_60/s0_params_counts.png" width=400 height=320></td>
  </tr>
 </table>

## Insights
"a": almost same overall trends as congested waves regime

"b": almost same overall trends as congested waves regime

"v0": almost same overall trends as congested waves regime

"T":  almost same overall trends as congested waves regime

"delta": almost same overall trends as congested waves regime

"s0": similar to congested waves regime

## Average Speed Data:

<table>
  <tr>
    <td>Average Speed data: 15 seconds fidelity</td>
    <td>Average Speed data: 30 seconds fidelity</td>
    <td>Average Speed data: 60 seconds fidelity</td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_15/a_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_30/a_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_60/a_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_15/b_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_30/b_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_60/b_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_15/v0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_30/v0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_60/v0_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_15/T_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_30/T_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_60/T_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_15/delta_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_30/delta_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_60/delta_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_15/s0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_30/s0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp9congestedNoWaves/fidelity_60/s0_params_velocity.png" width=400 height=320></td>
  </tr>
 </table>

## Insights
"a": similar to congested waves

"b": similar to congested waves. 

"v0": similar to congested waves.

"T": similar to congested waves.

"delta": not as similar to congested waves regime, delta paramaters not as sensentive at lower values. 

"s0": similar to congested waves.

## Overall Observations
Counts data cannot be used to differentiate between congested with and without waves regime. The only difference was the higher sensentivity of velocity to delta values in the waves regime.

# Conclusions
###For counts macro data:
v0 and T are paramaters of interest. a and b do not affect results.

###For velocity macro data:
v0 and T are paramaters of interest. a and b do not affect results.

###For free flow and congested regimes:

Most parameters don't help in identifying the regime, the only observable difference was the distict behavior for macro data at s0 = 5 in the two regime and the greater initial scatter of velocity fot T params in congested with waves regime compared to free flow. There are, however, differences in absolute numbers of values but that may be attributed to the netwrok paramters: inflow rate and inflow speed.

###For waves and no waves regime:
Counts data cannot be used to differentiate between congested with and without waves regime. The only difference was the higher sensentivity of velocity to delta values in the waves regime.

## TO DO
- [x] create reference data file from default paramter set
- [x] generate 7 sim data files for analysis
- [x] write script to plot generate macroscopic information from the data and plots necessary graphs
- [x] analyze data for different data taking time intervals
- [x] analyze data after trimming first 60 seconds and last 30 seconds
- [x] make the plotting and data analysis code more user friendly/general use
- [x] simulate cases with same IDM paramaters but different speed and inflow parameters
- [x] simulate the congested regime with both waves and no waves
- [ ] statistical metrics and analysis incorporation
- [ ] implement calibration models using sim data
- [ ] incorporate the error metrics
- [ ] update README.md and documentation
