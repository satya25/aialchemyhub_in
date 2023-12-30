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
# File Name         :       tests/test_example_1.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 22, 2023
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       numpy
#
# Installation      :       $ pip install --upgrade numpy flake8 autopep8 black pylint mypy pytest
#
# Usage             :       pytest ./numpy/tests/test_example_1.py
#
# Output            :       ./numpy/tests/results/test_results_example_1.txt
#
# ---------------------------------------------------------------------------
#
# Credits and Acknowledgements
#
# - Special thanks to the numpy community for their excellent library:
#   https://numpy.org/
#  
# - I express my gratitude to pytest community for this awesome Unit Testing tool:
#   https://docs.pytest.org/en/7.4.x/
#
# - The APIs used in this script is documented here:
#   https://docs.pytest.org/en/7.4.x/reference/reference.htm
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
    Unit tests for example_1.py script.
"""

import subprocess
import logging
import os

def run_script_and_capture_output(script_path):
    """
    Run the specified script and capture the output.

    Parameters:
    - script_path (str): The path to the script to be tested.

    Returns:
    - subprocess.CompletedProcess: CompletedProcess object.
    """
    return subprocess.run(
        ["python", script_path],
        capture_output=True,
        text=True,
    )
    
def test_script_runs_without_errors():
    """
    Test if the script runs without errors.
    """
    # Get the absolute path to the directory containing this test script
    test_script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Navigate up one directory to reach the directory containing "example_1.py"
    project_directory = os.path.abspath(os.path.join(test_script_directory, os.pardir))
    
    script_path = os.path.join(project_directory, "example_1.py")

    result = run_script_and_capture_output(script_path)

    assert result.returncode == 0, f"Script failed with output:\n{result.stdout}"

    # Log the results
    log_results(result.stdout, script_path)
    
def log_results(output, script_path):
    """
    Log the test results to a file.

    Parameters:
    - output (str): Output captured from the script.
    - script_path (str): Name of the script being tested.
    """
    results_folder = "./results/"
    os.makedirs(results_folder, exist_ok=True)

    result_file_path = os.path.join(results_folder, "test_results_example_1.txt")

    with open(result_file_path, "w") as result_file:
        result_file.write("Test Results:\n")
        result_file.write(output)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    try:
        test_script_runs_without_errors()
        logging.info("All tests passed successfully.")
    except AssertionError as e:
        logging.error(f"Test failed: {e}")
