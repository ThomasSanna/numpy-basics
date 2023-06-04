# Problem: Calculate the mean, median, and
# standard deviation of a dataset.

# Data: A NumPy array containing a dataset.

# Task: Use NumPy functions to calculate 
# the mean, median, and standard deviation of the dataset.

# Recommended programming language: Python with NumPy


#For Arrays

import numpy as np

data = np.array([1, 2, 3, 4, 5])

mean = np.mean(data)

median = np.median(data)

std = np.std(data)

print("Mean:", mean)
print("Median:", median)
print("Standard deviation:", std)

# For Matrices

data = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

meanAll = np.mean(data) # all rows
mean0 = np.mean(data[0]) # first row
mean1 = np.mean(data[1]) # second row

median = np.median(data)

std = np.std(data)

print("MeanALL:", meanAll, "\nMean0:", mean0, "\nMean1:", mean1)