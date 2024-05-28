#!/usr/bin/en 
# -*- coding: utf-8 -*- 

"""
This script is part of the aialchemyhub.in project 
(https://github.com/satya25/aialchemyhub_in).

Distributed under the MIT License (see LICENSE file for details).
"""  

# ----------------------------------------------------------------------------
# File Name         :       matplotlib/example_4.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 25, 2023
# Last Updated On   :       Jan 17, 2024
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       numpy, matplotlib
#
#
# Installation      :       $ pip install -r ./matplotlib/requirements.txt
#
# Usage             :       python ./matplotlib/example_4.py
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
# ---------------------------------------------------------------------------
#

import matplotlib.pyplot as plt
import numpy as np

def plot_random_scatter():
    """
        Generates a scatter plot with 50 random points, handles 
        potential errors with specific exception handling, and 
        indicates successful plot generation or any errors that occur.
    """
    
    try:
        # Generating data for a scatter plot
        x = np.random.rand(50)
        y = np.random.rand(50)

        # Creating a scatter plot
        plt.scatter(x, y, color='green', marker='s', label='Random Points')

        # Adding labels and title
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Scatter Plot - example-4')

        # Adding a legend
        plt.legend()

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
    plot_random_scatter()
    
    