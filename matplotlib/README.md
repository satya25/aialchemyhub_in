**Matplotlib Examples**

This folder provides a collection of 20 Python scripts demonstrating core functionalities of the Pandas library for data analysis. These scripts are designed to help you learn and practice various data manipulation and exploration techniques.

**Getting Started:**

1. **Prerequisites:** Ensure you have Python installed on your system. You can check by running `python --version` in your terminal.

2. **Dependencies:** These scripts require the following Python libraries:

   - pandas
   - numpy
   - matplotlib

   You can install them using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Running the Scripts:** Navigate to the `./matplotlib` folder in your terminal and execute a script using:

   ```bash
   python <script_name>.py
   ```

   Replace `<script_name>` with the actual filename of the script you want to run (e.g., `python example_1.py`).

**Examples:**

This folder includes 20 example scripts covering various Matplotlib operations. Here are some key functionalities demonstrated:

- Loading data from CSV files
- Exploring data with descriptive statistics
- Data cleaning and manipulation
- Data visualization using Matplotlib (if applicable)
  
1. **example_1.py**
 
	* **Description:** This script demonstrates creating a line graph with Matplotlib to visualize daily temperature variations. It includes sample data for temperature across several days and plots them using markers and labels.

	* **Relevant Documentation:**
	  - Matplotlib: [https://matplotlib.org/](https://matplotlib.org/)

	* **Function:**
	  - `plot_daily_temperature_variation()`: Generates a line graph for daily temperature variations, handling potential data errors and logging execution results.

	* **How to Run:**

	```bash
	python ./matplotlib/example_1.py
	```
	
	* **Note:**
	  - This script utilizes basic error handling and logging for demonstration purposes. You might adjust the logging level as needed.

2. **example_2.py**

* **Description:** This script demonstrates creating a bar chart with Matplotlib to visualize product sales. It includes sample data for product names and sales figures, and plots them as bars with distinct colors.

* **Relevant Documentation:**
  - Matplotlib: [https://matplotlib.org/](https://matplotlib.org/)

* **Function:**
  - `plot_product_sales_bar_chart()`: Generates a bar chart visualizing product sales, handling potential errors and logging execution results (logging not implemented in this example).

* **How to Run:**

	```bash
	python ./matplotlib/example_2.py
	```
* **Note:**

  - This script utilizes basic error handling (printing error messages). You might want to implement logging for more detailed tracking.

3. **example_3.py**

* **Description:** This script demonstrates creating a line plot for a sine curve using Matplotlib. It utilizes NumPy for data generation. The curve is styled with a blue dashed line and circular markers. Labels, title, and a legend are included for better visualization.

* **Relevant Documentation:**
  - Matplotlib: [https://matplotlib.org/](https://matplotlib.org/)
  - NumPy: [https://numpy.org/doc/](https://numpy.org/doc/)

* **Function:**
  - `plot_sine_curve()`: Generates a line plot for a sine curve, handling potential errors with specific exception handling (e.g., value format, data type mismatches).

* **How to Run:**

	```bash
	python ./matplotlib/example_3.py
	```
* **Note:**

  -  This script demonstrates basic error handling (printing error messages). You might want to consider implementing logging for more detailed tracking.
 
4. **example_4.py**

* **Description:** This script demonstrates creating a scatter plot with 50 random data points using Matplotlib and NumPy. It visualizes the points with green square markers and includes labels, a title, and a legend.

* **Relevant Documentation:**
  - Matplotlib: [https://matplotlib.org/](https://matplotlib.org/)
  - NumPy: [https://numpy.org/doc/](https://numpy.org/doc/)

* **Function:**
  - `plot_random_scatter()`: Generates a scatter plot with 50 random points, handling potential errors with specific exception handling (e.g., value format, data type mismatches).

* **How to Run:**

```bash
python ./matplotlib/example_4.py
```
* **Note:**

  -   This script demonstrates basic error handling (printing error messages). You might want to consider implementing logging for more detailed tracking.

5. **example_5.py**

* **Description:** This script demonstrates creating a histogram with Matplotlib and NumPy. It generates 1000 random data points and visualizes their distribution using a histogram with 30 bins. The histogram is colored sky blue with black edges for better clarity. Labels and a title are included for improved readability.

* **Relevant Documentation:**
  - Matplotlib: [https://matplotlib.org/](https://matplotlib.org/)
  - NumPy: [https://numpy.org/doc/](https://numpy.org/doc/)

* **Function:**
  - `plot_random_data_histogram()`: Generates a histogram for 1000 random data points, handling potential errors with specific exception handling (e.g., value format, data type mismatches).

* **How to Run:**

```bash
python ./matplotlib/example_5.py
```

* **Note:**

  -   This script demonstrates basic error handling (printing error messages). You might want to consider implementing logging for more detailed tracking.
 
6. **example_6.py**

* **Description:** This script demonstrates creating a pie chart with Matplotlib to visualize data for multiple categories. It includes sample data for five categories with their corresponding sizes and colors. The pie chart displays percentages with one decimal place and uses a starting angle of 90 degrees.

* **Relevant Documentation:**
  - Matplotlib: [https://matplotlib.org/](https://matplotlib.org/)

* **Function:**
  - `plot_category_pie_chart()`: Generates a pie chart for category data, handling potential errors with specific exception handling (e.g., value format, data type mismatches).

* **How to Run:**

```bash
python ./matplotlib/example_6.py
```

* **Note:**

  -   This script demonstrates basic error handling (printing error messages). You might want to consider implementing logging for more detailed tracking.
 
7. **example_7.py**

* **Description:** This script demonstrates creating a box plot with Matplotlib for data categorized into four groups. It utilizes NumPy for random data generation and assigns distinct light-colored fills to each category's box in the plot. The x-axis is labeled with descriptive category names, and the plot is titled for clarity.

* **Relevant Documentation:**
  - Matplotlib: [https://matplotlib.org/](https://matplotlib.org/)
  - NumPy: [https://numpy.org/doc/](https://numpy.org/doc/)

* **Function:**
  - `plot_categorical_boxplot()`: Generates a box plot for categorical data, handling potential errors with specific exception handling (e.g., value format, data type mismatches).

* **How to Run:**

```bash
python ./matplotlib/example_7.py
```
* **Note:** 
  -   This script demonstrates basic error handling (printing error messages). You might want to consider implementing logging for more detailed tracking.


8. **example_8.py**

* **Description:** This script demonstrates creating a combined visualization for a sample dataset with categorical data. It generates line, bar, scatter, and pie charts using Matplotlib and NumPy to represent values for four categories. The script saves the combined charts as a single image file named "combined_charts.png" and adjusts spacing for better readability using `tight_layout()`.

* **Relevant Documentation:**
  - Matplotlib: [https://matplotlib.org/](https://matplotlib.org/)
  - NumPy: [https://numpy.org/doc/](https://numpy.org/doc/)

* **Function:**
  - `plot_categorical_data_combos()`: Generates a combination of line, bar, scatter, and pie charts for categorical data, handling potential errors with specific exception handling (e.g., value format, data type mismatches).

* **How to Run:**

```bash
python ./matplotlib/example_8.py
```
* **Note:** 
  -  This script demonstrates basic error handling (printing error messages). You might want to consider implementing logging for more detailed tracking.

9. **example_9.py**

* **Description:** This script demonstrates creating stacked and grouped bar charts using Matplotlib and NumPy for the same sample data. It visualizes how data is segmented and displayed differently in these two chart types. The script saves the combined charts as a single image file named "stacked_grouped_bar_charts.png" and adjusts spacing for better readability using `tight_layout()`.

* **Relevant Documentation:**
  - Matplotlib: [https://matplotlib.org/](https://matplotlib.org/)
  - NumPy: [https://numpy.org/doc/](https://numpy.org/doc/)

* **Function:**
  - `plot_stacked_and_grouped_bar_charts()`: Generates stacked and grouped bar charts for the same data, handling potential errors with specific exception handling (e.g., value format, data type mismatches).

* **How to Run:**

```bash
python ./matplotlib/example_9.py
```
* **Note:** 
  -  This script demonstrates basic error handling (printing error messages). You might want to consider implementing logging for more detailed tracking.

10. **example_10.py**

* **Description:** This script demonstrates creating a visualization with multiple line charts using Matplotlib and NumPy. It generates six lines representing different mathematical functions (sin, cos, tan, etc.) and assigns distinct colors and styles to each line. The script saves the plot as a single image file named "multiple_line_charts.png".

* **Relevant Documentation:**
  - Matplotlib: [https://matplotlib.org/](https://matplotlib.org/)
  - NumPy: [https://numpy.org/doc/](https://numpy.org/doc/)

* **Function:**
  - `plot_multiple_line_charts()`: Generates a plot with multiple line charts for various datasets, handling potential errors with specific exception handling (e.g., value format, data type mismatches).

* **How to Run:**

```bash
python ./matplotlib/example_10.py
```

* **Note:** 
  -  This script demonstrates basic error handling (printing error messages). You might want to consider implementing logging for more detailed tracking.


**Further Learning:**

- For a comprehensive guide to Matplotlib, refer to the official documentation:

  [https://matplotlib.org/stable/](https://matplotlib.org/stable/)

- Explore the vast online Matplotlib tutorials and resources for further practice.

**Contact:**

For any feedback or questions about these scripts, feel free to reach out to Satya Prakash Nigam at spnigam25@yahoo.com.
 
**Note:**
 
 

 