#!/usr/bin/env python 
#!/usr/bin/en
# -*- coding: utf-8 -*-

"""
    This file is part of aialchemyhub_in
    (https://github.com/satya25/aialchemyhub_in).

    aialchemyhub_in is free software repository:
    You can redistribute it and/or modify it under
    the terms of the MIT License.

    aialchemyhub_in is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    MIT License for more details.

    You should have received a copy of the MIT License along with
    aialchemyhub_in.  If not, see <https://opensource.org/licenses/MIT>.
"""

# ----------------------------------------------------------------------------
# File Name         :       example_6.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 22, 2023
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       numpy
#
# Installation      :       $ pip install --upgrade numpy flake8 autopep8 black pylint mypy pytest
#
# Usage             :       python ./numpy/example_6.py
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
# ---------------------------------------------------------------------------
#
# - Content Removal Requests
#
#   If you are the owner or creator of any content used in this script and
#   would like it to be removed, please contact me at:  spnigam25@yahoo.com
#   I will promptly remove the content upon request.
#
# ---------------------------------------------------------------------------

"""
    Problem Statement:

    We have a 1D array representing the daily sales of a store for a week. 
    We wish  to analyze the data by finding the total sales, average daily 
    sales, and days with sales above a certain threshold.

"""

import numpy as np

def main():

    # 1D array representing daily sales for a week
    daily_sales = np.array([1200, 1500, 900, 1800, 2000, 1300, 1700])

    # Calculating total sales
    total_sales = np.sum(daily_sales)

    # Calculating average daily sales
    average_daily_sales = np.mean(daily_sales)

    # Setting a sales threshold
    sales_threshold = 1500

    # Finding days with sales above the threshold
    high_sales_days = np.where(daily_sales > sales_threshold)[0]

    # Printing the results
    print("Daily Sales Data:", daily_sales)
    print("\nTotal Sales:", total_sales)
    print("Average Daily Sales:", average_daily_sales)
    print(f"Days with Sales above {sales_threshold}:", high_sales_days)
     
if __name__ == "__main__": 
    
    main() 