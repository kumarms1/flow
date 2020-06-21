#!/bin/bash
# usage: . automate.sh num_of_sims csvFileName.csv dataDirectory regime 

#determine how many input params to generate
python3 generate_data.py $1 $2 $4

#run the simulations
. exec_sim_free.sh $2 $3 $1
