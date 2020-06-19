"""
@author: Sadman Ahmed Shanto
purpose: congested regime test
usage: python3 Highway_Downstream_Congestion.py a b noise v0 T delta s0 dataDirectoryName
"""

from flow.controllers import IDMController,LinearOVM,BandoFTL_Controller
from flow.core.params import SumoParams, EnvParams, NetParams, InitialConfig, SumoLaneChangeParams
from flow.core.params import VehicleParams, InFlows
from flow.envs.ring.lane_change_accel import ADDITIONAL_ENV_PARAMS
from flow.networks.highway import HighwayNetwork, ADDITIONAL_NET_PARAMS
from flow.networks.SpeedChange import HighwayNetwork_Modified, ADDITIONAL_NET_PARAMS 
from flow.envs import LaneChangeAccelEnv
from flow.core.experiment import Experiment
import numpy as np
import pandas as pd
import os, sys

# accel_data = (BandoFTL_Controller,{'alpha':.5,'beta':20.0,'h_st':12.0,'h_go':50.0,'v_max':30.0,'noise':0.0})
# traffic_speed = 28.6
# traffic_flow = 2172

#read data
a = round(float(sys.argv[1]),2)
b = round(float(sys.argv[2]),2)
noise =round(float(sys.argv[3]),2)
v0 = round(float(sys.argv[4]),3)
T = round(float(sys.argv[5]),2)
delta = round(float(sys.argv[6]),2)
s0 = round(float(sys.argv[7]),2)

accel_data = (IDMController, {'a':a,'b':b,'noise':noise, 'v0':v0, 'T':T, 'delta':delta, 's0':s0})
traffic_speed = 24.1
traffic_flow = 2215

#default waves congested
#% of the form: params = [a,b,V0,delta,T,s0]
#params = [1.3, 2.0, 30.0, 4.0, 1.0, 2.0];

#default no congested
#% of the form: params = [a,b,V0,delta,T,s0]
#params = [2.3, 2.0, 30.0, 4.0, 1.0, 2.0];

vehicles = VehicleParams()
vehicles.add(
    veh_id="human",
    acceleration_controller=accel_data,
    lane_change_params=SumoLaneChangeParams(
        model="SL2015",
        lc_sublane=2.0,
    ),
)

# Does this break the sim?
# vehicles.add(
#     veh_id="human2",
#     acceleration_controller=(LinearOVM,{'v_max':traffic_speed}),
#     lane_change_params=SumoLaneChangeParams(
#         model="SL2015",
#         lc_sublane=2.0,
#     ),
#     num_vehicles=1)

env_params = EnvParams(additional_params=ADDITIONAL_ENV_PARAMS)

inflow = InFlows()
inflow.add(
    veh_type="human",
    edge="highway_0",
    vehs_per_hour=traffic_flow,
    departLane="free",
    departSpeed=traffic_speed)

# inflow.add(
#     veh_type="human2",
#     edge="highway_0",
#     probability=0.25,
#     departLane="free",
#     departSpeed=20)


additional_net_params = ADDITIONAL_NET_PARAMS.copy()
additional_net_params['lanes'] = 1
additional_net_params['length'] = 1600
additional_net_params['end_speed_limit'] = 10.0
additional_net_params['boundary_cell_length'] = 100

flow_params = dict(
    # name of the experiment
    exp_tag='highway',
    # name of the flow environment the experiment is running on
    env_name=LaneChangeAccelEnv,
    # name of the network class the experiment is running on
    network=HighwayNetwork_Modified,
    # simulator that is used by the experiment
    simulator='traci',
    # sumo-related parameters (see flow.core.params.SumoParams)
    sim=SumoParams(
        sim_step=0.4,
        render=False,
        color_by_speed=False,
        emission_path='data/'+str(sys.argv[8]),
        use_ballistic=True
    ),
    # environment related parameters (see flow.core.params.EnvParams)
    env=EnvParams(
        horizon=500,
        additional_params=ADDITIONAL_ENV_PARAMS.copy(),
    ),
    # network-related parameters (see flow.core.params.NetParams and the
    # network's documentation or ADDITIONAL_NET_PARAMS component)
    net=NetParams(
        inflows=inflow,
        additional_params=additional_net_params,
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


#create experiment obj using flow params
exp = Experiment(flow_params)

# run the sumo simulation
_ = exp.run(1, convert_to_csv=True)

# to get data file as csv
emission_location = os.path.join(exp.env.sim_params.emission_path, exp.env.network.name)
print(emission_location + '-emission.xml')
pd.read_csv(emission_location + '-emission.csv')
