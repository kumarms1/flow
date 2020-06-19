"""
usage: python3 getMacroData.py name_of_data_dir csvFileName fidelity params_file
example: p3 getMacroData.py exp4_data exp4_macro_15 15 ImMParams_exp4.csv 
"""

#import Process_Flow_Outputs and other libraries
import Process_Flow_Outputs as PFO
import matplotlib.pyplot as pt
import numpy as np
import csv
import os
import glob
import sys

def getCounts(csv_path,fname, params_file, index):
    #read data into a var
    highway_data = PFO.SimulationData(csv_path = csv_path)
    #highway_data.veh_ids
    #print(highway_data.data_ids)

    #get total position information
    pos_dict = highway_data.get_Timeseries_Dict(data_id='TOTAL_POSITION',want_Numpy=True)
    #get velocity information
    vel_dict =highway_data.get_Timeseries_Dict(data_id='SPEED',want_Numpy=True)
    """
    #generate the spacing data and save into a variable
    highway_data.get_Spacing()
    highway_data.data_ids
    spacing_dict = highway_data.get_Timeseries_Dict(data_id='SPACING',want_Numpy=True)
    """
    #car counting and velocityalgorithm
    position_for_count = 800 #radar reading position
    time_count_data = []  #array to store results
    vTime_array = [] # array to store (time, velocity) results

    for veh_id in highway_data.veh_ids:  #looping through all cars
        pos_data = pos_dict[veh_id] #store position information for each car
        end_pos = pos_data[1,-1]
        veh_data = vel_dict[veh_id]
        if(end_pos > position_for_count): #if car crossed the radar line point
            t=0
            p = pos_data[1,t] #position at which car was spawned
            while(p < position_for_count): 
                t += 1
                p = pos_data[1,t]
            vTime_array.append((pos_data[0,t],veh_data[1,t])) #(time stamp, velocity a  t time stamp) at which car passes the radar point
    #sort in time
    vTime_array.sort(key=lambda x: x[0])
 #   counts = np.linspace(1,len(sorted_count_times),len(sorted_count_times))
    #pt.plot(sorted_count_times,counts)
    #pt.show()
    count_num, average_speed = countsEveryXSeconds(int(sys.argv[3]), vTime_array)
    print("The counts are: ", count_num)
    print("The speeds are: ", average_speed)
    print("The IDM parameters are: ", determineParams(index, params_file))
    print("")
    writeToFile(sys.argv[2], count_num, average_speed, determineParams(index, params_file) )
    #print("Writing the counts data from " + fname + ".csv file")
    #with open("data/"+sys.argv[2]+"/"+fname+"_counts.csv", 'a', newline='') as file:
    #    writer = csv.writer(file)
    #    writer.writerows([count_num])
    #print("File Written\n") 

def writeToFile(fileName,c,a,p):
    csvName = "info/" + fileName + ".csv"
    with open(csvName, "a") as file:
        writer = csv.writer(file)
        writer.writerows([c,a,p])

#counts every X seconds
def countsEveryXSeconds(x, sorted_counts, trim=False):
        i = 0
        m = 0
        j = 1
        comp = x
        c = []
        mc = []
        meanSpeed = []

        while (i < len(sorted_counts)):
            while( (m!=len(sorted_counts)) and ((j-1)*comp <= sorted_counts[m][0] <=   j*comp) ) :
                c.append(sorted_counts[m])
                m+=1
            i = m
            j+=1
            d = c.copy()
            mc.append(d)
            #print(d)
            if (len(d) == 0):
                meanSpeed.append(0)
            else:
                meanSpeed.append(round(sum(i for _, i in d)/len(d),3))
            c.clear()
        mcc = []
        for k in mc:
            mcc.append(len(k))
        if (trim==True):
            mcc.pop()
            mcc.pop(0)
            mcc.pop(0)
        return mcc, meanSpeed

def determineParams(i,params_file):
    with open(params_file, newline='') as f:
      reader = csv.reader(f)
      params_list = list(reader)
    return params_list[i]

if __name__ == "__main__":
    files = glob.glob("data/"+sys.argv[1] + "/highway*.csv")
    files.sort(key=os.path.getmtime)
    params_file = str(sys.argv[4])
    index = 0
    #print(sys.argv[1])
    for i in files:
        fname = i.split("/")[2].split("-e")[0]
     #   print("file name: ", fname)
        getCounts(i,fname, params_file, index)
        index += 1

