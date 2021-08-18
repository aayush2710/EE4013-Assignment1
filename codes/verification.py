import time
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shlex

def recursive(n):
    if(n==0):
        return
    Sum = 0
    for i in range(7*n):
        Sum+=i
    recursive(int(n//2))
    recursive(int(2*n/5))

Time_arr = []
for i in range(1000):
    start = time.time()
    recursive(i)
    end = time.time()
    Time_arr.append(end-start)

plt.plot(np.array(range(1000)), np.array(Time_arr))
plt.title("Verification of complexity")
plt.xlabel("n")
plt.ylabel("time")
plt.savefig("plot.eps")
plt.show()

#if using termux
#plt.savefig('./figs/ee18btech11001/ee18btech11001_1.pdf')
#plt.savefig('./figs/ee18btech11001/ee18btech11001_1.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11001/ee18btech11001_1.pdf"))
#end if
