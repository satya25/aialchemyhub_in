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
# File Name         :       example_18.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 22, 2023
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       numpy
#
# Installation      :       $ pip install --upgrade numpy flake8 autopep8 black pylint mypy pytest
#
# Usage             :       python ./numpy/example_18.py
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
    Advanced Statistical Techniques:

    Explore ANOVA (analysis of variance) for comparing means of multiple groups.
    Implement non-parametric tests like Mann-Whitney U test and Kruskal-Wallis test.
    Utilize NumPy functions for bootstrapping and hypothesis testing simulations.
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f_oneway, mannwhitneyu, kruskal
from sklearn.utils import resample

def main():

    # Set random seed for reproducibility
    np.random.seed(42)

    # Generate sample data for three groups
    group1 = np.random.normal(loc=5, scale=1, size=50)
    group2 = np.random.normal(loc=7, scale=1, size=50)
    group3 = np.random.normal(loc=6, scale=1, size=50)

    # ANOVA (Analysis of Variance)
    anova_statistic, anova_p_value = f_oneway(group1, group2, group3)

    # Non-parametric test (Mann-Whitney U test)
    u_statistic, mw_p_value = mannwhitneyu(group1, group2)

    # Non-parametric test (Kruskal-Wallis test)
    kruskal_statistic, kruskal_p_value = kruskal(group1, group2, group3)

    # Bootstrapping (Resampling with replacement)
    bootstrap_means = []
    num_bootstrap_samples = 1000

    for _ in range(num_bootstrap_samples):
        resampled_data = resample(group1)
        bootstrap_mean = np.mean(resampled_data)
        bootstrap_means.append(bootstrap_mean)

    # Visualization of results
    plt.figure(figsize=(14, 8))

    # Boxplot for ANOVA
    plt.subplot(2, 2, 1)
    plt.boxplot([group1, group2, group3], labels=['Group 1', 'Group 2', 'Group 3'])
    plt.title("ANOVA: Boxplot of Three Groups")
    plt.ylabel("Values")

    # Mann-Whitney U test results
    plt.subplot(2, 2, 2)
    plt.bar([1, 2], [u_statistic, 0], tick_label=['Mann-Whitney U Statistic', 0], color=['blue', 'gray'])
    plt.title("Mann-Whitney U Test")
    plt.ylabel("Values")

    # Kruskal-Wallis test results
    plt.subplot(2, 2, 3)
    plt.bar([1, 2], [kruskal_statistic, kruskal_p_value], tick_label=['Kruskal Statistic', 'P-value'],
            color=['blue', 'green'])
    plt.title("Kruskal-Wallis Test")
    plt.ylabel("Values")

    # Bootstrapped distribution
    plt.subplot(2, 2, 4)
    plt.hist(bootstrap_means, bins=30, edgecolor="k", alpha=0.7)
    plt.title("Bootstrapped Distribution of Means")
    plt.xlabel("Bootstrapped Means")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()

    # Print results
    print("ANOVA Results:")
    print("ANOVA Statistic:", anova_statistic)
    print("P-value:", anova_p_value)

    print("\nMann-Whitney U Test Results:")
    print("U Statistic:", u_statistic)
    print("P-value:", mw_p_value)

    print("\nKruskal-Wallis Test Results:")
    print("Kruskal Statistic:", kruskal_statistic)
    print("P-value:", kruskal_p_value)

if __name__ == "__main__":
    main()

