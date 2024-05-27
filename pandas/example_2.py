#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script is part of the aialchemyhub.in project 
(https://github.com/satya25/aialchemyhub_in).

Distributed under the MIT License (see LICENSE file for details).
"""

# ----------------------------------------------------------------------------
# File Name         :       example_2.py
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
# Usage             :       python ./pandas/example_2.py
#
# ---------------------------------------------------------------------------
#
# Credits and Acknowledgements
#
# - Special thanks to the numpy community for their excellent library:
#   https://numpy.org/
#
# - The APIs used in this script is documented here:
#  https://numpy.org/doc/stable/reference/index.html
#
# - Code Snippet(s) adapted from    :   -- NOT Applicable --
#
# - Dataset(s) sourced  from        :   -- NOT Applicable --
#
#
# - Inspiration for Numpy Arrays drawn from:
#   https://numpy.org/doc/stable/reference/arrays.html
#
# Thank you to the creators and maintainers of these resources!
#

import pandas as pd

def basic_data_manipulation_and_handling_missing_data(): 
    """
    Wrapper for overall functionality of this script:

    Problem Statement:  Handling Missing Data and Basic Data Manipulation
    """

    # 1. Load a CSV file into a Pandas DataFrame
    url = (
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )
    df = pd.read_csv(url)

    # 2. Display the first few rows of the DataFrame
    print("Original DataFrame:")
    print(df.head())

    # 3. Handling Missing Data
    #    - Identify missing values
    missing_values = df.isnull().sum()
    print("\nMissing Values:")
    print(missing_values)

    #    - Drop rows with missing values
    df_no_missing = df.dropna()
    print("\nDataFrame after dropping missing values:")
    print(df_no_missing.head())

    #    - Fill missing values with mean
    # df_filled_mean = df.fillna(df.mean())
    df_filled_mean = df.fillna(df.mean(numeric_only=True))
    print("\nDataFrame after filling missing values with mean:")
    print(df_filled_mean.head())

    # 4. Basic Data Manipulation
    #   - Select specific columns
    selected_columns = df[["Pclass", "Sex", "Age", "Survived"]]
    print("\nSelected Columns:")
    print(selected_columns.head())

    #    - Filter data based on conditions
    female_survivors = df[(df["Sex"] == "female") & (df["Survived"] == 1)]
    print("\nFemale survivors:")
    print(female_survivors.head())

if __name__ == "__main__":
    # This block ensures the following code executes 
    # only when this script is run directly,
    # not when imported as a module.
    basic_data_manipulation_and_handling_missing_data()
    
