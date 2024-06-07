import numpy as np
import matplotlib.pyplot as plt
import csv


def filep(file):
    with open(file) as datasheet:
        x, y = [], []
        for line in datasheet:
            L=line.split()
            x.append(float(L[0]))
            y.append(float(L[1]))
    return (np.array(x),np.array(y))        
def stline(x, m, c):
    return m * x + c        

x,y=filep("a3-data//dataset1.txt")   
M=np.column_stack([x,np.ones(len(x))])      
(m, c), _, _, _ = np.linalg.lstsq(M, y, rcond=None)  
yest = stline(x, m, c)
plt.plot(x, y)
#plt.plot(x,yest)
plt.plot(x,yest, 'b-', label=f'Estimated Line: y = {m:.2f}x + {c:.2f}')
plt.errorbar(x[::25], y[::25],np.std(yest) / np.sqrt(25), fmt='ro')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()