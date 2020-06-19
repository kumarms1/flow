#!/bin/bash

#get macro data file
p3 getMacroData.py exp5_data_congestedWaves exp5_macro_15 15 IDMParamsCongestedWaves_exp5.csv
p3 getMacroData.py exp5_data_congestedWaves exp5_macro_30 30 IDMParamsCongestedWaves_exp5.csv
p3 getMacroData.py exp5_data_congestedWaves exp5_macro_60 60 IDMParamsCongestedWaves_exp5.csv

#get plots
p3 graph.py exp5_macro_30 30 6
p3 graph.py exp5_macro_15 15 6
p3 graph.py exp5_macro_60 60 6
