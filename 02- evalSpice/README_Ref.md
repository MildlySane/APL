# SPICE simulation in Python
This program has been made to solve circuits given in a certain(spice) format.

## Approach
I am first making the matrix and then using "gausselim" function to solve this.
I am making the matrix row wise == nodal analysis at each node.So for, say, n nodes, we will have n nodal equations and n2 equations for the Vsources.

## Functions:
###  eval_spice:
This function opens the input file, if valid, and converts the list to a standardized list for further functions to work.
Further this is also the main function which calls all the other functions and produces the final result matrix.

###  nodal_anal:
This function is a major function for the logic implemented. It takes in the 
standardized input file and outputs an equation for the specified node.

###  v_equation:
This function completes the matrix and adds the voltage source equations.

###  b_out:
This function gives the constants matrix

###  gauss_elim:
This function solves the matrix and gives errors in case of invalid matrix.

###  unknown_counter:
This function basically counts the number of unique nodes.

## Errors resolved(given):

- FileNotFoundError(Wrong file name)
- No Solution - This error rises when the matrix sent to gauss_elim is singular, which means the ciruit has no solution.
- If .circuit or .end not found in file(Malformed Error)
- If any circuit element except R,V,I is given then it gives an invalid element error.


## Errors resolved(extra):

- If negative resistor is given then a "malformed circuit" error is raised.
- If resistance = 0 then I have taken 1/R to be 10^10 so that the other resistances are not ignored
-