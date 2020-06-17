"""
@author: Sadman Ahmed Shanto
pseudocode:
    read micro data: volume, flow rate, speed, density
    store data in arrays
    calculate macro quantities
    create plots: time_space, fd
    save micro data

functionality:
    function that reads data at every X miles
    function that reads data at every X cars
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

# function definitions
def getDataEveryXSeconds(X, df):
    return df[(df['time'] % X == 0) | (df['time']==1.0)] #includes the first data entry

def getGraph(quant,typeGraph="line",title="",label_axes=["",""]):
    quant.plot(kind=typeGraph)
    plt.title(title)
    plt.xlabel(label_axes[0])
    plt.ylabel(label_axes[1])
    plt.show()


#read data
if (len(sys.argv) < 2):
    fn = str(input("Please input data file name: "))
    dataFile = "data/" + fn
else:
    dataFile = "data/" + str(sys.argv[1])

#store data as a data frame
df = pd.read_csv(dataFile)
#getGraph(df['x'])
#getGraph(df['relative_position'], "line", "Relative Position", ["Time (ms)","Position (m)"] )

#process data
dfTime = getDataEveryXSeconds(30, df)
print(dfTime)
time = dfTime['time']

numVehiclesEachTimePeriod = dfTime.groupby('time')['id'].count()
print(numVehiclesEachTimePeriod)
#getGraph(numVehiclesEachTimePeriod, "bar", "Number of Vehicles per 30 seconds", ["Time (s)", "Number of Vehicles"])


"""
y = dfTime['y']
x = dfTime['x']
vehId = dfTime['id']
rp = dfTime['relative_position']
angle = dfTime['angle']
speed = dfTime['speed']
"""


