#!/usr/bin/en 
# -*- coding: utf-8 -*-

"""
This script is part of the aialchemyhub.in project 
(https://github.com/satya25/aialchemyhub_in).

Distributed under the MIT License (see LICENSE file for details).
"""

#----------------------------------------------------------------------------
# File Name         :   pandas/example-8.py
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
# Usage             :   python ./pandas/example_8.py
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
   In this script, we create two DataFrames (df1 and df2) 
   and then merge them based on the 'ID' column.  

   Additionally, we perform vertical and horizontal 
   concatenation of DataFrames.

""" 

import pandas as pd

def work_with_dataframes():
    # Create two DataFrames
    df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Rahul', 'Priya', 'Amit']})
    df2 = pd.DataFrame({'ID': [2, 3, 4], 'Age': [25, 30, 22]})

    # Display the original DataFrames
    print("DataFrame 1:")
    print(df1)
    print("\nDataFrame 2:")
    print(df2)

    # Merge DataFrames based on 'ID'
    merged_df = pd.merge(df1, df2, on='ID', how='inner')

    # Display the merged DataFrame
    print("\nMerged DataFrame:")
    print(merged_df)

    # Concatenate DataFrames vertically
    concatenated_df = pd.concat([df1, df2], axis=0, ignore_index=True)

    # Display the concatenated DataFrame
    print("\nConcatenated DataFrame (Vertical):")
    print(concatenated_df)

    # Concatenate DataFrames horizontally
    concatenated_horizontal_df = pd.concat([df1, df2], axis=1)

    # Display the concatenated DataFrame
    print("\nConcatenated DataFrame (Horizontal):")
    print(concatenated_horizontal_df)

if __name__ == "__main__":
    # This block ensures the following code executes 
    # only when this script is run directly,
    # not when imported as a module.    
    work_with_dataframes() 
