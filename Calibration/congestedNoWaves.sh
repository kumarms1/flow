#!/bin/bash

#get macro data file
p3 getMacroData.py CongestedNoWavesExp9_data exp9congestedNoWaves_macro_15 15 IDMParamsCongestedNoWaves_exp9.csv
p3 getMacroData.py CongestedNoWavesExp9_data exp9congestedNoWaves_macro_30 30 IDMParamsCongestedNoWaves_exp9.csv
p3 getMacroData.py CongestedNoWavesExp9_data exp9congestedNoWaves_macro_60 60 IDMParamsCongestedNoWaves_exp9.csv

#get plots
p3 graph.py exp9congestedNoWaves_macro_30 30 6
p3 graph.py exp9congestedNoWaves_macro_15 15 6
p3 graph.py exp9congestedNoWaves_macro_60 60 6
