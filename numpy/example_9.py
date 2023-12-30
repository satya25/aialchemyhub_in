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
# File Name         :       example_9.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 22, 2023
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       numpy
#
# Installation      :       $ pip install --upgrade numpy flake8 autopep8 black pylint mypy pytest
#
# Usage             :       python ./numpy/example_9.py
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
  
"""
    *** Broadcasting and Vectorization ***
    
    Problem Statement:
    
        We have two matrices, and you want to perform element-wise operations using 
        broadcasting and vectorization.
"""

import numpy as np

def main():

    # Creating two matrices (4x3 and 1x3)
    matrix_a = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                        [10, 11, 12]])

    matrix_b = np.array([0.5, 1, 2])

    # Broadcasting and Vectorization: Element-wise multiplication
    result_multiplication = matrix_a * matrix_b

    # Broadcasting and Vectorization: Element-wise addition
    result_addition = matrix_a + matrix_b

    # Broadcasting and Vectorization: Element-wise division
    result_division = matrix_a / matrix_b

    # Printing the results
    print("Matrix A:")
    print(matrix_a)
    
    print("\nMatrix B:")
    print(matrix_b)
    
    print("\nElement-wise Multiplication:")
    print(result_multiplication)
    
    print("\nElement-wise Addition:")
    print(result_addition)
    
    print("\nElement-wise Division:")
    print(result_division) 

    # Broadcasting and vectorization are two powerful concepts in 
    # NumPy that enhance the efficiency of array operations.

    '''
    Broadcasting:

        Definition:
        
            Broadcasting is the ability of NumPy to perform element-wise operations on arrays of different shapes and sizes. In simple terms, it allows NumPy to automatically expand smaller arrays to match the shape of larger arrays, enabling element-wise operations without the need for explicit looping.

        Key Points:

        Implicit Replication    :   Smaller arrays are implicitly replicated along the 
                                    missing dimensions to match the shape of larger arrays.
                                    
        No Copying              :   Broadcasting does not actually create multiple copies 
                                    of the data, making it memory-efficient.
        Rules for Broadcasting  : 
        
            If the arrays have a different number of dimensions, pad the smaller 
            array's shape with ones on its left side.
            
            Compare the sizes along each dimension. The sizes are compatible 
            if they are equal or one of them is 1.
            
            If the sizes along a dimension are different and neither is 1, broadcasting 
            will result in an error.
    '''

    # Broadcasting Example
    matrix_c = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                        [10, 11, 12]])

    matrix_d = np.array([0.5, 1, 2])

    # Broadcasting: Element-wise multiplication
    result_multiplication_broadcasting = matrix_c * matrix_d

    print("The result of Broadcasting (Element-wise multiplication) operation is : ", result_multiplication_broadcasting);
 
    # In the above example, matrix_b is broadcasted along the rows to match the 
    # shape of matrix_a, and element-wise multiplication is performed without 
    # the need for explicit loops.

    '''
    Vectorization:
        Definition:
            Vectorization refers to the process of converting a sequence of 
            operations into a vectorized form that can be executed on entire 
            arrays without the need for explicit looping. In NumPy, this is achieved 
            by applying operations directly to arrays, which are then executed 
            in a highly optimized, compiled C-code under the hood.

    Key Points:

        Efficiency      :   

            Vectorized operations are highly optimized and run faster compared to 
            traditional explicit looping in Python.
        
        Readable Code   :   
        
            Vectorized code is often more concise and readable, as it eliminates the 
            need for explicit loops.
            
        Broadcasting Enhances Vectorization: 
            
            Broadcasting enhances vectorization by allowing element-wise operations 
            on arrays with different shapes.
    ''' 

    # Vectorized Example
    matrix_e = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                        [10, 11, 12]])

    matrix_f = np.array([0.5, 1, 2])

    # Vectorized: Element-wise multiplication
    result_vectorized_multiplication = matrix_e * matrix_f

    print("The result of Vectorized (Element-wise multiplication) operation is : ", result_vectorized_multiplication);

if __name__ ==   "__main__":

    main()

