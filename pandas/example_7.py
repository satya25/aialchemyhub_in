#!/usr/bin/en 
# -*- coding: utf-8 -*- 

"""
This script is part of the aialchemyhub.in project 
(https://github.com/satya25/aialchemyhub_in).

Distributed under the MIT License (see LICENSE file for details).
"""

#----------------------------------------------------------------------------
# File Name     :   pandas/example-7.py
# Created By    :   Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date  :   Dec 17, 2023
# version       :   1.0
# Release       :   R1
#   
# Dependencies      :   pandas
#
# Installation      :   $ pip install -r ./pandas/requirements.txt
#                       
#
# Usage             :   python ./pandas/example_7.py
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
    This script creates a DataFrame with city-wise population 
    data for different years. It then groups the data by 
    both 'City' and 'Year', calculating the sum of population 
    for each group. The result is a new DataFrame with 
    aggregated population information. 

""" 
 
import pandas as pd

def analyze_population_data():
    # Create a DataFrame
    data = {'City': ['Mumbai', 'Delhi', 'Bangalore', 'Mumbai', 'Delhi', 'Bangalore'],
            'Year': [2020, 2020, 2020, 2021, 2021, 2021],
            'Population': [20, 18, 12, 22, 20, 15]}
    df = pd.DataFrame(data)

    # Display the original DataFrame
    print("Original DataFrame:")
    print(df)

    # Group by 'City' and 'Year' and calculate the sum of population
    grouped_df = df.groupby(['City', 'Year']).agg({'Population': 'sum'}).reset_index()

    # Display the grouped DataFrame
    print("\nGrouped DataFrame:")
    print(grouped_df)

if __name__ == "__main__":
    # This block ensures the following code executes 
    # only when this script is run directly,
    # not when imported as a module.    
    analyze_population_data() 
    
