import numpy as np
from scipy.optimize import curve_fit

#Linear Estimate
def linear(params, c0, c1, c2, c3, c4, c5, c6, c7):
    return c0*params[0]+c1*params[1]+c2*params[2]+c3*params[3]+c4*params[4]+c5*params[5]+c6*params[6]+c7

#Non-Linear Estimate
def power(data, c0, c1, c2, c3, c4, c5, c6, c7, p0, p1, p2, p3, p4, p5):
    return c0 * data[0]**p0 + c1 * data[1]**p1 + c2 *data[2]**p2 + c3*data[3]**p3 + c4*data[4]**p4 + c5 * data[5]**p5+ c6*data[6]+c7

# Maximum values of the parameter values to normalise
maxval=[340,120,5,5,5,10,1]

#Reading the values of parameters and function values
param =np.transpose(np.loadtxt("Admission_Predict_Ver1.1.csv",skiprows=1,delimiter=",", dtype=float,usecols=(1,2,3,4,5,6,7)))
y = np.loadtxt("Admission_Predict_Ver1.1.csv",skiprows=1,delimiter=",", dtype=float,usecols=(8))
param[param==0]=-1

for i in range(len(param)):
    param[i]=param[i]/maxval[i]
#Linear Fit
c=curve_fit(linear,param,y)[0]
yest=linear(param, c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7])
print(np.mean(abs(y-yest)/y))
print(c,end="\n\n")

#Nonlinear Fit
res = curve_fit(power, param, y,method="trf",maxfev=10000)[0]
y_est = power(param, res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8], res[9], res[10], res[11], res[12], res[13])
print(np.mean(abs(y-y_est)/y))
print(res[:8],end="\n\n")
print(res[8:])