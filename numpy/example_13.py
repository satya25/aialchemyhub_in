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
# File Name         :       example_13.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 22, 2023
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       numpy
#
# Installation      :       $ pip install --upgrade numpy flake8 autopep8 black pylint mypy pytest
#
# Usage             :       python ./numpy/example_13.py
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
    This script covers some fundamental NumPy features like:

    1.  Creating arrays from various sources (lists in this case).
   
    2.  Accessing elements using indexing and slicing.
    
    3.  Performing basic arithmetic operations like addition, 
        subtraction, and multiplication.
    
    4.  Calculating statistics like mean.
   
    5.  Demonstrating broadcasting, where an operation is applied 
        element-wise between arrays of different shapes.

    
'''

import numpy as np

def main():

    # 1. Create a NumPy array from a list
    data = [1, 2, 3, 4, 5]
    arr1 = np.array(data)

    # 2. Print the array and its dimensions
    print("Array:", arr1)
    print("Dimensions:", arr1.shape)

    # 3. Access specific elements using indexing
    first_element = arr1[0]
    last_element = arr1[-1]
    subarray = arr1[1:3]

    # 4. Perform basic arithmetic operations
    sum_array = arr1 + 5
    mean_array = np.mean(arr1)

    # 5. Print the results of element access and operations
    print("First element:", first_element)
    print("Last element:", last_element)
    print("Subarray:", subarray)
    print("Sum array:", sum_array)
    print("Mean:", mean_array)

    # 6. Demonstrate broadcasting
    arr2 = np.ones(5)
    multiplied_array = arr1 * arr2

    print("Multiplied array:", multiplied_array)

if __name__ ==  "__main__":

    main()  
