import Process_Flow_Outputs as PFO
import matplotlib.pyplot as pt
import numpy as np
import csv
import os
import glob
import sys

"""
pseudocode:
1) look at one point on road (800 m)
2) When a vehicle passes that point store its speed.
3) for each time aggregate (say 30 seconds) find the measurements that fit in that slot and then take the average of those speeds
4) Use those measurements in the same manner we use counts
"""

csv_path = "/Users/sshanto/summer_2020/vu/flow/Calibration/data/exp4_data/highway_20200617-1401231592420483.756893-emission.csv"

highway_data = PFO.SimulationData(csv_path = csv_path)

#get total position information
pos_dict = highway_data.get_Timeseries_Dict(data_id='TOTAL_POSITION',want_Numpy=True)

#get velocity information
vel_dict =highway_data.get_Timeseries_Dict(data_id='SPEED',want_Numpy=True)

#car counting algorithm
position_for_count = 800 #radar reading position
time_count_data = []  #array to store results
vTime_array = []

#print(vel_dict[highway_data.veh_ids[0]][1])

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
        vTime_array.append((pos_data[0,t],veh_data[1,t])) #(time stamp, velocity at time stamp) at which car passes the radar point

#sort in time
vTime_array.sort(key=lambda x: x[0])

#print(vTime_array)

def averageSpeedEveryXSeconds(X,arr):
    pass

def countsEveryXSeconds(x, sorted_counts, trim=False):
      i = 0
      m = 0
      j = 1
      comp = x
      c = []
      mc = []
      meanSpeed = []

      while (i < len(sorted_counts)):
          while( (m!=len(sorted_counts)) and ((j-1)*comp <= sorted_counts[m][0] <= j*comp) ) :
              c.append(sorted_counts[m])
              m+=1
          i = m
          j+=1
          d = c.copy()
          mc.append(d)
          print(d)
          if len(d)==0:
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

c, v = countsEveryXSeconds(30, vTime_array)

print(v)
