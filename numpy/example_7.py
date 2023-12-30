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
# File Name         :       example_7.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 22, 2023
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       numpy
#
# Installation      :       $ pip install --upgrade numpy flake8 autopep8 black pylint mypy pytest
#
# Usage             :       python ./numpy/example_7.py
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
    Problem Statement:

    You have a 2D array representing a grayscale image, and you want to 
    apply a Gaussian blur to the image.


"""

import numpy as np
from scipy.ndimage import convolve

def main():
    
    # Creating a sample grayscale image (5x5 array)
    image = np.array([[10, 20, 30, 40, 50],
                      [60, 70, 80, 90, 100],
                      [110, 120, 130, 140, 150],
                      [160, 170, 180, 190, 200],
                      [210, 220, 230, 240, 250]])

    # Gaussian blur kernel
    kernel = np.array([[1, 2, 1],
                       [2, 4, 2],
                       [1, 2, 1]])

    # Applying Gaussian blur using convolution
    blurred_image = convolve(image, kernel)

    # Printing the results
    print("Original Image:")
    print(image)
    print("\nGaussian Blurred Image:")
    print(blurred_image)

if __name__ == "__main__": 
    
    main() 
 
'''
    This script demonstrates advanced array manipulation by applying a Gaussian 
    blur to a grayscale image using convolution. It introduces the use of the 
    scipy.ndimage.convolve function for more complex operations. 
    
'''
