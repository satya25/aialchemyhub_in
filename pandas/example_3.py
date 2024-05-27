#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
 
"""
This script is part of the aialchemyhub.in project 
(https://github.com/satya25/aialchemyhub_in).

Distributed under the MIT License (see LICENSE file for details).
"""

#----------------------------------------------------------------------------
# File Name         :   pandas/example-3.py
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
# Usage             :   python ./pandas/example_3.py
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
Problem Statement:  

This script creates a simple DataFrame, selects specific 
columns, filters data based on a condition, and sorts the 
DataFrame by the 'Age' column.

The script also includes filtering (individuals aged 30 
and above) and sorting (by age in descending order) 
operations 
"""

import pandas as pd

def dataframes_create_sort_filter():

    # Create a DataFrame from a list of dictionaries
    data = [
        {'Name': 'Ravi', 'Age': 28, 'City': 'Mumbai'},
        {'Name': 'Priya', 'Age': 22, 'City': 'Delhi'},
        {'Name': 'Amit', 'Age': 35, 'City': 'Bangalore'},
        {'Name': 'Sneha', 'Age': 30, 'City': 'Chennai'},
        {'Name': 'Vikas', 'Age': 25, 'City': 'Hyderabad'}
    ]

    df = pd.DataFrame(data)

    # Display the original DataFrame
    print("Original DataFrame:")
    print(df)

    # Add a new column for salary
    df['Salary'] = [50000, 60000, 75000, 80000, 55000]

    # Update the 'Age' of Sneha
    df.loc[df['Name'] == 'Sneha', 'Age'] = 31

    # Display the updated DataFrame
    print("\nUpdated DataFrame:")
    print(df)

    # Filtering: Display individuals aged 30 and above
    filtered_df = df[df['Age'] >= 30]
    print("\nFiltered DataFrame (Age >= 30):")
    print(filtered_df)

    # Sorting: Sort the DataFrame by 'Age' in descending order
    sorted_df = df.sort_values(by='Age', ascending=False)
    print("\nSorted DataFrame (Descending Age):")
    print(sorted_df)

    # Group by 'City' and calculate the average salary
    average_salary = df.groupby('City')['Salary'].mean()

    # Display the average salary by city
    print("\nAverage Salary by City:")
    print(average_salary)
 
if __name__ == "__main__":
    # This block ensures the following code executes 
    # only when this script is run directly,
    # not when imported as a module.
    dataframes_create_sort_filter()
    
