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
# File Name         :       example_19.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 22, 2023
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       numpy
#
# Installation      :       $ pip install --upgrade numpy flake8 autopep8 black pylint mypy pytest
#
# Usage             :       python ./numpy/example_19.py
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
import numpy.ma as ma

def main():

    # Generate a random array with some invalid values (e.g., -999)
    random_array = np.random.randint(low=0, high=10, size=(3, 4))
    random_array[random_array % 2 == 0] = -999

    # Explanation: Masked arrays are arrays with a separate boolean mask that indicates where values are valid or invalid.
    # In this case, we create a mask for invalid values (-999) in the random array.
    mask = ma.masked_values(random_array, -999)

    # Apply operations on the masked array
    # Explanation: Operations on masked arrays automatically ignore masked values.
    masked_sum = ma.sum(mask)
    masked_mean = ma.mean(mask)

    # Display original array, mask, and results
    print("Original Array:")
    print(random_array)
    print("\nMask:")
    print(mask)
    print("\nMasked Sum:", masked_sum)
    print("Masked Mean:", masked_mean) 

if __name__ == "__main__":
    main()
