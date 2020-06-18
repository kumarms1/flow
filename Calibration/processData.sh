#!/bin/bash
# usage: . processData.sh experiment number simRepeatNum
echo "Processing macro data for 15 seconds fidelity"
p3 getMacroData.py exp$1_data exp$1_macro_15 15 IDMParams_exp$1.csv
echo "Processing macro data for 30 seconds fidelity"
p3 getMacroData.py exp$1_data exp$1_macro_30 30 IDMParams_exp$1.csv
echo "Processing macro data for 60 seconds fidelity"
p3 getMacroData.py exp$1_data exp$1_macro_60 60 IDMParams_exp$1.csv

echo "Creating plots for 15 seconds data taking range"
p3 graph.py exp$1_macro_15 15 $2
echo "Creating plots for 30 seconds data taking range"
p3 graph.py exp$1_macro_30 30 $2
echo "Creating plots for 30 seconds data taking range"
p3 graph.py exp$1_macro_60 60 $2
