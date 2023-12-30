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
# File Name         :       example_15.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 22, 2023
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       numpy
#
# Installation      :       $ pip install --upgrade numpy flake8 autopep8 black pylint mypy pytest
#
# Usage             :       python ./numpy/example_15.py
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
 
from scipy.stats import ttest_1samp, f_oneway, mannwhitneyu
from sklearn.utils import resample

import matplotlib.pyplot as plt

def main():

    # Generate random data
    data1 = np.random.normal(size=100)  # Normal distribution
    data2 = np.random.binomial(n=10, p=0.5, size=50)  # Binomial distribution

    # Calculate basic statistics
    mean1 = np.mean(data1)
    median1 = np.median(data1)
    std1 = np.std(data1)
    var1 = np.var(data1)
    percentiles1 = np.percentile(data1, [25, 50, 75])

    # Print descriptive statistics
    print("Data 1:")
    print("Mean:", mean1)
    print("Median:", median1)
    print("Standard deviation:", std1)
    print("Variance:", var1)
    print("Percentiles:", percentiles1)

    # Visualize data distribution
    plt.figure(figsize=(10, 6))
    plt.hist(data1, bins=20, edgecolor="k", alpha=0.7)
    plt.xlabel("Data Values")
    plt.ylabel("Frequency")
    plt.title("Distribution of Data 1")
    plt.grid(True)
    plt.show()

    # Hypothesis testing (Alternative approach)
    t_statistic, p_value = ttest_1samp(data1, popmean=5)  # One-sample t-test (mean=5)

    print("T-statistic:", t_statistic)
    print("P-value:", p_value)  # Interpret p-value for significance

    # Correlation & Regression (adjusted for dimension mismatch)
    correlation, _ = np.corrcoef(data1[:50], data2)  # Pearson correlation

    print("Correlation between Data 1 and Data 2:", correlation)

    ####################################################################

    # Advanced techniques: ANOVA, non-parametric tests, bootstrapping
    '''
        ANOVA (Analysis of Variance) for comparing means of multiple groups.
        Mann-Whitney U test, a non-parametric test for comparing distributions of two independent samples.
        Bootstrapping to estimate the sampling distribution of the mean.
    '''

    # ANOVA (Analysis of Variance)
    group1 = np.random.normal(loc=5, scale=1, size=50)
    group2 = np.random.normal(loc=7, scale=1, size=50)
    group3 = np.random.normal(loc=6, scale=1, size=50)

    anova_statistic, anova_p_value = f_oneway(group1, group2, group3)

    print("\nANOVA:")
    print("ANOVA Statistic:", anova_statistic)
    print("P-value:", anova_p_value)  # Interpret p-value for significance

    # Non-parametric test (Mann-Whitney U test)
    u_statistic, mw_p_value = mannwhitneyu(data1, data2)

    print("\nMann-Whitney U Test:")
    print("U Statistic:", u_statistic)
    print("P-value:", mw_p_value)  # Interpret p-value for significance

    # Bootstrapping (Resampling with replacement)
    bootstrap_means = []
    num_bootstrap_samples = 1000

    for _ in range(num_bootstrap_samples):
        resampled_data = resample(data1)
        bootstrap_mean = np.mean(resampled_data)
        bootstrap_means.append(bootstrap_mean)

    # Visualize bootstrapped distribution
    plt.figure(figsize=(10, 6))
    plt.hist(bootstrap_means, bins=30, edgecolor="k", alpha=0.7)
    plt.xlabel("Bootstrapped Means")
    plt.ylabel("Frequency")
    plt.title("Bootstrapped Distribution of Means")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
