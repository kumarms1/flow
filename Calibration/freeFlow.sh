#!/bin/bash

#get macro data file
p3 getMacroData.py FreeFlowExp7_data exp7freeFlow_macro_15 15 IDMParamsFreeFlow_exp7.csv
p3 getMacroData.py FreeFlowExp7_data exp7freeFlow_macro_30 30 IDMParamsFreeFlow_exp7.csv
p3 getMacroData.py FreeFlowExp7_data exp7freeFlow_macro_60 60 IDMParamsFreeFlow_exp7.csv

#get plots
p3 graph.py exp7freeFlow_macro_30 30 6
p3 graph.py exp7freeFlow_macro_15 15 6
p3 graph.py exp7freeFlow_macro_60 60 6
