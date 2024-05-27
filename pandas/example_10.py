#!/usr/bin/en 
# -*- coding: utf-8 -*- 

"""
This script is part of the aialchemyhub.in project 
(https://github.com/satya25/aialchemyhub_in).

Distributed under the MIT License (see LICENSE file for details).
"""


#----------------------------------------------------------------------------
# File Name         :   pandas/example-10.py
# Created By        :   Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :   Dec 17, 2023
# version           :   1.0
# Release           :   R1
#   
# Dependencies      :   pandas
#
# Installation      :   $ pip install -r ./pandas/requirements.txt
#                       
#
# Usage             :   python ./pandas/example_10.py
#
# ---------------------------------------------------------------------------
#
# Credits and Acknowledgements
#
# - Special thanks to the pandas community for their excellent library:
#   https://pandas.pydata.org/community/blog/
#
# - The APIs used in this script is documented here:
#   https://pandas.pydata.org/docs/reference/index.html
#
# - Here comes the User Guide:
#   https://pandas.pydata.org/docs/user_guide/index.html
#
# - Code Snippet(s) adapted from    :   -- NOT Applicable --
#
# - Dataset(s) sourced  from        :  
#   https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
#
# - Inspiration for Numpy Arrays drawn from:
#   https://numpy.org/doc/stable/reference/arrays.html
#
# Thank you to the creators and maintainers of these resources!
#

'''
A pivot table is a data summarization tool used in spreadsheet programs. 

Here, we have a DataFrame representing temperature and humidity 
data for different cities.

The pivot_table function is used to create a summary table, where 
the mean values of temperature and humidity are calculated for each city.

The resulting pivot table provides a concise overview of the average 
weather conditions in each city. 
'''

import pandas as pd

def summarize_weather_data():
    # Create a sample DataFrame
    data = {
        'City': ['Mumbai', 'Delhi', 'Mumbai', 'Bangalore', 'Delhi', 'Bangalore'],
        'Temperature': [32, 45, 30, 29, 40, 28],
        'Humidity': [80, 60, 78, 85, 55, 90]
    }

    df = pd.DataFrame(data)

    # Display the original DataFrame
    print("Original DataFrame:")
    print(df)

    # Create a pivot table to summarize temperature and humidity by city
    pivot_table = pd.pivot_table(df, values=['Temperature', 'Humidity'], index='City', aggfunc='mean')

    # Display the pivot table
    print("\nPivot Table (Mean Temperature and Humidity for each City):")
    print(pivot_table)

if __name__ == "__main__":
    # This block ensures the following code executes 
    # only when this script is run directly,
    # not when imported as a module.  
    summarize_weather_data() 

