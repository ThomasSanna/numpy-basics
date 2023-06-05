#Challenge matrix indexes : 
# 1. Create a 3x3 matrix with values ranging from 1 to 9.
# 2. Select the first row of the matrix.
# 3. Select the last column of the matrix.
# 4. Select the first two rows of the matrix.
# 5. Select the first two columns of the matrix.
# 6. Select the middle row of the matrix.
# 7. Select the middle column of the matrix.
# 8. Select the element at the center of the matrix.
# 9. Select the elements from the first two rows and last two columns.
# 10. Select the elements from the first two columns and last two rows.

import numpy as np

print('---------1. Create a 3x3 matrix with values ranging from 1 to 9.---------')
matrix = np.matrix([[1, 2, 3], 
                    [4, 5, 6], 
                    [7, 8, 9]])
print(matrix)

print('----------2. Select the first row of the matrix.---------')
print(matrix[0, :])

print('---------3. Select the last column of the matrix.---------')
print(matrix[:, 2])

print('---------4. Select the first two rows of the matrix.---------')
print(matrix[:2, :])

print('---------5. Select the first two columns of the matrix.---------')
print(matrix[:, :2])

print('---------6. Select the middle row of the matrix.---------')
print(matrix[1, :])

print('---------7. Select the middle column of the matrix.---------')
print(matrix[:, 1])

print('---------8. Select the element at the center of the matrix.---------')
print(matrix[1, 1])

print('---------9. Select the elements from the first two rows and last two columns.---------')
print(matrix[:2, 1:])

print('---------10. Select the elements from the first two columns and last two rows.---------')
print(matrix[1:, :2])