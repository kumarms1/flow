#!/bin/bash

#get macro data file
#p3 getMacroData.py CongestedWavesExp8_data exp8congestedWaves_macro_15 15 IDMParamsCongestedWaves_exp8.csv
#p3 getMacroData.py CongestedWavesExp8_data exp8congestedWaves_macro_30 30 IDMParamsCongestedWaves_exp8.csv
#p3 getMacroData.py CongestedWavesExp8_data exp8congestedWaves_macro_60 60 IDMParamsCongestedWaves_exp8.csv

#get plots
p3 graph.py exp8congestedWaves_macro_30 30 6
p3 graph.py exp8congestedWaves_macro_15 15 6
p3 graph.py exp8congestedWaves_macro_60 60 6
