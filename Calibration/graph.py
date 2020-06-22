"""
usage: python graph.py dataFile fidelity numSimsPerParam
example: p3 graph.py exp4_macro 30 6
"""
import csv
import sys, os
import matplotlib.pyplot as plt
import numpy as np

#process args
dataFile = "info/"+sys.argv[1]+".csv"
fidelity = int(sys.argv[2])
fileExt = "figs/"+str(sys.argv[1]).split("_")[0]+"/fidelity_"+str(fidelity)
num = int(sys.argv[3])

#create figure folder
os.makedirs(fileExt, exist_ok=True)

#function definition
def list_slice(S, step):
    return [S[i::step] for i in range(step)]

def plotCountsGraph(yvals, title, vals, figName):
      for i in range(len(yvals)):
          plt.plot([fidelity*i for i in range(len(yvals[i]))], yvals[i], '-o',label=vals[i])
          plt.legend(loc="best")
          plt.xlabel("Time Period (s)")
          plt.ylabel("Car Counts (units)")
          plt.title(title)
        #  plt.ylim(0,17)
      plt.savefig(fileExt+"/"+figName+".png")
      plt.show()

def plotVelocityGraph(yvals, title, vals, figName):
      for i in range(len(yvals)):
          plt.plot([fidelity*i for i in range(len(yvals[i]))], yvals[i],'-o',label=vals[i]) 
          plt.legend(loc="best")
          plt.xlabel("Time Period (s)")
          plt.ylabel("Average Velocity (m/s)")
          plt.title(title)
        #  plt.ylim(0,17)
      plt.savefig(fileExt+"/"+figName+".png")
      plt.show()


# for IDMparams
def getParamVals(params_list, index, num):
      if index == 0: #a
          p =  [round(float(params_list[i][index]),2) for i in range(len(params_list)) if i < (num+1)]
          return p
      elif index == 1: #b
          p =  [round(float(params_list[i][index]),2) for i in range(len(params_list)) if (  (i==0) or  (num < i < (2*num+1) ) ) ]
          return p
      elif index == 2: #noise
          p =  [round(float(params_list[i][index]),2) for i in range(len(params_list)) if (  (i==0) or  ( (2*num) < i < ((3*num+1) )) )]
          return p
      elif index == 3: #v0
          p =  [round(float(params_list[i][index]),2) for i in range(len(params_list)) if (  (i==0) or  ( (3*num)  < i < (4*num+1)  ) )]
          return p
      elif index == 4: #T
          p =  [round(float(params_list[i][index]),2) for i in range(len(params_list)) if (  (i==0) or  ((4*num) < i < (5*num+1)  ) )]
          return p
      elif index == 5: #delta
          p =  [round(float(params_list[i][index]),2) for i in range(len(params_list)) if (  (i==0) or  ( (5*num) < i < (6*num+1)  ) )]
          return p
      elif index == 6: #s0
          p =  [round(float(params_list[i][index]),2) for i in range(len(params_list)) if (  (i==0) or  ( (6*num) < i < (7*num +1)) )]
          return p

def find_min_list_size(lists):
    list_len = [len(i) for i in lists]
    return min(list_len)


def getRelationships(macroArray, paramSet, param, macro):
    #determine the min size of array in macroArray
    minSize = find_min_list_size(macroArray)
    avg = []
    maxD = []
    minD = []
    figName = param+"_"+macro+"_stats"
    for arr in macroArray:
        #trim all arrays in the macroArray based on that number
        while len(arr) > minSize:
            arr.pop()
        #calculate average based on that number
        avg.append(sum(arr)/len(arr))
        #calculate min and max based on that number
        maxD.append(max(arr))
        minD.append(min(arr))
        # plot against paramSet
    plt.scatter(paramSet, avg, label="mean")
    plt.scatter(paramSet, maxD, label="max")
    plt.scatter(paramSet, minD, label="min")
    plt.xlabel("Parameter: " + param)
    plt.ylabel(macro)
    plt.legend()
    plt.title("Effect of \"" + param + "\" on macro data: " + macro)
    plt.savefig(fileExt+"/"+figName+".png")
    plt.show()

#read data
results = []
with open(dataFile, 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        line = list(map(float, line))
        results.append(line)

#process data
runs = list_slice(results, 3)
counts = runs[0]
velocity = runs[1]
params = runs[2]


# reading the counts for IDM params
a_counts = [counts[i] for i in range(len(counts)) if i < (num+1) ]
b_counts = [counts[i] for i in range(len(counts)) if (  (i==0) or  ( num  < i < (2*num+1)  ) )]
noise_counts = [counts[i] for i in range(len(counts)) if (  (i==0) or  ( (2*num)  < i < (3*num+1)  ) )]
v0_counts = [counts[i] for i in range(len(counts)) if (  (i==0) or  ( (3*num)  < i < (4*num+1)  ) )]
T_counts = [counts[i] for i in range(len(counts)) if (  (i==0) or  ( (4*num)  < i < (5*num+1) ) )]
delta_counts = [counts[i] for i in range(len(counts)) if (  (i==0) or  ( (5*num)  < i <  (6*num+1) ) )]
s0_counts = [counts[i] for i in range(len(counts)) if (  (i==0) or  ( (6*num)  < i <  (7*num+1) ) )]

#all_counts_data = [a_counts,b_counts,v0_counts,T_counts,delta_counts,s0_counts]

# reading the velocity for IDM params
a_velocity = [velocity[i] for i in range(len(velocity)) if i < (num+1) ]
b_velocity = [velocity[i] for i in range(len(velocity)) if (  (i==0) or  ( num  < i < (2*num+1)  ) )]
noise_velocity = [velocity[i] for i in range(len(velocity)) if (  (i==0) or  ( (2*num)  < i < (3*num+1)  ) )]
v0_velocity = [velocity[i] for i in range(len(velocity)) if (  (i==0) or  ( (3*num)  < i < (4*num+1)  ) )]
T_velocity = [velocity[i] for i in range(len(velocity)) if (  (i==0) or  ( (4*num)  < i < (5*num+1) ) )]
delta_velocity = [velocity[i] for i in range(len(velocity)) if (  (i==0) or  ( (5*num)  < i <  (6*num+1) ) )]
s0_velocity = [velocity[i] for i in range(len(velocity)) if (  (i==0) or  ( (6*num)  < i <  (7*num+1) ) )]

#all_velocity_data = [a_velocity,b_velocity,v0_velocity,T_velocity,delta_velocity,s0_velocity]

getRelationships(a_counts, getParamVals(params,0,num), "a", "Counts") 
getRelationships(b_counts, getParamVals(params,1,num), "b", "Counts") 
getRelationships(v0_counts, getParamVals(params,3,num), "v0", "Counts") 
getRelationships(T_counts, getParamVals(params,4,num), "T", "Counts") 
getRelationships(delta_counts, getParamVals(params,5,num), "delta", "Counts") 
getRelationships(s0_counts, getParamVals(params,6,num), "s0", "Counts") 


getRelationships(a_velocity, getParamVals(params,0,num), "a", "Velocity") 
getRelationships(b_velocity, getParamVals(params,1,num), "b", "Velocity") 
getRelationships(v0_velocity, getParamVals(params,3,num), "v0", "Velocity") 
getRelationships(T_velocity, getParamVals(params,4,num), "T", "Velocity") 
getRelationships(delta_velocity, getParamVals(params,5,num), "delta", "Velocity") 
getRelationships(s0_velocity, getParamVals(params,6,num), "s0", "Velocity") 
"""
#plot counts graphs
plotCountsGraph(a_counts, "Varying the \"a\" parameter", getParamVals(params,0,num) ,"a_params_counts")
plotCountsGraph(b_counts, "Varying the \"b\" parameter", getParamVals(params,1,num) ,"b_params_counts")
plotCountsGraph(v0_counts,"Varying the \"v0\" parameter", getParamVals(params,3,num) ,"v0_params_counts")
plotCountsGraph(T_counts, "Varying the \"T\" parameter", getParamVals(params,4,num) ,"T_params_counts")
plotCountsGraph(delta_counts, "Varying the \"delta\" parameter", getParamVals(params,5,num) ,"delta_params_counts")
plotCountsGraph(s0_counts, "Varying the \"s0\" parameter", getParamVals(params,6,num) ,"s0_params_counts")

#plot velocity graphs
plotVelocityGraph(a_velocity, "Varying the \"a\" parameter", getParamVals(params,0,num) ,"a_params_velocity")
plotVelocityGraph(b_velocity, "Varying the \"b\" parameter", getParamVals(params,1,num) ,"b_params_velocity")
plotVelocityGraph(v0_velocity, "Varying the \"v0\" parameter", getParamVals(params,3,num) ,"v0_params_velocity")
plotVelocityGraph(T_velocity, "Varying the \"T\" parameter", getParamVals(params,4,num) ,"T_params_velocity")
plotVelocityGraph(delta_velocity, "Varying the \"delta\" parameter", getParamVals(params,5,num) ,"delta_params_velocity")
plotVelocityGraph(s0_velocity, "Varying the \"s0\" parameter", getParamVals(params,6,num) ,"s0_params_velocity")
"""




"""
popping last run
"""
#counts.pop()
#velocity.pop()
#params.pop()

#print(getParamVals(params,1,num))

#for i in params:
#    print(i)
