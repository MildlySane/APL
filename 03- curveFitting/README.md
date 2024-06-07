# Least Squares Linear Regression and Curve_Fit

## Working
- Least Squares Linear Regression is a method used to find the best fit for data that is a linear function in nature. It works by finding the coefficients of the linear terms so as to minimise the value of sum of squared difference between the linear function obtained and the values of $y_{i} given. This is done in this code by using the ```numpy.linalg.lstsq``` function.

- curve_fit is a function in ```scipy.optimize``` that calculates the parameters of a function, given the independent variable and the value of the function outputs at corresponding points.

- Both ```lstsq``` and ```curve_fit``` are used in this solution to solve each of the set of questions

## How to Run
### 1. dataset1.py
- Run the program with

```
python3 dataset1.py
```

- The current working directory must have dataset in a ```.txt``` file named ```dataset1.txt``` for the function to work. It takes the set of x and y pairs given in the text file, performs least squares linear regression and shows the plot of estimated line, given data and errorbars in every 25 observations. The program shows the plot and saves the plot in the same directory as ```dataset1.png```

- The program prints the value of slope and y-intercept of the graph as well

### 2. dataset2.py
- Run the program with

```
python3 dataset2.py
```

- The current working directory must have the dataset in a ```.txt``` file named ```dataset2.txt``` for the function to work. It takes the set of x and y pairs given in the text file, performs linear regression as well as curve_fit, and shows the plot of estimated graphs and given data. The program shows the plot and saves the plot in the same directory as ```dataset2.png```. 
- The code also prints the values of the coefficients of each of the sin functions as well as the constant in the linear combination obtained in both methods
- The code assumes the data to be the sum of 3 sin functions and that their frequencies are in the ratio $1:3:5$

### 3. dataset3_1.py
- Run the program with

```
python3 dataset3_1.py
```

- The current working directory must have the dataset in a ```.txt``` file named ```dataset3.txt``` for the function to work. It takes the set of x and y pairs given in the text file, uses curve_fit, and shows the plot of estimated graphs and given dataThe program shows the plot and saves the plot in the same directory as ```dataset3_1.png```. The code assumes the data to be obeying the equation for blackbody radiation.

- The program prints the value of the Temperature at which the data is obtained in the console

### 3. dataset3_1.py
- Run the program with

```
python3 dataset3_1.py
```

- The current working directory must have the dataset in a ```.txt``` file named ```dataset3.txt``` for the function to work. It takes the set of x and y pairs given in the text file, uses curve_fit, and shows the plot of estimated graphs and given data. The program shows the plot and saves the plot in the same directory as ```dataset3_2.png```. The code assumes the data to be obeying the equation for blackbody radiation.

- The program prints the value of the Temperature at which the data is obtained in the console
