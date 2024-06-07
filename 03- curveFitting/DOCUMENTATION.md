# Assignment 3 - Curve Fitting

## Dataset 1
- It is given that the data contains a straight line with added noise.
- So, ```numpy.linalg.lstsq``` function was used to perform least square regression to find the slope and y-intercept of the given line and find the best fit line for the given data.

### 1. Construction of M Matrix
We are given a number of *observations* $y_1, y_2, \ldots, y_n$ of this function at different x values $x_1, x_2, \ldots, x_n$.  These observations can then be written as:

$$
\mathbf{y} \equiv
\begin{pmatrix}
y_1 \\
y_2 \\
\vdots \\
y_n
\end{pmatrix}
=
\begin{pmatrix}
x_1 & 1 \\
x_2 & 1 \\
\vdots & \vdots \\
x_n & 1
\end{pmatrix}
\begin{pmatrix}
m \\
c
\end{pmatrix}
\equiv
\mathbf{M}\mathbf{p}
$$

In this case the $M$ matrix has each element in the $1^{st}$ column as corresponding values of x and the elements of the $2^{nd}$ column are all 1s. This implies that the equation will be $y_{i} = mx_{i} + c$. 

So, $\mathbf{M}$ is:

$$
\mathbf{M} \equiv
\begin{pmatrix}
x_1 & 1 \\
x_2 & 1 \\
\vdots & \vdots \\
x_n & 1
\end{pmatrix}
$$

$m$ and $c$ are returned by the `numpy.linalg.lstsq` function.

### 2. Plot
The plot of the given noisy data, estimated data and errorbars at every 25th value is given below:

![Plot with Errorbars, Estimated Line: Dataset 1](dataset1.pdf){width=100%}

### 3. Results
The slope was found to be 2.791124245414918 and the y-intercept was found to be 3.8488001014307436

## Dataset 2
- The dataset given was given to be sum of three sine waves of frequencies $f$,$3f$ and $5f$. I estimate the frequency as given in the next sections and find the coefficients of each of the sine waves in the sum.

### 1. Estimation of Time Period
- The code iterates through all the points in the function and clusters the x coordinates of points into groups on the criteria that the distance between that point and a reference value (0 here) is less than 0.5. The first cluster so obtained will be the set of values where 0 is obtained for the first time and the second cluster will be the set of values where 0 is obtained for the second time. 

- The distance between the average value of these clusters is half the period. This is used to derive the fundamental frequency (close to 0.4). Then, the other frequencies are given as $3 \times fundamental$ $frequency$ and $5 \times fundamental$ $frequency$

- This method can work for any sine function, given that the reference point is chosen suitably

### 2. Construction of M Matrix and Setting up Least Square Linear Regression
Let's consider $y$ to be in the form 

$y_{i}(x_{i},f,c_{0},c_{1},c_{2},c_{3})={c_{1}}{sin(2 \pi x_{i} \times f)}+{c_{2}}{sin(2 \pi x_{i} \times 3f)}+{c_{3}}{sin(2 \pi x_{i} \times 5f)}+c_{0}$

Writing in matrix form,

$$
\mathbf{y} \equiv
\begin{pmatrix}
y_1 \\
y_2 \\
\vdots \\
y_n
\end{pmatrix}
=
\begin{pmatrix}
{sin(2 \pi x_{1} \times f)} & {sin(2 \pi x_{1} \times 3f)} & {sin(2 \pi x_{1} \times 5f)} &1 \\
{sin(2 \pi x_{2} \times f)} & {sin(2 \pi x_{2} \times 3f)} & {sin(2 \pi x_{2} \times 5f)} &1 \\
\vdots & \vdots \\
{sin(2 \pi x_{n} \times f)} & {sin(2 \pi x_{n} \times 3f)} & {sin(2 \pi x_{n} \times 5f)} &1 \\
\end{pmatrix}
\begin{pmatrix}
c_{1} \\
c_{2} \\
c_{3} \\
c_{0}
\end{pmatrix}
\equiv
\mathbf{M}\mathbf{c}
$$

So, $\mathbf{M}$ is:

$$
\mathbf{M} \equiv
\begin{pmatrix}
{sin(2 \pi x_{1} \times f)} & {sin(2 \pi x_{1} \times 3f)} & {sin(2 \pi x_{1} \times 5f)} &1 \\
{sin(2 \pi x_{2} \times f)} & {sin(2 \pi x_{2} \times 3f)} & {sin(2 \pi x_{2} \times 5f)} &1 \\
\vdots & \vdots \\
{sin(2 \pi x_{n} \times f)} & {sin(2 \pi x_{n} \times 3f)} & {sin(2 \pi x_{n} \times 5f)} &1 \\
\end{pmatrix}
$$

`numpy.linalg.lstsq` performs linear regression and returns $[c1,c2,c3,c0]$

### 3. Results- scipy.optimize.curve_fit vs numpy.linalg.lstsq
The values of amplitudes of each sin function, the constant and frequcncy are tabulated below (truncated to 6 decimal places):

\begin{table}[h]
\centering
\begin{tabular}{c|c|c}

 & \texttt{curve\_fit} & \texttt{lstsq} \\
\hline
$f$ & 0.399914 & 0.397691 \\
$c_{1}$ & 6.011120 & 6.0077509 \\
$c_{2}$ & 2.001458 & 1.993806 \\
$c_{3}$ & 0.980907 & 0.990135 \\
$c_{0}$ & -0.025875 & -0.025875 \\

\end{tabular}
\end{table}

### 4. Plot
- Plot using linear regression and curve_fit are given below:

![Given Data and Estimate: Dataset 2](dataset2.pdf){width=100%}

## Dataset 3: Part 1
- The radiation is given by the formula
$$B(f, T ) = \frac{2hf^3}{c^2}\frac{1}{e^\frac{hf}{k_{B} T}-1}$$

For this part, the problem statement was to estimate the T at which the data was taken, given the correct values of $h$, $c$ and $k_{B}$

### 1. Approach
- My approach was to define a function with constants $h$, $c$ and $k_{B}$, independent variable $f$ and a parameter $T$ to be determined using the ```curve_fit``` function.

- When I provided no initial guess, the code gave me an overflow error in exponentiation and hence, in multiplication. This is because with no initial guess, the function takes all independent variable values as 1s. 

- So I bruteforced my way through a few values and found that ```curve_fit``` converged for values of $T$ greater than $14$. Despite this, the function gives a Runtime Warning

- The values of the constants used are:
\
$h=6.6260715 \times 10^{-34}$\
$c=3 \times 10^{8}$\
$K_b=1.3806452 \times 10^{-23}$

### 2. Results
- The value of Temperature at which the data was recorded was found to be $4999.11634$ (truncated to 5 decimal places) and the graph looked like the best fit for the data given.

- The function converges and gives the same result till the 5th decimal place for all values of guess till around $430000000$ (found by bruteforce as well)

### 3. Plot
- Plot of the given data and estimated graph are given below:

![Given Data and Estimate: Dataset 3_1](dataset3_1.pdf){width=100%}

## Dataset 3: Part 2

### 1. Approach
- My approach was similar to the previous one, but I defined the function with all $h$, $c$, $k_{B}$ and $T$ as parameters and $f$ as the independent variable. All the parameters were determined using the ```curve_fit``` function.

### 2. Results
- The code returned different values of the parameters for different initial guess values.

- This can be justified by looking at the relation of radiation:
$$B(f, T ) = \frac{2hf^3}{c^2}\frac{1}{e^\frac{hf}{k_{B} T}-1}$$

- This equation can be rewritten as
$$B(f, T ) = \frac{p_{1}f^3}{e^{p_{2}f}-1}$$

Here, 
$p_{1}=\frac{2h}{c^2}$ and $p_{2}=\frac{h}{k_{B}T}$

- The solutions given by the code satisfy the condition that $p_{1}$ and $p_{2}$ are constant. The values of $p_{1}$ and $p_{2}$ obtained are $1.469106 \times 10^{-50}$ and $9.594644 \times 10^{-15}$ respectively.

- The values of the parameters with the initial guess equal to the values obtained in the previous assignment are: (the values are in the order [$h$, $c$, $k_{B}$ and $T$])
\
Initial Guess: [$6.6260715 \times 10^{-34}$,$3 \times 10^{8}$,$K_b=1.3806452 \times 10^{-23}$,$4999.11634$]
\
Values Obtained: [$6.721190 \times 10^{-34}$,$3.024903 \times 10^{8}$,$K_b=1.393455 \times 10^{-23}$,$5027.176563$]

### 3. Plot
- Plot of the given data and estimated graph are given below:

![Given Data and Estimate: Dataset 3_2](dataset3_2.pdf){width=100%}