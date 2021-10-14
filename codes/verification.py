import time
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shlex
from scipy.optimize import curve_fit
import ctypes
  
# libfun loaded to the python file
# using fun.myFunction(),
# C function can be accessed
# but type of argument is the problem.
                        
fun = ctypes.CDLL("libfun.so")
fun.recursive.argtypes = [ctypes.c_int]

# define the true objective function
def objective(x, a, b):
	return a * x + b

Time_arr = []
for i in range(0,1005,5):
    start = time.time()
    fun.recursive(i)
    end = time.time()
    Time_arr.append((end-start)/1e-6)
x = np.array(range(0,1005,5))
y = np.array(Time_arr)
popt, _ = curve_fit(objective, x, y)
a, b = popt
eqn = "T(n) = {:.6f}*n {:.6f}".format(a,b)
x_line = np.array(range(1000))
y_line = objective(x_line, a, b)
plt.plot(x, y,c = "red", label = "Execution Time")
plt.plot(x_line, y_line, ls='--',lw=1.5, label = "Linear Fit", c = "black")
plt.title("Verification of complexity")
plt.text(550, 1, eqn)
plt.xlabel("n")
plt.ylabel("Time ($\mu$s)")
plt.legend()
plt.grid()
plt.savefig("plot.eps")
plt.show()

#if using termux
#plt.savefig('./figs/ee18btech11001/ee18btech11001_1.pdf')
#plt.savefig('./figs/ee18btech11001/ee18btech11001_1.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11001/ee18btech11001_1.pdf"))
#end if
