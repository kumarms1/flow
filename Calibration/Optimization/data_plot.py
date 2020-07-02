import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

RDS_path = 'data/' + sys.argv[1]
num = sys.argv[1].split(".csv")[0]
RDS_DataTrack = pd.read_csv(RDS_path,delimiter=',')

def tidyData(RDS_DataTrack):
    RDS_DataTrack = RDS_DataTrack.drop(RDS_DataTrack[RDS_DataTrack['speed'] == " -"].index).reset_index(drop=True)
    RDS_DataTrack = RDS_DataTrack.drop(RDS_DataTrack[RDS_DataTrack['speed'] == " 0"].index).reset_index(drop=True)
    return RDS_DataTrack

def convertTimeStampts(RDS_DataTrack):
    for i in range(len(RDS_DataTrack['timestamp'])):
        hrs=int(RDS_DataTrack['timestamp'][i][:2])
        mins=int(RDS_DataTrack['timestamp'][i][3:5])
        secs=int(RDS_DataTrack['timestamp'][i][6:8])
        total_seconds = hrs*3600 + mins*60 + secs
        RDS_DataTrack['timestamp'][i] = total_seconds

def createPlot( x_arr, y_arr, color_arr, x_label,y_label,title, figName,color=True):
    if color:
        plt.scatter(x_arr, y_arr, c=color_arr.astype(int), s=.5, cmap='viridis')
        plt.colorbar()
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.savefig("figures/"+figName)
        plt.show()
    else:
        plt.scatter(x_arr, y_arr, s=.5)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.savefig("figures/"+figName)
        plt.show()

def getDensity(RDS_DataTrack):
    density = []
    for i in range(len(RDS_DataTrack['volume'])):
       # print(RDS_DataTrack['volume'][i])
        density.append(  ( 12.0*float(RDS_DataTrack['volume'][i]) ) / float( RDS_DataTrack['speed'][i] ))
    return density


def fixDataFidelity(RDS_DataTrack,fidelity):
    pass


RDS_DataTrack = tidyData(RDS_DataTrack)
convertTimeStampts(RDS_DataTrack)
density = getDensity(RDS_DataTrack)
createPlot(RDS_DataTrack['timestamp'], RDS_DataTrack['volume']*12, RDS_DataTrack['speed'] ,"time series (s)", "Flow (vehicle/hour)", "Flow against Time", "flow_time_"+num+".png")
createPlot(RDS_DataTrack['timestamp'], RDS_DataTrack['speed'], RDS_DataTrack['speed'],"time series (s)", "Average Speed (miles/hour)", "Speed against Time", "speed_time_"+num+".png", False)
createPlot(RDS_DataTrack['speed'], RDS_DataTrack['volume']*12, RDS_DataTrack['speed'], "Average Speed (miles/hour)", "Flow (vehicle/hour)","Flow against Speed", "flow_speed_"+num+".png", False)
createPlot(RDS_DataTrack['timestamp'], density, RDS_DataTrack['speed'] ,"time series (s)", "Density (vehicle/mile)", "Density against Time", "density_time_"+num+".png")
createPlot(density, 12*RDS_DataTrack['volume'] ,RDS_DataTrack['speed'] , "Density (vehicle/mile)", "Flow (vehicle/hour)", "Fundamental Diagram", "fundamental_diagram_"+num+".png")
createPlot(density, RDS_DataTrack['speed'] ,RDS_DataTrack['speed'] , "Density (vehicle/mile)", "Speed (miles/hour)", "Speed against Density", "speed_density_"+num+".png",False)
