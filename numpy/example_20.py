#!/usr/bin/env python 
#!/usr/bin/en
# -*- coding: utf-8 -*-

"""
    This file is part of aialchemyhub_in
    (https://github.com/satya25/aialchemyhub_in).

    aialchemyhub_in is free software repository:
    You can redistribute it and/or modify it under
    the terms of the MIT License.

    aialchemyhub_in is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    MIT License for more details.

    You should have received a copy of the MIT License along with
    aialchemyhub_in.  If not, see <https://opensource.org/licenses/MIT>.
"""

# ----------------------------------------------------------------------------
# File Name         :       example_20.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 22, 2023
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       numpy
#
# Installation      :       $ pip install --upgrade numpy flake8 autopep8 black pylint mypy pytest
#
# Usage             :       python ./numpy/example_20.py
#
# ---------------------------------------------------------------------------
#
# Credits and Acknowledgements
#
# - Special thanks to the numpy community for their excellent library:
#   https://numpy.org/
#
# - The APIs used in this script is documented here:
#  https://numpy.org/doc/stable/reference/index.html
#
# - Code Snippet(s) adapted from    :   -- NOT Applicable --
#
# - Dataset(s) sourced  from        :   -- NOT Applicable --
#
#
# - Inspiration for Numpy Arrays drawn from:
#   https://numpy.org/doc/stable/reference/arrays.html
#
# Thank you to the creators and maintainers of these resources!
#
# ---------------------------------------------------------------------------
#
# - Content Removal Requests
#
#   If you are the owner or creator of any content used in this script and
#   would like it to be removed, please contact me at:  spnigam25@yahoo.com
#   I will promptly remove the content upon request.
#
# ---------------------------------------------------------------------------
 
'''
    The script performs various matrix operations using NumPy:

    It generates two random matrices, A (3x2) and B (2x3).
    It performs matrix addition with the transpose of matrix B (B.T).
    It demonstrates element-wise matrix addition using broadcasting along axis 2.
    It shows two options for matrix subtraction: one with the transpose of matrix B and another with broadcasting the transpose along axis 1.
    The script highlights NumPy's broadcasting capabilities for efficient matrix operations.
     
    
'''
import numpy as np
import matplotlib.pyplot as plt

def main():

    # Create arrays
    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.arange(6, 11)
    array3 = np.linspace(0, 1, 5)

    # Reshape arrays
    reshaped_array1 = array1.reshape((5, 1))
    reshaped_array2 = np.reshape(array2, (1, 5))

    # Stack arrays
    stacked_vertical = np.vstack((array1, array2))
    stacked_horizontal = np.hstack((array1, array2))

    # Indexing and slicing
    indexed_element = array1[2]
    sliced_array = array2[1:4]

    # Broadcasting
    broadcasted_sum = array1 + 10

    # Element-wise operations
    elementwise_product = np.multiply(array1, array2)
    elementwise_sqrt = np.sqrt(array3)

    # Statistical operations
    mean_value = np.mean(array2)
    std_deviation = np.std(array3)
    min_value = np.min(array1)
    max_value = np.max(array2)

    # Random array generation
    random_integers = np.random.randint(0, 10, size=(3, 3))
    random_uniform = np.random.rand(3, 2)  # Fixing the size to be compatible

    # Linear algebra operations
    dot_product = np.dot(array1, array2)
    matrix_product = np.matmul(random_integers, random_uniform)

    # Statistical functions
    percentile_value = np.percentile(array2, 75)

    # Array comparison
    elementwise_comparison = array1 == array2

    # Advanced indexing
    advanced_indexing_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    indices = np.array([0, 2])
    selected_elements = advanced_indexing_array[:, indices]

    # Concatenation
    concatenated_array = np.concatenate((array1, array2))

    # Array iteration
    for element in array3:
        print(element)

    # Save and load arrays
    np.save('saved_array.npy', array1)
    loaded_array = np.load('saved_array.npy')

    # Display results
    print("Original Arrays:")
    print(array1)
    print(array2)
    print(array3)

    print("\nReshaped Arrays:")
    print(reshaped_array1)
    print(reshaped_array2)

    print("\nStacked Arrays:")
    print(stacked_vertical)
    print(stacked_horizontal)

    print("\nIndexing and Slicing:")
    print(indexed_element)
    print(sliced_array)

    print("\nBroadcasting:")
    print(broadcasted_sum)

    print("\nElement-wise Operations:")
    print(elementwise_product)
    print(elementwise_sqrt)

    print("\nStatistical Operations:")
    print("Mean:", mean_value)
    print("Standard Deviation:", std_deviation)
    print("Min:", min_value)
    print("Max:", max_value)

    print("\nRandom Array Generation:")
    print(random_integers)
    print(random_uniform)

    print("\nLinear Algebra Operations:")
    print("Dot Product:", dot_product)
    print("Matrix Product:")
    print(matrix_product)

    print("\nStatistical Functions:")
    print("75th Percentile:", percentile_value)

    print("\nArray Comparison:")
    print(elementwise_comparison)

    print("\nAdvanced Indexing:")
    print(selected_elements)

    print("\nConcatenation:")
    print(concatenated_array)

    print("\nArray Iteration:")
    # Iterating through array3
    for element in array3:
        print(element)

    print("\nSave and Load Arrays:")
    print("Saved Array:", array1)
    print("Loaded Array:", loaded_array)

    #################


    # Visualizations
    plt.figure(figsize=(12, 8))

    # Histogram of array1
    plt.subplot(2, 3, 1)
    plt.hist(array1, bins=5, edgecolor="k", alpha=0.7)
    plt.title("Histogram of Array 1")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.grid(True)

    # Scatter plot of array2 vs array1
    plt.subplot(2, 3, 2)
    plt.scatter(array1, array2, color='blue', marker='o')
    plt.title("Scatter Plot of Array 2 vs Array 1")
    plt.xlabel("Array 1")
    plt.ylabel("Array 2")
    plt.grid(True)

    # Box plot of array3
    plt.subplot(2, 3, 3)
    plt.boxplot(array3)
    plt.title("Box Plot of Array 3")
    plt.xlabel("Array 3")
    plt.grid(True)

    # Heatmap of random_integers
    plt.subplot(2, 3, 4)
    plt.imshow(random_integers, cmap='viridis', interpolation='nearest')
    plt.title("Heatmap of Random Integers")
    plt.colorbar(label="Values")

    # Line plot of elementwise_product
    plt.subplot(2, 3, 5)
    plt.plot(elementwise_product, label="Elementwise Product", color='green')
    plt.title("Line Plot of Elementwise Product")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.legend()

    # Show all plots
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

