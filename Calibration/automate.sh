#!/bin/bash
# usage: . automate.sh num_of_sims csvFileName.csv dataDirectory fidelity

#determine how many input params to generate
python3 generate_data.py $1 $2

#run the simulations
. exec_sim.sh $2 $3 $1 $4
