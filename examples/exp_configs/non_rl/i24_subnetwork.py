"""I-24 subnetwork example."""
import os

import numpy as np

from flow.controllers.car_following_models import IDMController
from flow.controllers.lane_change_controllers import StaticLaneChanger
from flow.controllers.routing_controllers import I24Router  #new
from flow.core.params import SumoParams
from flow.core.params import EnvParams
from flow.core.params import NetParams
from flow.core.params import SumoLaneChangeParams
from flow.core.params import VehicleParams
from flow.core.params import InitialConfig
from flow.core.params import InFlows

from flow.core.params import SumoCarFollowingParams

import flow.config as config
from flow.envs import TestEnv
 
from flow.networks.i24_subnetwork import I24SubNetwork, EDGES_DISTRIBUTION #changed
# Instantiate which conditions we want to be true about the network

"""
WANT_GHOST_CELL = True
WANT_DOWNSTREAM_BOUNDARY = True
ON_RAMP = False
"""

inflow_rate = 2050
inflow_speed = 25.5

accel_data = (IDMController,{'a':1.3,'b':2.0,'noise':0.3})
highway_start_edge = '108162443'

vehicles = VehicleParams()

inflow = InFlows()

vehicles.add(
    "human",
    num_vehicles=0,
    lane_change_params=SumoLaneChangeParams(
        lane_change_mode="strategic",
    ),
    acceleration_controller=accel_data,
    routing_controller=(I24Router, {})
)

    # inflow.add(
    #     veh_type="human",
    #     edge=highway_start_edge,
    #     vehs_per_hour=inflow_rate,
    #     departLane="best",
    #     departSpeed=inflow_speed)

lane_list = ['0','1','2','3']

"""
inflow.add(
    veh_type="human",
    edge="108162443",
    vehs_per_hour=500,
    departLane="random",
    departSpeed=10)
"""
for lane in lane_list:
    inflow.add(
        veh_type="human",
        edge=highway_start_edge,
        vehs_per_hour=inflow_rate,
        departLane="random",
        departSpeed=inflow_speed)
    """
    # edge/route for 108162065 not defined
    inflow.add(
        veh_type="human",
        edge="108162065",
        vehs_per_hour=inflow_rate+2,
        departLane="random",
        departSpeed=inflow_speed)
    """

"""
inflow.add(
    veh_type="human",
    edge="27414345",
    vehs_per_hour=500,
    departLane="random",
    departSpeed=10)
inflow.add(
    veh_type="human",
    edge="27414342#0",
    vehs_per_hour=500,
    departLane="random",
    departSpeed=10)
"""
    # If you want to turn off the fail safes uncomment this:

    # vehicles.add(
    #     'human',
    #     num_vehicles=0,
    #     lane_change_params=SumoLaneChangeParams(
    #         lane_change_mode='strategic',
    #     ),
    #     acceleration_controller=accel_data,
    #     car_following_params=SumoCarFollowingParams(speed_mode='19')
    # )

network_xml_file = "examples/exp_configs/templates/sumo/i24_trim.net.xml"

# network_xml_file = "examples/exp_configs/templates/sumo/i210_with_congestion.xml"

NET_TEMPLATE = os.path.join(config.PROJECT_PATH,network_xml_file)


flow_params = dict(
    # name of the experiment
    exp_tag='I-24_subnetwork',

    # name of the flow environment the experiment is running on
    env_name=TestEnv,

    # name of the network class the experiment is running on
    network=I24SubNetwork,

    # simulator that is used by the experiment
    simulator='traci',

    # simulation-related parameters
    sim=SumoParams(
        sim_step=0.4,
        render=False,
        color_by_speed=True,
        use_ballistic=True,
        restart_instance=True
    ),

    # environment related parameters (see flow.core.params.EnvParams)
    env=EnvParams(
        horizon=1000,
    ),

    # network-related parameters (see flow.core.params.NetParams and the
    # network's documentation or ADDITIONAL_NET_PARAMS component)
    net=NetParams(
        inflows=inflow,
        template=NET_TEMPLATE,
        additional_params={}
    ),

    # vehicles to be placed in the network at the start of a rollout (see
    # flow.core.params.VehicleParams)
    veh=vehicles,

    # parameters specifying the positioning of vehicles upon initialization/
    # reset (see flow.core.params.InitialConfig)
    initial=InitialConfig(
        edges_distribution=EDGES_DISTRIBUTION,
    ),
)