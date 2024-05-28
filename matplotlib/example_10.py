#!/usr/bin/en 
# -*- coding: utf-8 -*- 

"""
This script is part of the aialchemyhub.in project 
(https://github.com/satya25/aialchemyhub_in).

Distributed under the MIT License (see LICENSE file for details).
"""     

# ----------------------------------------------------------------------------
# File Name         :       matplotlib/example_10.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 20, 2023
# Last Updated On   :       Jan 17, 2024
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       numpy, matplotlib
#
# Installation      :       $ pip install -r ./matplotlib/requirements.txt
#
# Usage             :       python ./matplotlib/example_7.py
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

def plot_multiple_line_charts():
    '''
        This script generates a figure with a single subplot containing six line 
        charts, each with a different color and style. 
        The chart is saved as 'multiple_line_charts.png'.
    '''
    
    try:
        # Sample data
        x = np.linspace(0, 10, 100)
        datasets = {
            'Dataset 1': np.sin(x),
            'Dataset 2': np.cos(x),
            'Dataset 3': np.tan(x),
            'Dataset 4': np.exp(x / 10),
            'Dataset 5': -np.sin(x),
            'Dataset 6': np.log(x + 1)
        }

        # Multiple Line Charts
        plt.figure(figsize=(10, 6))
        for label, data in datasets.items():
            plt.plot(x, data, label=label)

        plt.title('Multiple Line Charts')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()

        # Save the figure
        plt.savefig('multiple_line_charts.png')

        # Show the plot
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
    plot_multiple_line_charts()
