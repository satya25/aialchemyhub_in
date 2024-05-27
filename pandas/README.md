**Pandas Examples**

This folder provides a collection of 10 Python scripts demonstrating core functionalities of the Pandas library for data analysis. These scripts are designed to help you learn and practice various data manipulation and exploration techniques.

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

3. **Running the Scripts:** Navigate to the `./pandas` folder in your terminal and execute a script using:

   ```bash
   python <script_name>.py
   ```

   Replace `<script_name>` with the actual filename of the script you want to run (e.g., `python example_1.py`).

**Examples:**

This folder includes 10 example scripts covering various Pandas operations. Here are some key functionalities demonstrated:

- Loading data from CSV files
- Exploring data with descriptive statistics
- Data cleaning and manipulation
- Data visualization using Matplotlib (if applicable)
 
**Examples:**

This folder includes 10 example scripts covering various Pandas operations. Here are some key functionalities demonstrated:

- Loading data from CSV files
- Exploring data with descriptive statistics
- Data cleaning and manipulation
- Data visualization using Matplotlib (if applicable)

1. **example_1.py**

   * **Description:** This script demonstrates how to load a CSV dataset (Titanic passenger data) into a Pandas DataFrame, explore its basic information, and display descriptive statistics.

   * **Relevant Documentation:**
     - Loading Data from CSV files: [https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
     - Exploring DataFrames: [https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)
     - Descriptive Statistics: [https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)


2. **example_2.py**

   * **Description:** This script showcases various techniques for handling missing data and performing basic data manipulation on a Pandas DataFrame.

   * **Relevant Documentation:**
     - Handling Missing Data: https://pandas.pydata.org/docs/user_guide/missing_data.html
     - Selecting Data: https://pandas.pydata.org/pandas-docs/version/0.14.1/
     - Filtering Data: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html
     - Filling Missing Values: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.fillna.html

3. **example_3.py**

   * **Description:** This script demonstrates creating a Pandas DataFrame from scratch, manipulating data (adding columns, updating values), filtering data based on a condition, sorting the DataFrame by a specific column, and performing group-by operations to calculate average salary by city.

   * **Relevant Documentation:**
     - Creating DataFrames: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
     - Selecting Data: https://pandas.pydata.org/pandas-docs/version/0.14.1/
     - Filtering Data: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html
     - Sorting Data: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html
     - GroupBy Operations: https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.GroupBy.html
	 
4. **example_4.py**

   * **Description:** This script provides an introduction to merging and concatenating DataFrames in Pandas. It creates two DataFrames, concatenates them vertically, and then merges them based on a common column.

   * **Relevant Documentation:**
     - Concatenating DataFrames: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html
     - Merging DataFrames: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.merge.html

5. **example_5.py**

   * **Description:** This script demonstrates an introduction to column grouping and finding minimum, maximum, and mean column values. It creates a DataFrame with weather data (city, temperature, and humidity), groups data by city, and calculates the mean temperature and maximum humidity for each city.

   * **Relevant Documentation:**
     - GroupBy Operations: https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.GroupBy.html
     - Aggregation Functions: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.DataFrameGroupBy.agg.html

6. **example_6.py**

   * **Description:** This script demonstrates working with DataFrames representing city information. It creates two DataFrames, one with population data and another with area data, then performs both a merge and concatenate operation. The result is two new DataFrames: one with merged information for cities present in both DataFrames (inner join), and another with the rows of both DataFrames appended vertically (concatenation).

   * **Relevant Documentation:**
     - Merging DataFrames: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html
     - Concatenating DataFrames: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html
 
7. **example_7.py**

   * **Description:** This script demonstrates multi-level grouping with Pandas DataFrames. It creates a DataFrame with city-wise population data for different years. The script then groups the data by both 'City' and 'Year' and calculates the sum of the population for each city across the years. The result is a new DataFrame with aggregated population information.

   * **Relevant Documentation:**
     - GroupBy Operations: https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.GroupBy.html

8. **example_8.py**

   * **Description:** This script demonstrates working with DataFrames in Pandas. It creates two DataFrames, performs an inner merge based on a common column ('ID'), and showcases both vertical and horizontal concatenation of the DataFrames. The result is a merged DataFrame with combined information and two new DataFrames, one with vertically stacked rows and another with horizontally concatenated columns.

   * **Relevant Documentation:**
     - Merging DataFrames: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html
     - Concatenating DataFrames: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html
 

9. **example_9.py**

   * **Description:** This script demonstrates working with datetime data in Pandas. It creates a DataFrame with temperature data recorded on specific dates. The script converts the date strings to datetime format, extracts day, month, and year as separate columns, and then resamples the data to calculate the average temperature for each month.

   * **Relevant Documentation:**
     - Working with datetime data: https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html
     - Resampling data: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html
 
   
10. **example_10.py**

   * **Description:** This script demonstrates creating a pivot table with Pandas. It creates a DataFrame with weather data (city, temperature, and humidity). The script uses the `pivot_table` function to calculate the mean temperature and humidity for each city, providing a concise summary of average weather conditions across different locations.

   * **Relevant Documentation:**
     - Pivot Tables: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html


**Further Learning:**

- For a comprehensive guide to Pandas, refer to the official documentation:

  [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)

- Explore the vast online Pandas tutorials and resources for further practice.

**Contact:**

For any feedback or questions about these scripts, feel free to reach out to Satya Prakash Nigam at spnigam25@yahoo.com.
 
**Note:**
 