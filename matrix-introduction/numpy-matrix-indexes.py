#Tutorial Matrix Indexes

import numpy as np

# Creating a matrix.
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6],  # [vertical index, horizontal index]
                   [7, 8, 9]])

# Printing the matrix.
print('Matrix: \n', matrix)

# Printing the element at the first row and first column.
print('Element at the first row and first column: ', matrix[0, 0]) # 1

# Printing the element at the second row and third column.
print('Element at the second row and third column: ', matrix[1, 2]) # 6


# With negative indexes, we can access the elements from the end.
# Printing the element at the third row and third column.
print('Element at the third row and third column: ', matrix[-1, -1]) # 9

# Printing the element at the second last row and second last column.
print('Element at the second last row and second last column: ', matrix[-2, -2]) # 5


#With slicing, we can access a range of elements.
# Printing all the elements.
print('All the elements: \n', matrix[:, :]) # [[1 2 3] [4 5 6] [7 8 9]] (can be matrix[:] or matrix[:3, :3] or matrix[0:3, 0:3])

# Printing the elements from the second row.
print('Elements from the second row: \n', matrix[1, :]) # [4 5 6]

# Printing the elements up to the second row.
print('Elements up to the second row: \n', matrix[:2, :]) # [[1 2 3] [4 5 6]]

# Printing the elements from the second column.
print('Elements from the second column: \n', matrix[:, 1]) # [2 5 8]

# Printing the elements up to the second column.
print('Elements up to the second column: \n', matrix[:, :2]) # [[1 2] [4 5] [7 8]]