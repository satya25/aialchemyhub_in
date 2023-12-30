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
# File Name         :       example_17.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 22, 2023
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       numpy
#
# Installation      :       $ pip install --upgrade numpy flake8 autopep8 black pylint mypy pytest
#
# Usage             :       python ./numpy/example_17.py
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
    Correlation & Regression Analysis:

    -- Calculate correlation coefficients (Pearson, Spearman) to measure linear relationships between variables.
    -- Perform linear regression to model the relationship between a dependent variable and one or more independent variables.
    -- Analyze regression results like coefficients, R-squared, and p-values.


''' 

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from sklearn.linear_model import LinearRegression

def main():

    # Generate sample data
    np.random.seed(42)
    X = np.random.rand(100, 1) * 10  # Independent variable
    Y = 2 * X + 1 + np.random.randn(100, 1) * 2  # Dependent variable with noise

    # Calculate Pearson correlation coefficient
    pearson_corr = np.corrcoef(X.flatten(), Y.flatten())[0, 1]

    # Calculate Spearman correlation coefficient
    spearman_corr, _ = spearmanr(X.flatten(), Y.flatten())

    # Linear regression model
    model = LinearRegression()
    model.fit(X, Y)

    # Regression results
    slope = model.coef_[0, 0]
    intercept = model.intercept_
    r_squared = model.score(X, Y)

    # Predictions using the model
    X_pred = np.linspace(min(X), max(X), 100).reshape(-1, 1)
    Y_pred = model.predict(X_pred)

    # Visualization
    plt.figure(figsize=(12, 6))

    # Scatter plot of data points
    plt.scatter(X, Y, label="Data Points", color='blue')

    # Linear regression line
    plt.plot(X_pred, Y_pred, label=f"Linear Regression (y={slope:.2f}x + {intercept[0]:.2f})", color='red')

    plt.title("Correlation & Linear Regression Analysis")
    plt.xlabel("Independent Variable (X)")
    plt.ylabel("Dependent Variable (Y)")
    plt.legend()
    plt.grid(True)
    plt.show() 
    
    # Print results
    print("Pearson Correlation Coefficient:", pearson_corr)
    print("Spearman Correlation Coefficient:", spearman_corr)
    print("\nLinear Regression Results:")
    print("Slope (Coefficient):", slope)
    print("Intercept:", intercept)
    print("R-squared:", r_squared) 

if __name__ == "__main__":
    main()
