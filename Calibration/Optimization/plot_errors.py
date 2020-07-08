import csv, time
import matplotlib.pyplot as plt


timestr = time.strftime("%Y%m%d_%H%M%S")
def plotError():
    errors = []
    params = []
    with open("data/error.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for lines in csv_reader:
          errors.append(float(lines[0]))
          params.append(str(lines[1]))
    errors = errors[::2]  #every other term
    plt.plot([i+1 for i in range(len(errors))], errors)
    num = 2*(len(errors)) -  1
    plt.ylabel("Error")
    plt.xlabel("Iteration")
    plt.title("Initial [v0, T]: " + str(params[0]) + " Final [v0,T]: " + str(params[-1])+"\n Iterations: " + str(num))
    plt.savefig("figures/error_latest_"+timestr+".png")
   # plt.show()

plotError()
