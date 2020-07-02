"""
@author: Sadman Ahmed Shanto
Plan:
    simulation should be a class with IDM paramaters as init values, data file name as a instance variable. Needs functions that processes macro data, needs function that deletes the resultant data file.
"""

from flow.controllers import IDMController,OV_FTL_Controller,LinearOVM,BandoFTL_Controller
from flow.core.params import SumoParams, EnvParams, NetParams, InitialConfig, SumoLaneChangeParams
from flow.core.params import VehicleParams, InFlows
from flow.envs.ring.lane_change_accel import ADDITIONAL_ENV_PARAMS
from flow.networks.highway import HighwayNetwork, ADDITIONAL_NET_PARAMS
from flow.envs import LaneChangeAccelEnv
from flow.core.experiment import Experiment
import numpy as np
import pandas as pd
import os, sys, csv
import Process_Flow_Outputs as PFO
#import matplotlib.pyplot as pt

class HighwayFreeFlow:

    def __init__(self,params,fidelity=30):
        self.a = 0.73
        self.b = 1.67
        self.v0 = params[0] 
        self.T = params[1]
        self.delta = 4
        self.s0 = 2
        self.noise = 0 #no noise
        self.fidelity = fidelity
        self.traffic_speed = 25.8
        self.traffic_flow = 2006
        self.accel_data = (IDMController, {'a':self.a,'b':self.b,'noise':self.noise, 'v0':self.v0, 'T':self.T, 'delta':self.delta, 's0':self.s0})
        self.env_params = EnvParams(additional_params=ADDITIONAL_ENV_PARAMS)
        self.additional_net_params = ADDITIONAL_NET_PARAMS.copy()
        self.additional_net_params['lanes'] =1
        self.additional_net_params['length'] = 1600
        self.csvFileName = ""
        self.runSim()

    def addVehicles(self):
        vehicles = VehicleParams()
        vehicles.add(
            veh_id="human",
            acceleration_controller=self.accel_data,
            lane_change_params=SumoLaneChangeParams(
                model="SL2015",
                lc_sublane=2.0,
            ),
        )
        return vehicles

    def addInflows(self):
        inflow = InFlows()
        inflow.add(
            veh_type="human",
            edge="highway_0",
            vehs_per_hour=self.traffic_flow,
            departLane="free",
            departSpeed=self.traffic_speed)
        return inflow

    def setFlowParams(self, inflow,  vehicles): 
        flow_params = dict(
            # name of the experiment
            exp_tag='highway',
            # name of the flow environment the experiment is running on
            env_name=LaneChangeAccelEnv,
            # name of the network class the experiment is running on
            network=HighwayNetwork,
            # simulator that is used by the experiment
            simulator='traci',
            # sumo-related parameters (see flow.core.params.SumoParams)
            sim=SumoParams(
                sim_step=0.4,
                render=False,
                lateral_resolution=0.1,
                emission_path='data/',
                restart_instance=True,
            ),
            # environment related parameters (see flow.core.params.EnvParams)
            env=EnvParams(
                horizon=1000,
                additional_params=ADDITIONAL_ENV_PARAMS.copy(),
            ),
            # network-related parameters (see flow.core.params.NetParams and the
            # network's documentation or ADDITIONAL_NET_PARAMS component)
            net=NetParams(
                inflows=inflow,
                additional_params= self.additional_net_params,
            ),
            # vehicles to be placed in the network at the start of a rollout (see
            # flow.core.params.VehicleParams)
            veh=vehicles,
            # parameters specifying the positioning of vehicles upon initialization/
            # reset (see flow.core.params.InitialConfig)
            initial=InitialConfig(
                spacing="uniform",
                shuffle=True,
            ),
        )
        return flow_params

    def runSim(self):
        vehicles = self.addVehicles()
        inflow = self.addInflows()
        flow_params = self.setFlowParams(inflow,vehicles)
        exp = Experiment(flow_params)
        _ = exp.run(1, convert_to_csv=True)
        emission_location = os.path.join(exp.env.sim_params.emission_path, exp.env.network.name)
        pd.read_csv(emission_location + '-emission.csv')
        self.csvFileName = emission_location+"-emission.csv"

    def getCountsData(self):
        countsData, speedData = self.processMacroData(self.csvFileName)
      #  print("The counts are: ", countsData)
     #   self.deleteDataFile(self.csvFileName)
        return countsData

    def getVelocityData(self):
        countsData, speedData = self.processMacroData(self.csvFileName)
      #  print("The speeds are: ", speedData)
        self.deleteDataFile(self.csvFileName)
        return speedData

    def processMacroData(self,csvFile):
        highway_data = PFO.SimulationData(csv_path = csvFile)
        pos_dict = highway_data.get_Timeseries_Dict(data_id='TOTAL_POSITION',want_Numpy=True)
        vel_dict =highway_data.get_Timeseries_Dict(data_id='SPEED',want_Numpy=True)
        position_for_count = 800 #radar reading position
        time_count_data = []  #array to store results
        vTime_array = [] # array to store (time, velocity) results
        for veh_id in highway_data.veh_ids:  #looping through all cars
          pos_data = pos_dict[veh_id] #store position information for each car
          end_pos = pos_data[1,-1]
          veh_data = vel_dict[veh_id]
          if(end_pos > position_for_count): #if car crossed the radar line point
              t=0
              p = pos_data[1,t] #position at which car was spawned
              while(p < position_for_count):
                  t += 1
                  p = pos_data[1,t]
              vTime_array.append((pos_data[0,t],veh_data[1,t])) #(time stamp, velocity a  t time stamp) at which   car passes the radar point
        vTime_array.sort(key=lambda x: x[0])
        count_num, average_speed = self.countsEveryXSeconds(self.fidelity, vTime_array)
        return count_num, average_speed

    def countsEveryXSeconds(self, x, sorted_counts, trim=False):
        i = 0
        m = 0
        j = 1
        comp = x
        c = []
        mc = []
        meanSpeed = []
        while (i < len(sorted_counts)):
            while( (m!=len(sorted_counts)) and ((j-1)*comp <= sorted_counts[m][0] <=   j*comp) ) :
                c.append(sorted_counts[m])
                m+=1
            i = m
            j+=1
            d = c.copy()
            mc.append(d)
            #print(d)
            if (len(d) == 0):
                meanSpeed.append(0)
            else:
                meanSpeed.append(round(sum(i for _, i in d)/len(d),3))
            c.clear()
        mcc = []
        for k in mc:
            mcc.append(len(k))
        if (trim==True):
            mcc.pop()
            mcc.pop(0)
            mcc.pop(0)
        return mcc, meanSpeed

    def deleteDataFile(self,csvFile):
        os.remove(csvFile)
