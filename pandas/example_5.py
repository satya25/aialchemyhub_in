#!/usr/bin/en 
# -*- coding: utf-8 -*- 

"""
This script is part of the aialchemyhub.in project 
(https://github.com/satya25/aialchemyhub_in).

Distributed under the MIT License (see LICENSE file for details).
"""

#----------------------------------------------------------------------------
# File Name         :   pandas/example-4.py
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
# Usage             :   python ./pandas/example_5.py
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

"""
    Problem Statement:  An introduction to column grouping and
    finding min, max and mean column values:
    
    This script creates a DataFrames, and then group by 'City' and 
    calculate mean temperature and maximum humidity 
"""

import pandas as pd

def analyze_weather_data():

    # Create a DataFrame
    data = {'City': ['Mumbai', 'Delhi', 'Bangalore', 'Mumbai', 'Bangalore', 'Pune', 'Hyderabad'],
            'Temperature': [32, 28, 30, 29, 31, 32, 35],
            'Humidity': [60, 75, 50, 80, 65, 78, 81]}

    df = pd.DataFrame(data)

    # Display the original DataFrame
    print("Original DataFrame:")
    print(df)

    # Group by 'City' and calculate mean temperature and maximum humidity
    grouped_df = df.groupby('City').agg({'Temperature': 'mean', 'Humidity': 'max'}).reset_index()

    # Display the grouped and aggregated DataFrame
    print("\nGrouped and Aggregated DataFrame:")
    print(grouped_df)
 

if __name__ == "__main__":
    # This block ensures the following code executes 
    # only when this script is run directly,
    # not when imported as a module.
    analyze_weather_data() 
    