def matmul(A, B):
    """
        Multiplies two matrices A and B
    
        This function gives the result of matrix multiplication of two matrices A 
    and B. It multiplies matrices A (of dimension M x N) and matrix B (of dimension N x K)
    and returns the matrix multiplication product (of dimensions M x K)
    
    Arguments:
        A: Matrix of order M X N
        B: Matrix of order N X K
    
    Returns:
        Product Matrix as a list of lists

    NOTE:
        In Check 4, the program checks for the attribute '__float__' 
        as it is usually exclusive to numerical values

    """

    matrices=[A,B]

    #CHECK 1: Checks if A and B are not of the correct data types (if A and B are not iterables or are strings)
    for i in matrices:
        if not hasattr(i,'__iter__') or type(i)==str:
            raise TypeError("A and B are not of the correct type")
    
    #CHECK 2: Check if elements of A and B are of the correct datatypes:
    for matrix in matrices:
        if len(matrix)!=0:
            for row in matrix:
                if not(hasattr(row,'__iter__')) or type(row)==str:
                    raise TypeError("Elements of A and B are not of the correct type")
                
    #Order of A is M X N and Order of B is N X K
    M=len(A)
    N=len(A[0])
    K=len(B[0])
    
    #CHECK 3: Checks if A and B are of correct dimensions
    if(N!=len(B)):
        raise ValueError("A and B are not of Correct Dimensions")

    result_matrix=[]
    
    # Iterates through each row in A
    for i in range(M):

        #Creating i_th row of result matrix
        result_matrix.append([]) 

        #For Each Column in B, multiply the corresponding elements and find sum, ie, multiply i_th row of A with j_th row of B
        #This loop goes through each column of B
        for j in range(K):

            sum=0
            
            #Goes through each element of the j_th row and multiplies it with the corresponding element in i_th row of A
            for k in range(N):
                
                try:

                    #CHECK 4: Check if values are numeric- '__float__' attribute is usually used for numeric datatypes
                    if not( hasattr(A[i][k],'__float__') or hasattr(B[k][j],'__float__')):
                        raise TypeError("Elements of A and B should be numerical")

                    else:
                        sum+=A[i][k]*B[k][j]
                
                #CHECK 5: Raise ValueError if the length of any rows is wrong
                except IndexError:
                    raise TypeError("Row of A and B should be of correct lengths")

            #Adding j_th entry in the i_th row of result matrix
            result_matrix[i].append(sum) 
        
    return result_matrix