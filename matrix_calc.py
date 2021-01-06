# A matrix Calculator
import numpy as np
# from tkinter import *

#####################################################################################################
#####################################################################################################
# 
# 
# First define the two matrices um on front and then you can run the programm
# the result will be shown in the command terminal
#
#
#####################################################################################################
#####################################################################################################

# Define first Matrix:

first = np.array((
    [0,0,0],
    [0,0,0]
))

# Define second Matrix:

second = np.array((
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
))

# Little Example:
first = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

second = np.array([
    [4],
    [5],
    [6]
])




def matrix_multiplication(a,b):

    if not np.shape(a)[1] == np.shape(b)[0]:
        raise ValueError(f"Dimensions are wrong: a-columns: {np.shape(a)[1]} != b-rows: {np.shape(b)[0]}")
    
    rows = np.shape(a)[1]
    columns = np.shape(b)[1]

    result = np.zeros((rows,columns))

    for i in range(rows):
        for j in range(columns): # für den durchlauf der spalten in Vektor b
            result[i,j] = np.sum( a[i,:] * b[:,j]  )
    
    return result







res = matrix_multiplication(b,c)
print(res)