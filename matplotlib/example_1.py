#!/usr/bin/en 
# -*- coding: utf-8 -*- 
 
"""
This script is part of the aialchemyhub.in project 
(https://github.com/satya25/aialchemyhub_in).

Distributed under the MIT License (see LICENSE file for details).
"""

'''
    This script will demonstrate how to plot 
    a line graph with some sample data
'''

# ----------------------------------------------------------------------------
# File Name         :       matplotlib/example_1.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 25, 2023
# Last Updated On   :       Jan 17, 2024
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       matplotlib
#
# Installation      :       $ pip install -r ./matplotlib/requirements.txt
#                        
#
# Usage             :       python ./matplotlib/example_1.py
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

import logging
import os
import matplotlib.pyplot as plt

def plot_daily_temperature_variation():
    """
    Generates a line graph visualizing daily temperature variations,
    handles potential errors with specific exception handling,
    and logs execution results for debugging and monitoring.
    """
    
    try:
        # Sample data
        days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 8']
        temperature = [30, 32, 28, 35, 29, 33, 28]

        # Plotting the line graph
        plt.plot(days, temperature, marker='o', linestyle='-', color='b', label='Temperature')

        # Adding labels and title
        plt.xlabel('Days')
        plt.ylabel('Temperature (°C)')
        plt.title('Daily Temperature Variation')
        plt.legend()

        # Display the plot
        plt.show()

        logging.info("Plot generated successfully!")
    
    ## handling multiple possible exceptions here.
    except ValueError as e:
        logging.error("Invalid data format: {}".format(e))
    except TypeError as e:
        logging.error("Data type mismatch: {}".format(e)) 
    except Exception as e:
        logging.error("An error occurred: {}".format(e))

if __name__ == "__main__":

    # Configure logging
    logging.basicConfig(filename='temperature_plot.log', level=logging.DEBUG)
    # This block ensures the following code executes 
    # only when this script is run directly,
    # not when imported as a module.
    plot_daily_temperature_variation() 