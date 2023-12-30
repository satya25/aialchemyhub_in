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
# File Name         :       example_16.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 22, 2023
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       numpy
#
# Installation      :       $ pip install --upgrade numpy flake8 autopep8 black pylint mypy pytest
#
# Usage             :       python ./numpy/example_16.py
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

    # 1. Create matrices
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 3x3 matrix (originally singular)
    B = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # Identity matrix

    # 2. Modify A to make it non-singular (optional)
    # Uncomment the following line to slightly change A and make it non-singular
    # A = np.array([[1, 2, 3], [4, 5, 6.1], [7, 8, 9]])

    # 3. Handle singularity and perform operations
    try:
        C = A @ B  # Matrix multiplication
        D = A.T  # Matrix transpose
        A_inverse = np.linalg.inv(A)  # Use separate variable for inverse (if successful)
        det_A = np.linalg.det(A)  # Store determinant before potential exception
        print("Matrix A is non-singular. All operations successful.")
    except np.linalg.LinAlgError:
        print("Matrix A is singular. Some operations may not be available.")
        A_inverse = None
        det_A = None  # Define det_A here to handle the case of singularity


    # 4. Operations based on singularity check
    if A_inverse is not None:
      # Use A_inverse for operations requiring a non-singular matrix
      x = np.linalg.solve(A_inverse, B)  # Solve Ax = B for x
      print("Solution to Ax = B (x):")
      print(x)
    else:
      # Perform operations applicable even for singular matrices
      eigenvalues, eigenvectors = np.linalg.eig(A)  # Calculate eigenvalues and eigenvectors
      U, S, Vh = np.linalg.svd(A)  # Decompose A into U, S, Vh

    # 5. Printing results
    print("Matrix A:")
    print(A)
    print("Matrix C (A @ B):")
    print(C) if C is not None else None
    print("Matrix D (A transpose):")
    print(D)
    print("Matrix A inverse:")
    print(A_inverse) if A_inverse is not None else None
    print("Matrix F (A determinant):")
    print(det_A) if det_A is not None else None  # Print determinant only if calculated
     
    # (Optional) Visualization of matrices, eigenvalues, etc.
    if A_inverse is not None:
        # Visualization of A and A_inverse
        plt.figure(figsize=(12, 6))

        plt.subplot(1, 2, 1)
        plt.imshow(A, cmap='viridis')
        plt.title("Matrix A")
        plt.colorbar()

        plt.subplot(1, 2, 2)
        plt.imshow(A_inverse, cmap='viridis')
        plt.title("Matrix A Inverse")
        plt.colorbar()

        plt.show()

    # Visualization of eigenvalues
    if eigenvalues is not None:
        plt.figure(figsize=(10, 6))
        plt.plot(eigenvalues, marker='o')
        plt.title("Eigenvalues of Matrix A")
        plt.xlabel("Eigenvalue Index")
        plt.ylabel("Eigenvalue")
        plt.grid(True)
        plt.show()

    # Visualization of eigenvectors
    if eigenvectors is not None:
        plt.figure(figsize=(12, 6))

        for i in range(len(eigenvectors)):
            plt.subplot(1, len(eigenvectors), i + 1)
            plt.plot(eigenvectors[i], marker='o')
            plt.title(f"Eigenvector {i + 1}")
            plt.xlabel("Vector Index")
            plt.ylabel("Value")

        plt.tight_layout()
        plt.show()
        

if __name__ == "__main__":
    main()
