Automated Scientific Data Processing Pipeline
A simple Python ETL (Extract, Transform, Load) pipeline that reads data from multiple sources, cleans and processes it, and loads it into a MySQL database.

Project Description:
This project automates the process of:

Extracting data from CSV, Excel, and JSON files

Transforming the data by cleaning, filtering, and merging it

Loading the processed data into a MySQL database

Built with Python, Pandas, and MySQL.
What the Code Does
Extract Phase
Reads sales data from CSV file

Reads customer data from Excel file

Reads web analytics from JSON file

Transform Phase
Cleans up dates and removes missing values

Filters only active customers

Merges sales and customer data

Load Phase
Saves the processed data to MySQL database table sales_warehouse
