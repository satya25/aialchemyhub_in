# Flask CRUD Application

This is a Flask web application for managing records with Create, Read, Update, and Delete (CRUD) functionalities. The application uses a MySQL database and includes features for data generation and interactive dashboards.

## Features

- **Record Management:** Add, view, update, and delete records.
- **Data Generation:** Generate and insert multiple records quickly with the data generator tool.
- **Interactive Dashboards:** Visualize data with dynamic bar charts, pie charts, histograms, and scatter plots.
- **Responsive Design:** The application works seamlessly across desktop and mobile devices.
- **Easy Integration:** Modular and customizable codebase for easy integration into existing projects.

## Folder Structure

.
|-- app.py
|-- database.py
|-- database_schema.sql
|-- reports
|-- requirements.txt
|-- static
| -- images | |-- resized_schema.png | -- schema.png
-- templates |-- add-record.html |-- dashboard.html |-- dashboard2.html |-- dashboard3.html |-- dashboard4.html |-- data-generator.html |-- delete-record.html |-- footer.html |-- index.html |-- show-records.html |-- top-nav-bar.html -- update-record.html
 
## Prerequisites

- Python 3.x
- MySQL Server

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    - Ensure MySQL server is running.
    - Run the SQL script to create the database and table:

    ```sh
    mysql -u root -p < database_schema.sql
    ```

5. **Configure the database connection:**

    Update the `create_engine` line in `app.py` with your database credentials if necessary:

    ```python
    engine = create_engine('mysql://root:@localhost/your_database')
    ```

## Usage

1. **Run the application:**

    ```sh
    python app.py
    ```

2. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:5000`.

## Screenshots

### Home Page
![Home Page](static/images/home_page.png)

### Data Generator
![Data Generator](static/images/data_generator.png)

### Dashboard
![Dashboard](static/images/dashboard.png)

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [Faker](https://faker.readthedocs.io/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Pillow](https://python-pillow.org/)

