"""
usage: python3 getMacroData.py name_of_data_dir name_of_processed_data_to_be_created_dir fidelity
"""

#import Process_Flow_Outputs and other libraries
import Process_Flow_Outputs as PFO
import matplotlib.pyplot as pt
import numpy as np
import csv
import os
import glob
import sys

os.mkdir("data/"+sys.argv[2])

def getCounts(csv_path,fname):
    #read data into a var
    highway_data = PFO.SimulationData(csv_path = csv_path)
    #highway_data.veh_ids
    #print(highway_data.data_ids)

    #get total position information
    pos_dict = highway_data.get_Timeseries_Dict(data_id='TOTAL_POSITION',want_Numpy=True)
    pos_data = pos_dict[highway_data.veh_ids[0]]

    #np.shape(pos_data)
    #pt.plot(pos_data[0,:],pos_data[1,:])
    """
    #generate the spacing data and save into a variable
    highway_data.get_Spacing()
    highway_data.data_ids
    spacing_dict = highway_data.get_Timeseries_Dict(data_id='SPACING',want_Numpy=True)
    """
    #car counting algorithm
    position_for_count = 800 #radar reading position
    time_count_data = []  #array to store results
    for veh_id in highway_data.veh_ids:  #looping through all cars
        pos_data = pos_dict[veh_id] #store position information for each car
        end_pos = pos_data[1,-1] 
        if(end_pos > position_for_count): #if car crossed the radar line point
            t=0
            p = pos_data[1,t] #position at which car was spawned
            while(p < position_for_count): 
                t += 1
                p = pos_data[1,t]
            time_count_data.append(pos_data[0,t]) #add time at which car crossed the radar to the array

    #len(time_count_data) #number of cars that crossed the line
    #len(highway_data.veh_ids)

    sorted_time_count_data = np.sort(time_count_data)
    sorted_count_times = sorted_time_count_data

 #   counts = np.linspace(1,len(sorted_count_times),len(sorted_count_times))
    #pt.plot(sorted_count_times,counts)
    #pt.show()
    count_num = countsEveryXSeconds(int(sys.argv[3]), sorted_count_times)
    print("Writing the counts data from " + fname + ".csv file")
    with open("data/"+sys.argv[2]+"/"+fname+"_counts.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([count_num])
    print("File Written\n")    

#counts every X seconds
def countsEveryXSeconds(x, sorted_counts, trim=False):
    i = 0
    m = 0
    j = 1
    comp = x
    c = []
    mc = []
    while (i < len(sorted_counts)):
        while( (m!=len(sorted_counts)) and ((j-1)*comp <= sorted_counts[m] <= j*comp) ) :
            c.append(sorted_counts[m])
            m+=1
        i = m
        j+=1
        d = c.copy()
        mc.append(d)
        c.clear()
    mcc = []
    for k in mc:
        mcc.append(len(k))
    if (trim==True):
        mcc.pop()
        mcc.pop(0)
        mcc.pop(0)
    return mcc


if __name__ == "__main__":
    files = glob.glob("data/"+sys.argv[1] + "/highway*.csv")
    files.sort(key=os.path.getmtime)
    print(sys.argv[1])
    for i in files:
        fname = i.split("/")[2].split("-e")[0]
        getCounts(i,fname)

