import glob
import os, csv, sys
import matplotlib.pyplot as plt
import numpy as np

#files1 = glob.glob(sys.argv[1]+"/*csv")
files1 = glob.glob("data/"+str(sys.argv[1])+"/*csv")
files1.sort(key=os.path.getmtime)

params = str(sys.argv[2])
num = int(sys.argv[3])

#params = "newSimIDMParams.csv"
#num = 7

counts_list = []
avg_counts_list = []


for file in files1:
    with open(file, 'r') as csvfile:
        content = csv.reader(csvfile)
        for line in content:
            line = list(map(int, line))
            counts_list.append(line)
            avg_counts_list.append(sum(line)/len(line))

#print(len(avg_counts_list))

with open(params, newline='') as f:
    reader = csv.reader(f)
    params_list = list(reader)


def getParamVals(params_list, index):
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

# reading the counts
a_counts = [counts_list[i] for i in range(len(counts_list)) if i < (num+1) ]
b_counts = [counts_list[i] for i in range(len(counts_list)) if (  (i==0) or  ( num  < i < (2*num+1)  ) )]
noise_counts = [counts_list[i] for i in range(len(counts_list)) if (  (i==0) or  ( (2*num)  < i < (3*num+1)  ) )]
v0_counts = [counts_list[i] for i in range(len(counts_list)) if (  (i==0) or  ( (3*num)  < i < (4*num+1)  ) )]
T_counts = [counts_list[i] for i in range(len(counts_list)) if (  (i==0) or  ( (4*num)  < i < (5*num+1) ) )]
delta_counts = [counts_list[i] for i in range(len(counts_list)) if (  (i==0) or  ( (5*num)  < i <  (6*num+1) ) )]
s0_counts = [counts_list[i] for i in range(len(counts_list)) if (  (i==0) or  ( (6*num)  < i <  (7*num+1) ) )]
#random_counts = counts_list[36]


def getError(counts):
    for i in counts:
        print(len(i))
    ref = np.array(counts[0])
    error = []
    i = 1
    while (i<len(counts)):
        pres = np.array(counts[i])
        err = np.average(pres-ref)
        print("ref: ", ref)
        print("current: ", pres)
        print("error: ", err)
        print("")
        error.append(err)
        i+=1 
    print(error)
    return error

def plotGraph(yvals, title, vals, figName):
    for i in range(len(yvals)):
        plt.plot([30*i for i in range(len(yvals[i]))], yvals[i], label=vals[i]) #need to update the time period
        plt.legend(loc="best")
        plt.xlabel("Time (s)")
        plt.ylabel("Car Counts (units)")
        plt.title(title)
    plt.savefig("figs/"+figName+".png")
    plt.show()

#getError(a_counts)
plotGraph(a_counts, "Varying the \"a\" parameter", getParamVals(params_list,0) ,"a_params")
plotGraph(b_counts, "Varying the \"b\" parameter", getParamVals(params_list,1) ,"b_params")
plotGraph(noise_counts, "Varying the \"noise\" parameter", getParamVals(params_list,2) ,"noise_params")
plotGraph(v0_counts,"Varying the \"v0\" parameter", getParamVals(params_list,3) ,"v0_params")
plotGraph(T_counts, "Varying the \"T\" parameter", getParamVals(params_list,4) ,"T_params")
plotGraph(delta_counts, "Varying the \"delta\" parameter", getParamVals(params_list,5) ,"delta_params")
plotGraph(s0_counts, "Varying the \"s0\" parameter", getParamVals(params_list,6) ,"s0_params")
#plotGraph([counts_list[0],random_counts])

