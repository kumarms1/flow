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
. automate.sh num_of_sims csvFileName.csv dataDirectory macroDataDirectory
```
The above command will generate the IDM parameter data, run the corresponding simulation for that data set and create the microsimulation csv files in the data/dataDirectory directory and the resultant macroscopic data in the data/macroData directory. 

## Preliminary Results

The simulation was conducted on a one lane road of length 1600 meters for 300 seconds with vehicles with inflow speed 26.8 and flow 2006.

### Results when looking at data every 15 seconds
![a](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_15/a_params.png)
![b](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_15/b_params.png)
![n](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_15/noise_params.png)
![v](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_15/v0_params.png)
![t](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_15/T_params.png)
![d](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_15/delta_params.png)
![s](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_15/s0_params.png)


### Results when looking at data every 30 seconds
![a](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/a_params.png)
![b](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/b_params.png)
![n](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/noise_params.png)
![v](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/v0_params.png)
![t](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/T_params.png)
![d](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/delta_params.png)
![s](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/s0_params.png)

#### Results looking at data trimming first 60 seconds and last 30 seconds (data taken every 30 seconds)
![a](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_trimmed_30/a_params.png)
![b](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_trimmed_30/b_params.png)
![n](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_trimmed_30/noise_params.png)
![v](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_trimmed_30/v0_params.png)
![t](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_trimmed_30/T_params.png)
![d](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_trimmed_30/delta_params.png)
![s](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_trimmed_30/s0_params.png)


### Results when looking at data every 60 seconds
![a](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_60/a_params.png)
![b](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_60/b_params.png)
![n](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_60/noise_params.png)
![v](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_60/v0_params.png)
![t](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_60/T_params.png)
![d](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_60/delta_params.png)
![s](https://github.com/shanto268/comprehensive_simulation_traffic_analysis_software/blob/master/exp2_60/s0_params.png)

## TO DO
- [x] create reference data file from default paramter set
- [x] generate 7 sim data files for analysis
- [x] write script to plot generate macroscopic information from the data and plots necessary graphs
- [ ] incorporate the error metrics
- [x] analyze data for different data taking time intervals
- [x] analyze data after trimming first 60 seconds and last 30 seconds
- [ ] simulate cases with same IDM paramaters but different speed and inflow parameters
- [ ] make the plotting and data analysis code more user friendly/general use
- [ ] update README.md and documentation
