#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
This script is part of the aialchemyhub.in project 
(https://github.com/satya25/aialchemyhub_in).

Distributed under the MIT License (see LICENSE file for details).
"""

# ----------------------------------------------------------------------------
# File Name         :       app.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       June 01, 2024
# Last Update on    :       June 01, 2024
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       
#
# Installation      :       $ pip install -r ./requirements.txt
#                           
# ---------------------------------------------------------------------------
# 

from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_db_connection

from flask import jsonify
import time

from faker import Faker 

import io
import os
import sys
import base64
import matplotlib.pyplot as plt
import pandas as pd
 
import secrets
 
from sqlalchemy import create_engine, MetaData
from sqlalchemy_schemadisplay import create_schema_graph
from PIL import Image
 
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Generate random secret key
 
# Function to generate and resize the schema image
def generate_and_resize_schema_image():
    # Create a dummy engine
    dummy_engine = create_engine('sqlite://')

    # Create an SQLAlchemy engine
    engine = create_engine('mysql://root:@localhost/aialchemyhub_tut_1')

    # Create an empty MetaData object
    metadata = MetaData()

    # Reflect the database schema into the MetaData object
    metadata.reflect(bind=engine)

    # Create a schema graph
    graph = create_schema_graph(metadata=metadata, engine=dummy_engine)

    # Save the graph as an image file in the /images folder
    image_folder = 'static/images'
    os.makedirs(image_folder, exist_ok=True)
    image_filename = os.path.join(image_folder, 'schema.png')
    graph.write_png(image_filename)

    # Open the image with PIL
    image = Image.open(image_filename)

    # Resize the image to the desired width and height
    width_pixels = 400
    height_pixels = 300
    resized_image = image.resize((width_pixels, height_pixels))

    # Save the resized image
    resized_image_filename = os.path.join(image_folder, 'resized_schema.png')
    resized_image.save(resized_image_filename)

    return resized_image_filename
    
    
# Home route
@app.route('/')
def index():
    # Generate and get the resized schema image filename
    schema_image_path = generate_and_resize_schema_image()

    return render_template('index.html', schema_image_path=schema_image_path)
    
# Show records route
@app.route('/show-records')
def show_records():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM records')
    records = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('show-records.html', records=records)

# Add record route - Display form
@app.route('/add-record', methods=['GET', 'POST'])
def add_record():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        salary = request.form['salary']
        
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO records (name, age, city, salary) VALUES (%s, %s, %s, %s)',
                       (name, age, city, salary))
        connection.commit()
        cursor.close()
        connection.close()
        
        return redirect(url_for('show_records'))
    
    return render_template('add-record.html')
    
# Update record route - Display form
@app.route('/update-record/<int:id>', methods=['GET', 'POST'])
def update_record(id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM records WHERE id = %s', (id,))
    record = cursor.fetchone()
    cursor.close()
    
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        salary = request.form['salary']
        
        cursor = connection.cursor()
        cursor.execute('UPDATE records SET name = %s, age = %s, city = %s, salary = %s WHERE id = %s',
                       (name, age, city, salary, id))
        connection.commit()
        cursor.close()
        connection.close()
        
        return redirect(url_for('show_records'))
    
    connection.close()
    return render_template('update-record.html', record=record)

# Delete record route - Display confirmation
@app.route('/delete-record/<int:id>', methods=['GET', 'POST'])
def delete_record(id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM records WHERE id = %s', (id,))
    record = cursor.fetchone()
    cursor.close()

    if request.method == 'POST':
        if request.form.get('confirm') == 'yes':
            cursor = connection.cursor()
            cursor.execute('DELETE FROM records WHERE id = %s', (id,))
            connection.commit()
            cursor.close()
            connection.close()
            return redirect(url_for('show_records'))
        else:
            connection.close()
            return redirect(url_for('show_records'))
    
    connection.close()
    return render_template('delete-record.html', record=record)
 
# Dashboard route
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    # Fetch records from the database
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT age FROM records')
    records = cursor.fetchall()
    cursor.close()
    connection.close()

    # Process data into age groups
    df = pd.DataFrame(records)
    bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    labels = ['10-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']
    df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)
    age_group_counts = df['age_group'].value_counts().sort_index()

    # Create bar chart
    plt.figure(figsize=(10, 6))
    age_group_counts.plot(kind='bar', color='skyblue')
    plt.title('Number of Persons in Different Age Groups')
    plt.xlabel('Age Group')
    plt.ylabel('Number of Persons')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save plot to a string buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

    if request.method == 'POST':
        # Save the chart to the reports directory
        reports_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports')
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)
        chart_path = os.path.join(reports_dir, 'age_group_chart.png')
        with open(chart_path, 'wb') as f:
            f.write(buf.getvalue())

    buf.close()
    
    return render_template('dashboard.html', image_base64=image_base64)

@app.route('/dashboard2', methods=['GET', 'POST'])
def dashboard2():
    # Fetch records from the database
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT age FROM records')
    records = cursor.fetchall()
    cursor.close()
    connection.close()

    # Process data into age groups
    df = pd.DataFrame(records)
    bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    labels = ['10-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']
    df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)
    age_group_counts = df['age_group'].value_counts().sort_index()

    # Create pie chart
    plt.figure(figsize=(10, 6))
    age_group_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title('Distribution of Persons in Different Age Groups')
    plt.ylabel('')
    plt.tight_layout()

    # Save plot to a string buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

    if request.method == 'POST':
        # Save the chart to the reports directory
        reports_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports')
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)
        chart_path = os.path.join(reports_dir, 'age_group_pie_chart.png')
        with open(chart_path, 'wb') as f:
            f.write(buf.getvalue())

    buf.close()
    
    return render_template('dashboard2.html', image_base64=image_base64)


@app.route('/dashboard3', methods=['GET', 'POST'])
def dashboard3():
    # Fetch records from the database
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT age, salary FROM records')
    records = cursor.fetchall()
    cursor.close()
    connection.close()

    # Convert records to DataFrame
    df = pd.DataFrame(records)

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['age'], df['salary'], color='blue', alpha=0.5)
    plt.title('Age vs. Salary')
    plt.xlabel('Age')
    plt.ylabel('Salary')
    plt.grid(True)
    plt.tight_layout()

    # Save plot to a string buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

    # Check if the request method is POST (i.e., form submission)
    if request.method == 'POST':
        # Save the chart to the reports directory
        reports_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports')
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)
        chart_path = os.path.join(reports_dir, 'scatter_plot.png')
        with open(chart_path, 'wb') as f:
            f.write(buf.getvalue())  # Write chart data to the file

    buf.close()  # Close the buffer after writing to the file
    
    return render_template('dashboard3.html', image_base64=image_base64)

@app.route('/dashboard4', methods=['GET', 'POST'])
def dashboard4():
    # Fetch records from the database
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT age, salary FROM records')
    records = cursor.fetchall()
    cursor.close()
    connection.close()

    # Convert records to DataFrame
    df = pd.DataFrame(records)

    # Create histograms
    plt.figure(figsize=(12, 6))

    # Age histogram
    plt.subplot(1, 2, 1)
    plt.hist(df['age'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')

    # Salary histogram
    plt.subplot(1, 2, 2)
    plt.hist(df['salary'], bins=20, color='salmon', edgecolor='black')
    plt.title('Salary Distribution')
    plt.xlabel('Salary')
    plt.ylabel('Frequency')

    plt.tight_layout()

    # Save plot to a string buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

    # Check if the request method is POST (i.e., form submission)
    if request.method == 'POST':
        # Save the histograms to the reports directory
        reports_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports')
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)
        hist_path = os.path.join(reports_dir, 'histograms.png')
        with open(hist_path, 'wb') as f:
            f.write(buf.getvalue())  # Write chart data to the file

    return render_template('dashboard4.html', image_base64=image_base64)


# Route for the "Data Generator" page
# Route for the "Data Generator" page
@app.route('/data-generator', methods=['GET', 'POST'])
def data_generator():
    message = None  # Initialize message variable

    if request.method == 'POST':
        num_records = int(request.form['num_records'])
        generate_records(num_records)
        message = f'Successfully generated and inserted {num_records} records.'

    return render_template('data-generator.html', message=message)
    
# Function to generate and insert records into the database
def generate_records(num_records):
    fake = Faker()
    for _ in range(num_records):
        name = fake.name()
        age = fake.random_int(min=18, max=100)
        city = fake.city()
        salary = fake.random_int(min=10000, max=100000)
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO records (name, age, city, salary) VALUES (%s, %s, %s, %s)',
                       (name, age, city, salary))
        connection.commit()
        cursor.close()
        connection.close()
    return
 
# other (future) route definitions...

if __name__ == '__main__':
    app.run(debug=True)
 