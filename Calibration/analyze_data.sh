# . analyze_data.sh exp_num fidelity inputParams.csv multiple_num_sim

#get macro data
python3 getMacroData.py exp$1_data exp$1_res_$2 $2
#get plots
python3 createMacroGraphs.py exp$1_res_$2 $3 $4 exp$1_res_$2 $2
