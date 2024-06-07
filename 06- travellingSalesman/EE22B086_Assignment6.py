import numpy as np
import matplotlib.pyplot as plt
import sys

#Distance in the path
def distance(cities, cityorder):
    totaldistance = 0
    for i in range(1, len(cityorder)):
        totaldistance += np.sqrt((cities[cityorder[i]][0] - cities[cityorder[i - 1]][0]) ** 2 + (cities[cityorder[i]][1] - cities[cityorder[i - 1]][1]) ** 2)
    #Distance previously calculated + the distance between last and first node
    return totaldistance+np.sqrt((cities[cityorder[-1]][0] - cities[cityorder[0]][0]) ** 2 + (cities[cityorder[-1]][1] - cities[cityorder[0]][1]) ** 2)

def tsp(cities):
    
    cities = np.array(cities)
    N = len(cities)
    
    #Number of Iterations
    num_iter=50000

    # Initial temperature and Decay Rate
    T = 1000
    decayrate = 0.99
    
    # Generate an initial random order
    cityorder = np.arange(N)
    np.random.shuffle(cityorder)

    #Initial Guess, Initial Value
    initialdist=distance(cities,cityorder)
    bestcost=initialdist

    fig, ax = plt.subplots()

    #Function to Shuffle Order in each Iteration by Simulated Annealing
    for iter in range(num_iter):

        #Pick two vertices in random and swap order
        swap = np.random.choice(N, 2, replace=False)
        cityorder[swap[0]], cityorder[swap[1]] = cityorder[swap[1]], cityorder[swap[0]]

        dist = distance(cities, cityorder)

        # The new cityorder has already been updated if the following condition happens
        if dist < bestcost:
            bestcost = dist

        # Check if the random probability is less than the e^(-dE)/T term to choose value
        else:
            toss = np.random.random_sample()
            if toss < np.exp(-(dist - bestcost) / T):
                bestcost = dist
            else:
                # Revert the swap
                cityorder[swap[0]], cityorder[swap[1]] = cityorder[swap[1]], cityorder[swap[0]]

        T = T * decayrate

        print(f"Progress:{int(iter*100.0/(num_iter-1))} %",end="\r") 
    
    # Plot values, display and save
    ax.clear()
    xplot = cities[cityorder][:, 0]
    yplot = cities[cityorder][:, 1]
    xplot = np.append(xplot, xplot[0])
    yplot = np.append(yplot, yplot[0])
    plt.plot(xplot, yplot, marker='o')
    plt.show()
    plt.savefig("Sim_Annealing.jpg")
    
    #Print stats on terminal
    print("Initial Guess:", initialdist)
    print("Best Distance:",bestcost)
    print("\nImprovement=",abs(bestcost-initialdist)*100/initialdist)
    return cityorder

#Read Values from the file given as argument
cities=[]
args=sys.argv[1:]
with open(args[0],"r") as f:
    N=int(f.readline().strip())
    
    for i in range(N):
        line=f.readline()
        data=line.split()
        cities.append([float(data[0]),float(data[1])])

#Calling tsp with the given data, displaying the best route and distance
result = tsp(cities)
print(result)
