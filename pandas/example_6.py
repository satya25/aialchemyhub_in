#!/usr/bin/en 
# -*- coding: utf-8 -*-

"""
This script is part of the aialchemyhub.in project 
(https://github.com/satya25/aialchemyhub_in).

Distributed under the MIT License (see LICENSE file for details).
"""

#----------------------------------------------------------------------------
# File Name         :   pandas/example-6.py
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
# Usage             :   python ./pandas/example_6.py
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
     Merging and concatenating DataFrames:
     
     This script creates two DataFrames representing population 
     and area information for cities, then performs both a 
     merge and concatenation operation. The result is two new 
     DataFrames, one with merged information and the other 
     with concatenated rows.  
""" 

import pandas as pd

def analyze_city_data():

    # Create two DataFrames
    df1 = pd.DataFrame({'City': ['Mumbai', 'Delhi', 'Bangalore'],
                        'Population': [20, 18, 12]})
    df2 = pd.DataFrame({'City': ['Mumbai', 'Delhi', 'Hyderabad'],
                        'Area': [603, 556, 650]})

    # Display the original DataFrames
    print("DataFrame 1:")
    print(df1)
    print("\nDataFrame 2:")
    print(df2)

    # Merge DataFrames on 'City'
    merged_df = pd.merge(df1, df2, on='City', how='inner')

    # Concatenate DataFrames along rows
    concatenated_df = pd.concat([df1, df2], axis=0, ignore_index=True)

    # Display the merged and concatenated DataFrames
    print("\nMerged DataFrame:")
    print(merged_df)
    print("\nConcatenated DataFrame:")
    print(concatenated_df)

if __name__ == "__main__":
    # This block ensures the following code executes 
    # only when this script is run directly,
    # not when imported as a module.
    analyze_city_data() 
    
