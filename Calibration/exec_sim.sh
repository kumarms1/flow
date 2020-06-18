#!/bin/bash
INPUT=$1
OLDIFS=$IFS
IFS=','
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
expNum=0
while read a b noise v0 T delta s0 
do      
        expNum=$(( expNum + 1 )) 
        echo  "==================================================="
        echo " Simulation: $expNum "
        echo  " IDM Parameters"
	echo -e "\tAcceleration : $a"
	echo -e "\tDeceleration : $b"
	echo -e "\tNoise : $noise"
	echo -e "\tDesirable Velocity : $v0"
	echo -e "\tSafe Time Headway : $T"
	echo -e "\tAcceleration exponent : $delta"
	echo -e "\tLinear Jam Distance : $s0"
        echo " Starting simulation with the given parameters ... "
        python3 straight_road_test.py $a $b $noise $v0 $T $delta $s0 $2
        echo " Simulation complete!"
        echo "==================================================="
	echo ""
done < $INPUT
IFS=$OLDIFS

echo "All data taking is complete"  

#process data to get macro data
#create graphs
