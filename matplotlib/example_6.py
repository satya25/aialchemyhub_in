#!/usr/bin/en 
# -*- coding: utf-8 -*- 
 
"""
This script is part of the aialchemyhub.in project 
(https://github.com/satya25/aialchemyhub_in).

Distributed under the MIT License (see LICENSE file for details).
"""  

# ----------------------------------------------------------------------------
# File Name         :       matplotlib/example_6.py
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
# Usage             :       python ./matplotlib/example_6.py
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
# - Content Removal Requests
#
#   If you are the owner or creator of any content used in this script and
#   would like it to be removed, please contact me at:  spnigam25@yahoo.com
#   I will promptly remove the content upon request.
#
# ---------------------------------------------------------------------------

import matplotlib.pyplot as plt
  
def plot_category_pie_chart():
    '''
        This script generates a pie chart with sample data. 
    '''
    try:
        # Sample data for the pie chart
        labels = ['Category A', 'Category B', 'Category C', 'Category D',  'Category D']
        sizes = [25, 30, 20, 25, 43]
        colors = ['skyblue', 'lightcoral', 'lightgreen', 'lightsalmon', 'teal']

        # Creating a pie chart
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

        # Adding a title
        plt.title('Pie Chart - example_6')

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
    plot_category_pie_chart()  
    