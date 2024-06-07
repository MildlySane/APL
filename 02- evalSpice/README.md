# SPICE simulation in Python
This python script ```evalSpice.py``` implements a circuit solver that parses and solves for all nodal voltages and voltage source currents described in a SPICE Netlist

## Inputs
Input is a SPICE Netlist (Filename with appropriate path of the netlist describing the circuit)

## Outputs
The script returns two dictionaries:

1. `Node_V`: Voltages at all Nodes in the circuit, with key as node name and value as Voltages at nodes
2. `Vs_Current`: Currents through each voltage node, with key as name of voltage souce and value as Current through the voltage source

## Modules Defined
The script uses four functions:

1. `evalSpice`: Main function that calls the other functions
2. `file_parse`: Parses data from the file given
3. `create_eqns`: Creates equations for the variables
4. `equation_solve`: Solves the system of linear equations and formats them in the term of required outputs


## Approach
Let the number of Nodes and Voltage Sources be $N$ and $K$ respectively. The script uses modified nodal analysis to create the equation matrices [(given here)](https://en.wikipedia.org/wiki/Modified_nodal_analysis).

The first $N$ equations correspond to the [KCL](https://en.wikipedia.org/wiki/Kirchhoff%27s_circuit_laws#Kirchhoff's_current_law) at each node. The next $K$ equations correspond to the Voltage Characteristics of each Voltage source.

So the coefficient matrix has dimensions $(N+K)\times(N+K)$, and the solution matrix and RHS Matrix have dimension $(N+K)\times 1$

The script uses the [numpy](https://numpy.org/) module. It Uses [`numpy arrays`](https://numpy.org/doc/stable/reference/generated/numpy.array.html) to store the equation matrices and [`numpy.linalg.solve`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html) to solve the system of linear equations

### 1. Parsing Data
The code initially parses the data in SPICE netlist and checks for errors. Then, these values are used to create the equation matrices

### 2. Generating Equation Matrices
1. The program iterates through each Voltage Source and adds the corresponding Voltage equations ($V_{node1}-V_{node2}=V_s$) as well as contribution of source current in the equation matrix (The $I_s$ term in the voltage equations)

2. The program iterates through each Current Source and adds the contribution of each current source in the KCL of each node

3. The program iterates through each Resistor and does the following:
    1. Adds $\frac{1}{R}$ to coefficient of Node 1 in equation 1
    2. Adds $\frac{-1}{R}$ to coefficient of Node 2 in equation 2
    3. Does the same for Node 2 as well

### 3. Solving Equations
The program uses `numpy.linalg.solve` in the module `numpy` to solve the linear equations

## All Error and Special Cases Handled:
1. The code raises a `ValueError`
 for the following, with appropriate error messages:
    - Elements other than Voltage and Current Sources, Resistances given
    - `.end` or `.circuit` is absent in the netlist
    - Circuit is unsolvable
    - The LHS matrix of the matrix equation is singular
    - Incorrect Configuration of Current and/or Voltage Sources
    - Non-DC sources given as input
    - Same element name repeats in the circuit file
    - A negative resistance

2. It raises `FileNotFoundError` if Invalid filename supplied

3. For Zero Resistance, the code approximates to a small value of resistance ($10^{-10}$) and solves the circuit

## Limitations

Since the code uses approximations for 0 Resistance, the values have small errors in the solution obtained