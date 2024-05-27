#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
This script is part of the aialchemyhub.in project 
(https://github.com/satya25/aialchemyhub_in).

Distributed under the MIT License (see LICENSE file for details).
"""

# ----------------------------------------------------------------------------
# File Name         :       example_1.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 31, 2023
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       pandas
#
# Installation      :       $ pip install -r ./pandas/requirements.txt
#                           
#
# Usage             :       python ./pandas/example_1.py
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
 
import pandas as pd
 
def load_and_explore_titanic_data(): 
    """
    Wrapper for overall functionality of this script:

    Problem Statement:

    1.  We use Pandas to load a Titanic dataset from a CSV file.
    2.  info() provides information on the DataFrame, including
        data types and missing values.
    3.  head() displays the first few rows to give an overview of the data.
    4.  describe() provides summary statistics for numerical columns.
    5.  tail() is used to display the last few rows.
    6.  Script displays of column names using columns.
    7.  Script provides the total number of rows and columns using shape.

    """

    # Problem Statement: Load and Explore Data

    # 1. Load a CSV file into a Pandas DataFrame
    url = (
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )
    df = pd.read_csv(url)

    # 2. Display basic information about the DataFrame
    print("Basic Info:")
    print(df.info())

    # 3. Display the first and last few rows of the DataFrame
    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nLast 5 Rows:")
    print(df.tail())

    # 4. Display summary statistics of the numerical columns
    print("\nSummary Statistics:")
    print(df.describe())

    # 5. Display column names
    print("\nColumn Names:")
    print(df.columns)

    # 6. Display total number of rows and columns
    num_rows, num_cols = df.shape
    print("\nTotal Rows:", num_rows)
    print("Total Columns:", num_cols)
 
if __name__ == "__main__":
    # This block ensures the following code executes 
    # only when this script is run directly,
    # not when imported as a module.
    load_and_explore_titanic_data()