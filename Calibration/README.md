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
"v0":
"T":
"delta":
"s0":

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
"a":
"b":
"v0":
"T":
"delta":
"s0":

## Overall Observations

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
"a": at lower fidelities the macroscopic behavior converges
"b": some convergence at lower fidelities. Interesting behavior at 1.3 and 1.38 values. Noise may be responsible for differences.
"v0": positive distinct relationship, gets better at lower fidelities.
"T": at higher fidelities small differences in values are observable (2.63 and 2.89). This trend holds overall.
"delta":positive distinct relationship.
"s0": lower fidelity subtle differences observable.

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
"a": distinct spread as compared to free flow.
"b": distinct spread as compared to free flow. the value 2 seems to be a local minima as values on both ends result in lower average velocities.
"v0": distinct values as compared to free flow regime where it seemed to be discrete bands. overall positive relationship
"T": not as strong distinctions
"delta": strong positive distinction
"s0": 2 seems to be a local minima. not as strong distinctions.

## Overall Observations

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
"T": parameter defining behavior
"delta": quantum model like parameterization
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
"b": 2 no longer a minima. indistinguishable spread.
"v0": similar to congested waves.
"T": good distinction values inverse trend
"delta": strong distinction values postive trend
"s0": 2 is not a local minima like the congested wave regime. not as strong distinctions.

## Overall Observations

# Observations

## TO DO
- [x] create reference data file from default paramter set
- [x] generate 7 sim data files for analysis
- [x] write script to plot generate macroscopic information from the data and plots necessary graphs
- [x] analyze data for different data taking time intervals
- [x] analyze data after trimming first 60 seconds and last 30 seconds
- [x] make the plotting and data analysis code more user friendly/general use
- [x] simulate cases with same IDM paramaters but different speed and inflow parameters
- [x] simulate the congested regime with both waves and no waves
- [ ] reanalyze the results, fix the plot scales, and think of better representation/metrics for analysis 
- [ ] incorporate the error metrics
- [ ] t delta swap fix exp4
- [ ] update README.md and documentation
