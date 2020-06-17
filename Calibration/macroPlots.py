import glob
import os, csv
import matplotlib.pyplot as plt

files1 = glob.glob("data/exp1_res/*csv")
files1.sort(key=os.path.getmtime)

counts_list = []
avg_counts_list = []


for file in files1:
    with open(file, 'r') as csvfile:
        content = csv.reader(csvfile)
        for line in content:
            line = list(map(int, line))
            counts_list.append(line)
            avg_counts_list.append(sum(line)/len(line))

def plotGraph(yvals):
    for y in yvals:
        plt.plot([30*i for i in range(len(y))],y)
#    plt.savefig("pic.png")
    plt.show()

plotGraph(counts_list)
