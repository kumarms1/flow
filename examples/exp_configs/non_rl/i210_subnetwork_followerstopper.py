"""I-210 subnetwork example."""
import os

import numpy as np

from flow.controllers.car_following_models import IDMController
from flow.controllers.lane_change_controllers import StaticLaneChanger
from flow.controllers.routing_controllers import I210Router
from flow.controllers.velocity_controllers import DynamicDelayFollowerStopper
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

# Instantiate which conditions we want to be true about the network

WANT_GHOST_CELL = True
WANT_DOWNSTREAM_BOUNDARY = True
ON_RAMP = False


inflow_rate = 2050
inflow_speed = 25.5


accel_data = (IDMController,{'a':1.3,'b':2.0,'noise':0.3})
accel_data2 = (DynamicDelayFollowerStopper,{'delay':0})

highway_start_edge = ''

if(WANT_GHOST_CELL):
    from flow.networks.i210_subnetwork_ghost_cell import I210SubNetwork, EDGES_DISTRIBUTION
    highway_start_edge = 'ghost0'
else:
    from flow.networks.i210_subnetwork import I210SubNetwork, EDGES_DISTRIBUTION
    highway_start_edge = "119257914"


vehicles = VehicleParams()

inflow = InFlows()

if ON_RAMP:   
    vehicles.add(
        "human",
        num_vehicles=0,
        lane_change_params=SumoLaneChangeParams(
            lane_change_mode="strategic",
        ),
        acceleration_controller=accel_data,
        routing_controller=(I210Router, {})
    )

    # inflow.add(
    #     veh_type="human",
    #     edge=highway_start_edge,
    #     vehs_per_hour=inflow_rate,
    #     departLane="best",
    #     departSpeed=inflow_speed)

    lane_list = ['0','1','2','3','4']

    for lane in lane_list:
        inflow.add(
            veh_type="human",
            edge=highway_start_edge,
            vehs_per_hour=inflow_rate,
            departLane=lane,
            departSpeed=inflow_speed)

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

else:
    # create the base vehicle type that will be used for inflows
    vehicles.add(
        "human",
        num_vehicles=0,
        lane_change_params=SumoLaneChangeParams(
            lane_change_mode="strategic",
        ),
        acceleration_controller=accel_data,
    )

    vehicles.add(
        "auto",
        num_vehicles=0,
        lane_change_params=SumoLaneChangeParams(
            lane_change_mode="strategic",
        ),
        acceleration_controller=accel_data2,
    )
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

    lane_list = ['0','1','2','3','4']

    for lane in lane_list:
        inflow.add(
            veh_type="human",
            edge=highway_start_edge,
            vehs_per_hour=inflow_rate*0.9,
            departLane=lane,
            departSpeed=inflow_speed)

        inflow.add(
            veh_type="auto",
            edge=highway_start_edge,
            vehs_per_hour=inflow_rate*0.1,
            departLane=lane,
            departSpeed=inflow_speed)

network_xml_file = "examples/exp_configs/templates/sumo/i210_with_ghost_cell_with_downstream.xml"

# network_xml_file = "examples/exp_configs/templates/sumo/i210_with_congestion.xml"

NET_TEMPLATE = os.path.join(config.PROJECT_PATH,network_xml_file)


flow_params = dict(
    # name of the experiment
    exp_tag='I-210_subnetwork',

    # name of the flow environment the experiment is running on
    env_name=TestEnv,

    # name of the network class the experiment is running on
    network=I210SubNetwork,

    # simulator that is used by the experiment
    simulator='traci',

    # simulation-related parameters
    sim=SumoParams(
        sim_step=0.5,
        render=False,
        color_by_speed=True,
        use_ballistic=True
    ),

    # environment related parameters (see flow.core.params.EnvParams)
    env=EnvParams(
        horizon=800,
    ),

    # network-related parameters (see flow.core.params.NetParams and the
    # network's documentation or ADDITIONAL_NET_PARAMS component)
    net=NetParams(
        inflows=inflow,
        template=NET_TEMPLATE,
        additional_params={"use_on_ramp": ON_RAMP}
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

edge_id = "119257908#1-AddedOnRampEdge"
custom_callables = {
    "avg_merge_speed": lambda env: np.nan_to_num(np.mean(
        env.k.vehicle.get_speed(env.k.vehicle.get_ids_by_edge(edge_id)))),
    "avg_outflow": lambda env: np.nan_to_num(
        env.k.vehicle.get_outflow_rate(120)),
    # we multiply by 5 to account for the vehicle length and by 1000 to convert
    # into veh/km
    "avg_density": lambda env: 5 * 1000 * len(env.k.vehicle.get_ids_by_edge(
        edge_id)) / (env.k.network.edge_length(edge_id)
                     * env.k.network.num_lanes(edge_id)),
}
