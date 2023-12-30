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
# File Name         :       example_11.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       Dec 22, 2023
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       numpy
#
# Installation      :       $ pip install --upgrade numpy flake8 autopep8 black pylint mypy pytest
#
# Usage             :       python ./numpy/example_11.py
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


'''
    *** NumPy's FFT for Signal Processing ***

    This script uses NumPy's Fast Fourier Transform (FFT) to analyze the 
    frequency components of a signal. The signal is created as a sum of 
    two sinusoids, and the resulting frequency spectrum is plotted for visualization.
    
'''

import numpy as np
import matplotlib.pyplot as plt


def main():
    
    # Generating a sample signal (sum of two sinusoids)
    t = np.linspace(0, 1, 1000, endpoint=False)  # 1 second, 1000 samples
    signal = 0.7 * np.sin(2 * np.pi * 5 * t) + 0.3 * np.sin(2 * np.pi * 20 * t)

    # Applying Fast Fourier Transform (FFT) to analyze frequency components
    fft_result = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(len(t), t[1] - t[0])

    # Plotting the original signal and its frequency components
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(t, signal)
    plt.title("Original Signal")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")

    plt.subplot(2, 1, 2)
    plt.plot(frequencies, np.abs(fft_result))
    plt.title("Frequency Components")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")

    plt.tight_layout()
    plt.show() 

if __name__ ==  "__main__":

    main() 
