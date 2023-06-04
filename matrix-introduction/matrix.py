# COURSE : BASICS OF NUMPY. by WadeeKT.

# Importing numpy library.
import numpy as np

# Creating a matrix.
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Printing the matrix.
print('Matrix: \n', matrix)

# Printing the shape of the matrix.
print('Shape of the matrix: ', matrix.shape)

# Printing the size of the matrix.
print('Size of the matrix: ', matrix.size)

# Creating a new matrix with random values.
random_matrix = np.random.rand(3, 3)

# Printing the new matrix.
print('Random matrix: \n', random_matrix)

# Finding the maximum and minimum values in the matrix.
max_value = np.max(matrix)
min_value = np.min(matrix)

# Printing the maximum and minimum values.
print('Maximum value in the matrix: ', max_value)
print('Minimum value in the matrix: ', min_value)

# Creating two matrices.
matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Performing element-wise addition and subtraction of two matrices.
addition = matrix1 + matrix2
subtraction = matrix1 - matrix2

# Printing the result of element-wise addition and subtraction.
print('Element-wise addition of two matrices: \n', addition)
print('Element-wise subtraction of two matrices: \n', subtraction)