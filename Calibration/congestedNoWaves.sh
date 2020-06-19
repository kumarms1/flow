#!/bin/bash

#get macro data file
p3 getMacroData.py exp6_data_congestedNoWaves exp6_macro_15 15 IDMParamsCongestedNoWaves_exp6.csv
p3 getMacroData.py exp6_data_congestedNoWaves exp6_macro_30 30 IDMParamsCongestedNoWaves_exp6.csv
p3 getMacroData.py exp6_data_congestedNoWaves exp6_macro_60 60 IDMParamsCongestedNoWaves_exp6.csv

#get plots
p3 graph.py exp6_macro_15 15 6
p3 graph.py exp6_macro_30 30 6
p3 graph.py exp6_macro_60 60 6
