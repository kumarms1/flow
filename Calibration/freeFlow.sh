#!/bin/bash

#get macro data file
#p3 getMacroData.py exp10_data exp10freeFlow_macro_15 15 IDMParams_exp10LongSims.csv
#p3 getMacroData.py exp10_data exp10freeFlow_macro_30 30 IDMParams_exp10LongSims.csv
#p3 getMacroData.py exp10_data exp10freeFlow_macro_60 60 IDMParams_exp10LongSims.csv

#get plots
p3 graph.py exp10freeFlow_macro_30 30 6
p3 graph.py exp10freeFlow_macro_15 15 6
p3 graph.py exp10freeFlow_macro_60 60 6
