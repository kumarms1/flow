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

```
Some Naming Conventions:
Make sure the name of the csvName is in the format IDMParams_exp(some number).csv 
Make sure the name of the dataDirectory is in the format exp(some number)_data 

```

<table>
  <tr>
    <td>Counts data: 15 seconds fidelity</td>
    <td>Counts data: 30 seconds fidelity</td>
    <td>Counts data: 60 seconds fidelity</td>
  </tr>
  <tr>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_15/a_params.png" width=270 height=480></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_30/a_params.png" width=270 height=480></td>
    <td><img src="https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_60/a_params.png" width=270 height=480></td>
  </tr>
 </table>


# Preliminary Results

The simulation was conducted on a one lane road of length 1600 meters for 300 seconds with vehicles with inflow speed 26.8 and flow 2006.

## Counts Data:

### Results when looking at data every 15 seconds
![a](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_15/a_params.png)
![b](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_15/b_params.png)
![v](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_15/v0_params.png)
![t](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_15/T_params.png)
![d](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_15/delta_params.png)
![s](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_15/s0_params.png)


### Results when looking at data every 30 seconds
![a](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_30/a_params.png)
![b](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_30/b_params.png)
![v](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_30/v0_params.png)
![t](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_30/T_params.png)
![d](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_30/delta_params.png)
![s](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_30/s0_params.png)


### Results when looking at data every 60 seconds
![a](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_60/a_params.png)
![b](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_60/b_params.png)
![v](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_60/v0_params.png)
![t](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_60/T_params.png)
![d](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_60/delta_params.png)
![s](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp4_res_60/s0_params.png)


## Insights
The geometry of the counts data with the fidelity of data taking is noteworthy. a and b paramaters for the most part don't show any effect on the counts data, delta shows very slight change, so does s0. Interestingly, at longer data taking times, the distinction in v0 values become more apparant and that between s0 diminishes.

T seems to be the only paramater that causes significant changes to the macroscopic perceieved data.

## Average Speed Data:

### Results when looking at data every 15 seconds
![a](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_15/a_params_velocity.png)
![b](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_15/b_params_velocity.png)
![v](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_15/v0_params_velocity.png)
![t](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_15/T_params_velocity.png)
![d](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_15/delta_params_velocity.png)
![s](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_15/s0_params_velocity.png)

### Results when looking at data every 30 seconds
![a](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_30/a_params_velocity.png)
![b](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_30/b_params_velocity.png)
![v](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_30/v0_params_velocity.png)
![t](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_30/T_params_velocity.png)
![d](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_30/delta_params_velocity.png)
![s](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_30/s0_params_velocity.png)

### Results when looking at data every 60 seconds
![a](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_60/a_params_velocity.png)
![b](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_60/b_params_velocity.png)
![v](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_60/v0_params_velocity.png)
![t](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_60/T_params_velocity.png)
![d](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_60/delta_params_velocity.png)
![s](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/figs/exp4/fidelity_60/s0_params_velocity.png)

## Insights

## TO DO
- [x] create reference data file from default paramter set
- [x] generate 7 sim data files for analysis
- [x] write script to plot generate macroscopic information from the data and plots necessary graphs
- [x] analyze data for different data taking time intervals
- [x] analyze data after trimming first 60 seconds and last 30 seconds
- [x] make the plotting and data analysis code more user friendly/general use
- [x] simulate cases with same IDM paramaters but different speed and inflow parameters
- [ ] incorporate the error metrics
- [ ] update README.md and documentation
- [ ] simulate the congested regime with both waves and no waves
- [ ] conduct data analysis for that regime
