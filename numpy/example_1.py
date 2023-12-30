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
# File Name         :       example_1.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 22, 2023
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       numpy
#
# Installation      :       $ pip install --upgrade numpy flake8 autopep8 black pylint mypy pytest
#
# Usage             :       python ./numpy/example_1.py
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

import logging
import os
import numpy as np


def main():
    """
    This function creates a simple 2D array and perform basic
    operations such as finding the sum, mean, and transpose.
    """

    # Configure logging
    # creating log file name from current script name
    log_file_name = os.path.splitext(__file__)[0] + ".log"
    logging.basicConfig(
        filename=log_file_name,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    try:
        # Creating a 2D array
        array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        # Finding the sum of all elements
        sum_result = np.sum(array_2d)

        # Finding the mean of all elements
        mean_result = np.mean(array_2d)

        # Transposing the array
        transposed_array = np.transpose(array_2d)

        # Printing the results
        print("Original 2D Array:")
        print(array_2d)
        print("\nSum of all elements:", sum_result)
        print("Mean of all elements:", mean_result)
        print("\nTransposed Array:")
        print(transposed_array)

        # Logging successful execution of script now.
        file_name = os.path.basename(__file__)
        logging.info("%s : Script execution completed successfully.", file_name)

    except (ValueError, TypeError, np.AxisError) as e:
        logging.error("An error occurred: %s", e)
        print(
            "An unexpected error occurred. \
            Please check the logs for details."
        )


if __name__ == "__main__":
    main()
