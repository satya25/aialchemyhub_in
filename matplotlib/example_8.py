#!/usr/bin/en 
# -*- coding: utf-8 -*- 

"""
This script is part of the aialchemyhub.in project 
(https://github.com/satya25/aialchemyhub_in).

Distributed under the MIT License (see LICENSE file for details).
"""    

# ----------------------------------------------------------------------------
# File Name         :       matplotlib/example_8.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 22, 2023
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
# ---------------------------------------------------------------------------
#

'''
    This script show cases visualization of a sample dataset with values 
    for three different categories. 
    
    The data is visualized using a line chart, a bar chart, scatter plot and a pie chart. 
    
    The savefig function is used to save the combined charts as an 
    image named 'combined_charts.png'. 
    
    The tight_layout function is used to improve the spacing between subplots. 
'''

import matplotlib.pyplot as plt
import numpy as np

def plot_categorical_data_combos():
    
    try:
        # Sample data
        categories = ['Category A', 'Category B', 'Category C', 'Category D']
        values_line = np.array([20, 35, 25, 40])
        values_bar = np.array([15, 25, 30, 20])
        values_pie = np.array([10, 30, 25, 35])
        values_scatter = np.array([25, 20, 15, 30])

        # Increase canvas size
        plt.figure(figsize=(10, 6))

          # Line chart
        plt.subplot(2, 2, 1)
        plt.plot(categories, values_line, marker='o', color='blue')
        plt.title('Line Chart')
        plt.xlabel('Categories')
        plt.ylabel('Values')

        # Bar chart
        plt.subplot(2, 2, 2)
        plt.bar(categories, values_bar, color='green')
        plt.title('Bar Chart')
        plt.xlabel('Categories')
        plt.ylabel('Values')

        # Pie chart
        plt.subplot(2, 2, 3)
        plt.pie(values_pie, labels=categories, autopct='%1.1f%%', colors=['orange', 'pink', 'purple', 'brown'])
        plt.title('Pie Chart')

        # Scatter plot
        plt.subplot(2, 2, 4)
        plt.scatter(categories, values_scatter, color='red', marker='D')
        plt.title('Scatter Plot')
        plt.xlabel('Categories')
        plt.ylabel('Values')

     
        # Save the figure
        plt.savefig('combined_charts.png')

        # Show the plots
        plt.tight_layout()
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
    plot_categorical_data_combos() 