#!/bin/bash

echo "Analyzing data for Free Flow regime"
. freeFlow.sh
echo "Analyzing data for Congested Flow with Waves regime"
. congestedWaves.sh
echo "Analyzing data for Congested Flow with No Waves regime"
. congestedNoWaves.sh
