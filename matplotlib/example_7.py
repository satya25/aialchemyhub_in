#!/usr/bin/en 
# -*- coding: utf-8 -*- 

"""
This script is part of the aialchemyhub.in project 
(https://github.com/satya25/aialchemyhub_in).

Distributed under the MIT License (see LICENSE file for details).
"""    

# ----------------------------------------------------------------------------
# File Name         :       matplotlib/example_7.py
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

'''
    This script generates a box plot with three categories of sample data.
    
    
    A box plot, also known as a box-and-whisker plot, is a graphical representation 
    of the distribution of a dataset. It provides a summary of key statistical measures 
    and displays the spread and skewness of the data.

    Here are the key components of a box plot:

    Box         :   The box represents the interquartile range (IQR), which is 
                    the range between the first quartile (Q1) and the third 
                    quartile (Q3). The box's length indicates the spread of the 
                    middle 50% of the data.
    
    Whiskers    :   The whiskers extend from the box and show the range of the 
                    data outside the IQR. They are often set to a certain multiple 
                    of the IQR, like 1.5 times the IQR.
    
    Median      :   A line inside the box represents the median (Q2), which is 
                    the middle value of the dataset when it's sorted.
    
    Outliers    :   Points beyond the whiskers are considered outliers 
                    and are plotted individually.
 
    
    Box plots are useful for identifying the central tendency, spread, 
    and presence of outliers in a dataset. They are particularly helpful 
    when comparing the distribution of multiple datasets or variables.


'''

def plot_categorical_boxplot():
    '''
        This Python script utilizes the Matplotlib library to create 
        an insightful box plot with distinct fill colors for each category. 
        The script generates sample data for three categories, creating 
        a box plot that visually represents the distribution of values 
        within each category. By incorporating the `boxprops` parameter 
        and customizing box face colors, the resulting plot provides a 
        clear visual distinction between the categories. The x-axis is 
        labeled with descriptive category names, and the plot is 
        appropriately titled. This script serves as a concise and 
        customizable example for creating box plots with Matplotlib, 
        showcasing the flexibility and versatility of the library in 
        visualizing categorical data. 
    '''
    
    try:
        import matplotlib.pyplot as plt
        import numpy as np

        # Sample data for the box plot
        data = [np.random.normal(0, std, 100) for std in range(1, 5)]

        # Creating a box plot with different fill colors
        colors = ['lightblue', 'lightgreen', 'lightcoral', 'teal']
        boxprops = dict(facecolor=colors[0])
        bplot = plt.boxplot(data, vert=True, patch_artist=True, boxprops=boxprops)

        # Assigning different colors to each box
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)

        # Adding labels and title
        plt.xticks([1, 2, 3, 4], ['Category 1', 'Category 2', 'Category 3', 'Category 4'])
        plt.xlabel('Categories')
        plt.ylabel('Values')
        plt.title('Box Plot - example_7')

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
    plot_categorical_boxplot()

