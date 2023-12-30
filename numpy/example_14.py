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
# File Name         :       example_14.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 22, 2023
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       numpy
#
# Installation      :       $ pip install --upgrade numpy flake8 autopep8 black pylint mypy pytest
#
# Usage             :       python ./numpy/example_14.py
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

def main():

    # 1. Generate random matrices with compatible dimensions
    A = np.random.rand(3, 2)  # 3x2 matrix with random values
    B = np.random.rand(2, 3)  # 2x3 matrix with random values

    # 2. Print matrices
    print("Matrix A:")
    print(A)
    print("Matrix B:")
    print(B)

    # 3. Perform matrix addition with transpose
    C = A + B.T
    print("Sum (A + B.T):")
    print(C)

    # 4. Perform element-wise matrix addition with broadcasting
    D = A + B[:, :, None]  # Add B columns to A rows (broadcasting B along axis 2)
    print("Element-wise addition (A + B[:, :, None]):")
    print(D)

    # 5. Perform matrix subtraction with transpose (option 1)
    E_transposed = A - B.T
    print("Difference (A - B.T):")
    print(E_transposed)

    # 6. Perform element-wise matrix subtraction with broadcasting (option 2)
    # Corrected broadcasting dimensions
    E_broadcasted = A - B.T[:, None, :]  # Broadcast B.T along rows of A
    print("Element-wise difference (A - B.T[:, None, :]):")
    print(E_broadcasted)

    # 7. (Optional) Perform other operations... (dot product, matrix multiplication, etc.)

if __name__ == "__main__":
    main()
