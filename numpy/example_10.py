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
# File Name         :       example_10.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 22, 2023
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       numpy
#
# Installation      :       $ pip install --upgrade numpy flake8 autopep8 black pylint mypy pytest
#
# Usage             :       python ./numpy/example_10.py
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
    This script demonstrates the use of NumPy's polynomial functions to 
    fit a polynomial to a set of data points. It uses np.polyfit to find 
    the coefficients of the polynomial and np.poly1d to create a polynomial 
    function. The fitted polynomial is then plotted alongside the original 
    data for visualization. 
'''

import numpy as np
import matplotlib.pyplot as plt

def main():

    # Generating sample data points
    x_data = np.array([1, 2, 3, 4, 5])
    y_data = np.array([2, 8, 20, 38, 62])

    # Fitting a polynomial of degree 2 to the data
    coefficients = np.polyfit(x_data, y_data, deg=2)

    # Creating a polynomial function from the coefficients
    poly_function = np.poly1d(coefficients)

    # Generating x values for plotting
    x_values = np.linspace(0, 6, 100)

    # Calculating corresponding y values using the polynomial function
    y_values = poly_function(x_values)

    # Plotting the original data and the fitted polynomial
    plt.scatter(x_data, y_data, label="Original Data")
    plt.plot(x_values, y_values, label="Fitted Polynomial (Degree 2)", color='red')

    plt.title("Polynomial Fitting using NumPy")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.legend()
    plt.show()

 
if __name__ ==   "__main__":

    main()
