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
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_15/a_params.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_30/a_params.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_60/a_params.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_15/b_params.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_30/b_params.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_60/b_params.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_15/v0_params.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_30/v0_params.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_60/v0_params.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_15/T_params.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_30/T_params.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_60/T_params.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_15/delta_params.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_30/delta_params.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_60/delta_params.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_15/s0_params.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_30/s0_params.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_60/s0_params.png" width=400 height=320></td>
  </tr>
 </table>

## Insights
The geometry of the counts data with the fidelity of data taking is noteworthy. a and b paramaters for the most part don't show any effect on the counts data, delta shows very slight change, so does s0. Interestingly, at longer data taking times, the distinction in v0 values become more apparant and that between s0 diminishes.

T seems to be the only paramater that causes significant changes to the macroscopic perceieved data.

## Average Speed Data:

<table>
  <tr>
    <td>Average Speed data: 15 seconds fidelity</td>
    <td>Average Speed data: 30 seconds fidelity</td>
    <td>Average Speed data: 60 seconds fidelity</td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_15/a_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_30/a_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_60/a_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_15/b_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_30/b_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_60/b_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_15/v0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_30/v0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_60/v0_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_15/T_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_30/T_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_60/T_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_15/delta_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_30/delta_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_60/delta_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_15/s0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_30/s0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_60/s0_params_velocity.png" width=400 height=320></td>
  </tr>
 </table>

## Insights
a and b parameters don't seem to affect the average velocity significantly. v0 shows that longer data taking periods,the values converge based on some discrete model, T is still the most sensitive paramter even for average velocity. The distinction between the delta and s0 parameters and the average velocity becomes more prominent at longer data taking periods.

## Overall Observations
a and b have very minute effect on macro quantities. T seems to play a consequential role in determining macro quantities. Certain parameters cannot be discerned at higher fidelites but at longer data taking period becomes distinct (v0, s0 and delta for average velocity) (v0 and delta for counts). s0 behaves interestingly in the sense that at lower fidelites it becomes indifferent wrt the count data but more distinct wrt to average velocity data. This feature may be beneficial when it comes to optimization routines.

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
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_15/a_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_30/a_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_60/a_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_15/b_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_30/b_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_60/b_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_15/v0_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_30/v0_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_60/v0_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_15/T_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_30/T_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_60/T_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_15/delta_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_30/delta_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_60/delta_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_15/s0_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_30/s0_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_60/s0_params_counts.png" width=400 height=320></td>
  </tr>
 </table>

## Insights

## Average Speed Data:

<table>
  <tr>
    <td>Average Speed data: 15 seconds fidelity</td>
    <td>Average Speed data: 30 seconds fidelity</td>
    <td>Average Speed data: 60 seconds fidelity</td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_15/a_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_30/a_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_60/a_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_15/b_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_30/b_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_60/b_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_15/v0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_30/v0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_60/v0_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_15/T_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_30/T_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_60/T_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_15/delta_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_30/delta_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_60/delta_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_15/s0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_30/s0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp5/fidelity_60/s0_params_velocity.png" width=400 height=320></td>
  </tr>
 </table>

## Insights

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
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_15/a_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_30/a_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_60/a_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_15/b_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_30/b_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_60/b_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_15/v0_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_30/v0_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_60/v0_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_15/T_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_30/T_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_60/T_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_15/delta_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_30/delta_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_60/delta_params_counts.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_15/s0_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_30/s0_params_counts.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_60/s0_params_counts.png" width=400 height=320></td>
  </tr>
 </table>

## Insights

## Average Speed Data:

<table>
  <tr>
    <td>Average Speed data: 15 seconds fidelity</td>
    <td>Average Speed data: 30 seconds fidelity</td>
    <td>Average Speed data: 60 seconds fidelity</td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_15/a_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_30/a_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_60/a_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_15/b_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_30/b_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_60/b_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_15/v0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_30/v0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_60/v0_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_15/T_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_30/T_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_60/T_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_15/delta_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_30/delta_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_60/delta_params_velocity.png" width=400 height=320></td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_15/s0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_30/s0_params_velocity.png" width=400 height=320></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp6/fidelity_60/s0_params_velocity.png" width=400 height=320></td>
  </tr>
 </table>

## Insights

## Overall Observations

## TO DO
- [x] create reference data file from default paramter set
- [x] generate 7 sim data files for analysis
- [x] write script to plot generate macroscopic information from the data and plots necessary graphs
- [x] analyze data for different data taking time intervals
- [x] analyze data after trimming first 60 seconds and last 30 seconds
- [x] make the plotting and data analysis code more user friendly/general use
- [x] simulate cases with same IDM paramaters but different speed and inflow parameters
- [x] simulate the congested regime with both waves and no waves
- [ ] look at data at 90 seconds range and affect on delta and s0 and macro parameters
- [ ] incorporate the error metrics
- [ ] update README.md and documentation
