import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Finds Time Period
def Timeperiod(X,Y,ref_point):
    l=[[],[],[]]
    count=0

    #Goes through each (X,Y)
    for i in range(len(X)):
        
        #Puts groups of X_i around ref_point such that ||Y_i-ref_point||<0.5
        #l[0] is the first cluster of X with Y around 0 and l[1] is the second
        try:
            if abs(Y[i]-ref_point)<0.5:
                c=abs(X[i]-l[count][-1])
                if c>0.05:
                    count+=1  
                l[count].append(X[i])
        except IndexError:
            l[count].append(X[i])
        
        #Distance between two Xs with same Y value is Period/2
        if count==2:
            return 2*(np.mean(l[1])-np.mean(l[0]))


#Sin Function for Least Squares Interpolation
def sin_lstsq(x,fund_freq):
    return [np.sin(p*x*1*fund_freq),np.sin(p*x*3*fund_freq),np.sin(p*x*5*fund_freq),np.ones(len(x))]

#Sin function for curve_fit
def sinfunc(x,f,c1,c2,c3,c0):
    return c1*np.sin(p*f*x)+c2*np.sin(3*p*x*f)+c3*np.sin(5*p*x*f)+c0

with open("dataset2.txt","r") as file1:
    p=2*np.pi

    x=[]
    y=[]
    
    #Reading x,y pairs from file
    lines=file1.readlines()
    for line in lines:
        data=line.split()
        x.append(float(data[0]))
        y.append(float(data[1]))
    x,y=np.array(x),np.array(y)
    
    #Finding Fundamental Frequency using Timeperiod
    fund_freq=1/Timeperiod(x,y,0)

    #Creating M matrix
    M=np.column_stack(sin_lstsq(x,fund_freq))

    #Least Squares Linear Regression with constructed M and y
    coeffs=np.linalg.lstsq(M, y, rcond=None)[0]
    
    #Curve_fit to find coefficients
    guess=(0.4,1,1,1,1)
    (f,c1,c2,c3,c0),_ = curve_fit(sinfunc, x, y,guess)

    #Print Values for Checking
    print(fund_freq,coeffs)
    print(f,c1,c2,c3,c0)
    
    #Plot all values of x,y
    plt.plot(x,y,color="green",label="Original Data with Noise",lw=0.6)
    
    #Plot Graphs obtained by curve_fit and least squares linear regression
    plt.plot(x,np.dot(coeffs,sin_lstsq(x,fund_freq)),color="red",lw=0.7,label="Estimated using lstsq") #Least Squares
    plt.plot(x,sinfunc(x,f,c1,c2,c3,c0),color="black",lw=0.7,label="Estimated using curve_fit") #curve_fit
    
    #Set legend and display graph
    plt.legend()
    plt.savefig("dataset2.pdf",format="pdf")