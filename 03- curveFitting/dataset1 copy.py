import sys
import numpy as np
import matplotlib.pyplot as plt

def leastsquares(filename):
    f=open(filename,"r")
    x=[]
    y=[]
    
    lines=f.readlines()
    
    #Reading x,y pairs from file
    for line in lines:
        data=line.split()
        x.append(float(data[0]))
        y.append(float(data[1]))
    x,y=np.array(x),np.array(y)

    #Creating M matrix
    M=np.column_stack([x,np.ones(len(x))])

    #Least Squares Linear Regression with constructed M and y
    m,c=np.linalg.lstsq(M, y, rcond=None)[0]
    error=y-(m*x+c)

    #Plot all values of x,y joined by a line
    plt.plot(x,y,color="green",label="Original Data with Noise",lw=0.5)
    
    #Plot errorbar for every 25 points
    plt.errorbar(x[::25],y[::25],np.std(error),marker="s",color="red",markersize=2,ecolor="red",barsabove=False,linestyle="None",label="Errorbar",lw=1)
    
    #Plot the estimated line
    plt.plot(x,m*x+c,color="black",label="Estimated Line")
    print(m,c)
    #Set legend and export the graph
    plt.legend()
    plt.show()
    #plt.savefig('dataset1.png', format='png')

arguments = sys.argv[1:]
leastsquares(arguments[0])