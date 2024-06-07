import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

########################################################################################
def f1(x):
    return x ** 2 + 3 * x + 8

def df1_dx(x):
    return 2*x+3
########################################################################################

xlim3 =  [-10, 10]
ylim3 =  [-10, 10]
def f3(x, y):
    return x**4 - 16*x**3 + 96*x**2 - 256*x + y**2 - 4*y + 262

def df3_dx(x, y):
    return 4*x**3 - 48*x**2 + 192*x - 256

def df3_dy(x, y):
    return 2*y - 4

########################################################################################
xlim4 = [-np.pi, np.pi]
def f4(x,y):
    return np.exp(-(x - y)**2) * np.sin(y)

def df4_dx(x, y):
    return -2 * np.exp(-(x - y)**2) * np.sin(y) * (x - y)

def df4_dy(x, y):
    return np.exp(-(x - y)**2) * np.cos(y) + 2 * np.exp(-(x - y)**2) * np.sin(y)*(x - y)

########################################################################################
xlim5= [0,2*np.pi]
def f5(x):
    return np.cos(x)**4 - np.sin(x)**3 - 4*np.sin(x)**2 + np.cos(x) + 1

def df5_dx(x):
    return -4*np.sin(x)*(np.cos(x)**3)- 3*(np.sin(x)**2)*np.cos(x)- 8*np.sin(x)*np.cos(x)-np.sin(x)
########################################################################################

#One Dimensional Gradient Descent
def oneDim(f,d_dx,lim,filename="Animation.png"):

    xbase=np.linspace(lim[0],lim[1],200)
    ybase=f(xbase)
    
    #Initial Guess
    bestx = 3
    bestcost = f(bestx)

    #Setting up plots
    fig, ax = plt.subplots()
    ax.plot(xbase, ybase)
    xall, yall = [], []
    lnall,  = ax.plot([], [], 'ro', markersize=4)
    lngood, = ax.plot([], [], 'go', markersize=7)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # Learning rate 
    lr = 0.15

    # Move in the x direction by d_dx * lr
    def onestepderiv(frame):
        nonlocal bestx, lr

        xall.append(bestx)
        yall.append(f(bestx))

        x = bestx - d_dx(bestx) * lr 
        bestx = x
        y = f(x)
        
        lngood.set_data(x, y)
        lnall.set_data(xall, yall)
        if frame==34:
            print(f"Best x:{x}", f"Best y:{y}")

    # Iterate 35 times and display animation
    ani= FuncAnimation(fig, onestepderiv, frames=range(35), interval=500, repeat=False)
    ani.save(filename, writer='pillow', dpi=100)
    plt.show()
    

#Two Dimensional Gradient Descent
def twoDim(f, d_dx, d_dy, lim_x,lim_y,bestx=0,besty=0,lr=0.4,filename="Animation.png"):
    
    #Setting up figure and initial plot of f
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    X = np.arange(lim_x[0], lim_x[1], 0.25)
    Y = np.arange(lim_y[0], lim_y[1], 0.25)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)
    surf = ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.8)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    #Points that the code finds during gradient descent
    xall, yall, zall = [], [], []
    lnall, = ax.plot([], [], [], 'ro', markersize=4)
    lngood, = ax.plot([], [], [], 'go', markersize=7)

    bestcost = f(bestx, besty)

    # Change x and y by deriv*lr
    def onestepderiv(frame):
        nonlocal bestx, besty, bestcost

        #Points that have been visited
        xall.append(bestx)
        yall.append(besty)
        zall.append(f(bestx, besty))

        # Calculate the new x and y values
        new_x = bestx - d_dx(bestx, besty) * lr
        new_y = besty - d_dy(bestx, besty) * lr

        # Calculate the new cost
        new_cost = f(new_x, new_y)

        # Update if the new cost is better
        if new_cost < bestcost:
            bestx = new_x
            besty = new_y
            bestcost = new_cost

        # Display the values on graph
        lngood.set_data([bestx], [besty])
        lngood.set_3d_properties([bestcost])
        lnall.set_data(xall, yall)
        lnall.set_3d_properties(zall)
        if frame==59:
            print(f"Best x:{bestx}", f"Best y:{besty}", f"Best z: {f(bestx,besty)}")

    # Animate 60 iterations
    ani = FuncAnimation(fig, onestepderiv, frames=range(60), interval=10, repeat=False)
    ani.save(filename, writer='pillow', dpi=100)
    plt.show()


oneDim(f1,df1_dx,[-5,5],filename="Q1.png")
oneDim(f5,df5_dx,xlim5,filename="Q4.png")

twoDim(f3,df3_dx,df3_dy,xlim3,ylim3,2,0,lr=0.1,filename="Q2.png")
twoDim(f4,df4_dx,df4_dy,xlim4,xlim4,filename="Q3.png")