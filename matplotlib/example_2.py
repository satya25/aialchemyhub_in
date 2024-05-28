#!/usr/bin/en 
# -*- coding: utf-8 -*- 

"""
This script is part of the aialchemyhub.in project 
(https://github.com/satya25/aialchemyhub_in).

Distributed under the MIT License (see LICENSE file for details).
"""  

# ----------------------------------------------------------------------------
# File Name         :       matplotlib/example_2.py
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
# Usage             :       python ./matplotlib/example_2.py
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
    This script generates a simple bar chart representing the 
    sales of different products.
'''

import matplotlib.pyplot as plt

def plot_product_sales_bar_chart():
    """
        Generates a bar chart visualizing product sales,
        handles potential errors with exception handling,
        and logs execution results for debugging and monitoring.
    """
    
    try:
        # Sample data
        products = ['Product A', 'Product B', 'Product C', 'Product D']
        sales = [1500, 2200, 1800, 3000]
        colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold']

        # Creating the bar chart
        plt.bar(products, sales, color=colors)

        # Adding labels and title
        plt.xlabel('Products')
        plt.ylabel('Sales (units)')
        plt.title('Product Sales Overview')

        # Display the plot
        plt.show()

        print("Plot generated successfully!")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # This block ensures the following code executes 
    # only when this script is run directly,
    # not when imported as a module.
    plot_product_sales_bar_chart() 
