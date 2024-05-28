#!/usr/bin/en 
# -*- coding: utf-8 -*- 
 
"""
This script is part of the aialchemyhub.in project 
(https://github.com/satya25/aialchemyhub_in).

Distributed under the MIT License (see LICENSE file for details).
""" 

# ----------------------------------------------------------------------------
# File Name         :       matplotlib/example_5.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 25, 2023
# Last Updated On   :       Jan 17, 2024
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       numpy, matplotlib
#
# Installation      :       $ pip install -r ./matplotlib/requirements.txt
#
# Usage             :       python ./matplotlib/example_5.py
#
# ---------------------------------------------------------------------------
#
# Credits and Acknowledgements
#
# - Special thanks to the matplotlib community for their excellent library:
#   https://matplotlib.org/
#
# - The APIs used in this script is documented here:
#  https://matplotlib.org/stable/users/explain/quick_start.html
#
# - Code Snippet(s) adapted from    :   -- NOT Applicable --
#
# - Dataset(s) sourced  from        :   -- NOT Applicable --
#
#
# Thank you to the creators and maintainers of these resources!
#

import matplotlib.pyplot as plt
import numpy as np

def plot_random_data_histogram():
    '''
        This script creates a histogram using random data, providing 
        insights into the distribution of the dataset.
    '''

    try:
        # Generating random data for the histogram
        data = np.random.randn(1000)

        # Creating a histogram
        plt.hist(data, bins=30, color='skyblue', edgecolor='black')

        # Adding labels and title
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Histogram - example-6')

        # Display the plot
        plt.show()
    
        print("Plot generated successfully!")

    except Exception as e:
        print("An error occurred:", e) 
    except ValueError as e:
        print("Invalid data format:", e)
    except TypeError as e:
        print("Data type mismatch:", e)
    
    # ... other specific exceptions as needed
 
if __name__ == "__main__":
    # This block ensures the following code executes 
    # only when this script is run directly,
    # not when imported as a module.    
    plot_random_data_histogram()
    