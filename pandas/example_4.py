#!/usr/bin/env python 
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
# Usage             :   python ./pandas/example_4.py
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
Problem Statement:  An introduction to merging and concatenation:

This script creates two DataFrames, then concatenates them vertically 
using pd.concat. Additionally, it merges the DataFrames based on the 
'Name' column using pd.merge.  
"""

import pandas as pd

def dataframes_concatenate_and_merge(): 

    # Create two DataFrames
    data1 = {'Name': ['Ravi', 'Priya', 'Amit'],
             'Age': [28, 22, 35],
             'City': ['Mumbai', 'Delhi', 'Bangalore']}

    data2 = {'Name': ['Sneha', 'Vikas'],
             'Age': [30, 25],
             'City': ['Chennai', 'Hyderabad']}

    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    # Display the original DataFrames
    print("DataFrame 1:")
    print(df1)
    print("\nDataFrame 2:")
    print(df2)

    # Concatenate DataFrames vertically
    concatenated_df = pd.concat([df1, df2], ignore_index=True)

    # Display the concatenated DataFrame
    print("\nConcatenated DataFrame:")
    print(concatenated_df)

    # Merge DataFrames based on the 'Name' column
    merged_df = pd.merge(df1, df2, on='Name', how='outer')

    # Display the merged DataFrame
    print("\nMerged DataFrame:")
    print(merged_df)
  
 
if __name__ == "__main__":
    # This block ensures the following code executes 
    # only when this script is run directly,
    # not when imported as a module.
    dataframes_concatenate_and_merge()
    