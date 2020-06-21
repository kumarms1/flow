#!/bin/bash

#free flow
. automate_free.sh 6 IDMParamsFreeFlow_exp7.csv FreeFlowExp7_data free 

#congested with waves
. automate_congested.sh 6 IDMParamsCongestedWaves_exp8.csv CongestedWavesExp8_data congestedWaves

#congested with no waves
. automate_congested.sh 6 IDMParamsCongestedNoWaves_exp9.csv CongestedNoWavesExp9_data congestedNoWaves

