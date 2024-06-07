import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#Returns the value of Blackbody radiation
def radiation(f,h,c,K_b,T):
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

#Initial guess for h,c,Kb,T
guess=(6.6260715e-34,3e8,1.3806452e-23,4999)
(h,c,K_b,T),_=curve_fit(radiation,x,y,guess)

print(2*h/c**2,h/(K_b*T))

#Display the values of variables and plot the graph
print(h,c,K_b,T)
plt.plot(x,y,color="green",label="Original Data with Noise",lw=0.6)
plt.plot(x,radiation(x,h,c,K_b,T),color="black",lw=0.7,label="Estimated Plot")
plt.savefig("dataset3_2.png",format="png")
plt.savefig("dataset3_2.pdf",format="pdf")