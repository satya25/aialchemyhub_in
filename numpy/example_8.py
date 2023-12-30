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
# File Name         :       example_8.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 22, 2023
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       numpy
#
# Installation      :       $ pip install --upgrade numpy flake8 autopep8 black pylint mypy pytest
#
# Usage             :       python ./numpy/example_8.py
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
    *** Singular Value Decomposition (SVD) for Image Compression ***
     
    Problem Statement:
    
    You have a grayscale image represented as a 2D array, and you want to 
    compress it using Singular Value Decomposition (SVD).

"""

import numpy as np
import matplotlib.pyplot as plt

def main(): 

    # Creating a sample grayscale image (10x10 array)
    image = np.array([[10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
                      [110, 120, 130, 140, 150, 160, 170, 180, 190, 200],
                      [210, 220, 230, 240, 250, 240, 230, 220, 210, 200],
                      [190, 180, 170, 160, 150, 140, 130, 120, 110, 100],
                      [90, 80, 70, 60, 50, 40, 30, 20, 10, 0],
                      [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
                      [110, 120, 130, 140, 150, 160, 170, 180, 190, 200],
                      [210, 220, 230, 240, 250, 240, 230, 220, 210, 200],
                      [190, 180, 170, 160, 150, 140, 130, 120, 110, 100],
                      [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]])

    # Applying Singular Value Decomposition (SVD) for compression
    U, S, Vt = np.linalg.svd(image, full_matrices=False)

    # Selecting the top k singular values to compress the image
    k = 5
    compressed_image = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vt[:k, :]))

    # Plotting the original and compressed images
    plt.figure(figsize=(8, 4))

    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image, cmap='gray')

    plt.subplot(1, 2, 2)
    plt.title(f"Compressed Image (k={k})")
    plt.imshow(compressed_image, cmap='gray')

    plt.show()

     

if __name__ == "__main__": 
    
    main() 
