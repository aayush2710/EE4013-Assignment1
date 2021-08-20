import time
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shlex
from scipy.optimize import curve_fit

# define the true objective function
def objective(x, a, b):
	return a * x + b
 
# load the dataset

def recursive(n):
    if(n==0):
        return
    Sum = 0
    for i in range(7*n):
        Sum+=i
    recursive(int(n//2))
    recursive(int(2*n/5))

Time_arr = []
for i in range(0,1005,5):
    start = time.time()
    recursive(i)
    end = time.time()
    Time_arr.append(end-start)
x = np.array(range(0,1005,5))
y = np.array(Time_arr)
popt, _ = curve_fit(objective, x, y)
a, b = popt
x_line = np.array(range(1000))
y_line = objective(x_line, a, b)
plt.plot(x, y,c = "red", label = "Execution Time")
plt.plot(x_line, y_line, ls='--',lw=1.5, label = "Linear Fit", c = "black")
plt.title("Verification of complexity")
plt.xlabel("n")
plt.ylabel("time")
plt.legend()
plt.grid()
plt.savefig("plot.eps")
plt.show()

#if using termux
#plt.savefig('./figs/ee18btech11001/ee18btech11001_1.pdf')
#plt.savefig('./figs/ee18btech11001/ee18btech11001_1.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11001/ee18btech11001_1.pdf"))
#end if
