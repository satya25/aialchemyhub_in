#!/usr/bin/en 
# -*- coding: utf-8 -*- 

"""
This script is part of the aialchemyhub.in project 
(https://github.com/satya25/aialchemyhub_in).

Distributed under the MIT License (see LICENSE file for details).
"""

#----------------------------------------------------------------------------
# File Name         :   pandas/example-9.py
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
# Usage             :   python ./pandas/example_9.py
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
    This script showcases working with datetime data, converting it, 
    extracting components, and performing resampling operations. 
""" 

import pandas as pd

def analyze_temperature_data():

    # Create a DataFrame with datetime data
    data = {'Date': ['2023-01-01', '2023-02-15', '2023-03-20'],
            'Temperature (Celsius)': [25, 28, 22]}

    df = pd.DataFrame(data)

    # Display the original DataFrame
    print("Original DataFrame:")
    print(df)

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Extract day, month, and year as separate columns
    df['Day'] = df['Date'].dt.day
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year

    # Display the DataFrame with datetime operations
    print("\nDataFrame with Datetime Operations:")
    print(df)

    # Set the 'Date' column as the index
    df.set_index('Date', inplace=True)

    # Resample the data to get the average temperature per month
    monthly_average = df.resample('M').mean()

    # Display the resampled DataFrame
    print("\nMonthly Average Temperature:")
    print(monthly_average)


if __name__ == "__main__":
    # This block ensures the following code executes 
    # only when this script is run directly,
    # not when imported as a module.     
    analyze_temperature_data()
