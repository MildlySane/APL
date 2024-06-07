import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#Define Constants
h,c,K_b=6.6260715e-34,3e8,1.3806452e-23

#Returns the value of Blackbody radiation
def radiation(f,T):
    return 2*h*f**3/(c**2*(np.exp(h*f/(K_b*T))-1))

f=open("dataset3.txt","r")
x=[]
y=[]

lines=f.readlines()

#Reading x,y pairs from file
for line in lines:
    data=line.split()
    x.append(float(data[0]))
    y.append(float(data[1]))
x,y=np.array(x),np.array(y)

#Initial Guess for curve_fit and solving for T
guess=(430000000) #From 145, does not give overflow
(T),_=curve_fit(radiation,x,y,guess)

#Plot the graph after curve fitting
print(T)
plt.plot(x,y,color="green",label="Original Data with Noise",lw=0.6)
plt.plot(x,radiation(x,T),color="black",lw=0.7,label="Estimated Plot")
plt.savefig("dataset3_1.pdf",format="pdf")