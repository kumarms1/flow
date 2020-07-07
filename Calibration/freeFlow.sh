#!/bin/bash

#get macro data file
p3 getMacroData.py exp11_data exp11freeFlow_macro_15 15 IDMParams_exp11LongSim.csv
p3 getMacroData.py exp11_data exp11freeFlow_macro_30 30 IDMParams_exp11LongSim.csv
p3 getMacroData.py exp11_data exp11freeFlow_macro_60 60 IDMParams_exp11LongSim.csv

#get plots
p3 graph.py exp11freeFlow_macro_30 30 6
p3 graph.py exp11freeFlow_macro_15 15 6
p3 graph.py exp11freeFlow_macro_60 60 6
