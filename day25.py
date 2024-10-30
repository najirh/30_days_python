# Required Libraries
import pandas as pd
import mysql.connector  # MySQL connection
import psycopg2  # PostgreSQL connection
from sqlalchemy import create_engine  # SQLAlchemy for connecting Pandas and databases

# PostgreSQL Configuration
psql_config = {
    'host': 'localhost',
    'port': 5432,
    'user': 'postgres',
    'password': 'x0000',
    'database': 'demo'
}

# Establishing PostgreSQL Connection
try:
    conn = psycopg2.connect(**psql_config)
    print("Connected to PostgreSQL!")
except psycopg2.Error as e:
    print(f"PostgreSQL Connection Failed: {e}")
    exit(1)  # Exit if connection fails

# Create a Cursor for executing SQL queries
cursor = conn.cursor()

# SQL Query to Create 'walmart' Table if not exists
create_table_query = """
    CREATE TABLE IF NOT EXISTS walmart (
        invoice_id INT,
        branch TEXT,
        city TEXT,
        gender TEXT,
        total FLOAT,
        date DATE,
        payment_method TEXT,
        rating FLOAT
    );
"""

try:
    cursor.execute(create_table_query)
    conn.commit()  # Save changes
    print("Walmart Table created successfully.")
except psycopg2.Error as e:
    print(f"Error creating table: {e}")

# Load Walmart Data from CSV into Pandas DataFrame
df = pd.read_csv('walmart.csv')
print(df.head())  # Display the first few rows

# Creating SQLAlchemy Engine to connect with PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:x0000@localhost:5432/demo')

# Insert Data from DataFrame to PostgreSQL Table
try:
    df.to_sql(name='walmart', con=engine, if_exists='append', index=False)
    print("Data inserted into 'walmart' table.")
except Exception as e:
    print(f"Error inserting data: {e}")

# Query Walmart Data: Branch-wise Total Sales
query = """
    SELECT 
        branch, 
        COUNT(*) AS total_sale
    FROM walmart
    GROUP BY branch;
"""

# Execute the Query and Load the Result into a DataFrame
try:
    df_result = pd.read_sql(query, con=engine)
    print(df_result.head())  # Display the query result
except Exception as e:
    print(f"Error fetching data: {e}")

# Insert Product Data into 'products' Table
create_products_table = """
    CREATE TABLE IF NOT EXISTS products (
        id INT PRIMARY KEY,
        product_name TEXT,
        price INT
    );
"""

try:
    cursor.execute(create_products_table)
    print("Products Table created successfully.")
except psycopg2.Error as e:
    print(f"Error creating 'products' table: {e}")

# Sample Data for Insertion
product_data = [
    (101, 'iPhone 15', 899),
    (102, 'iPhone 14', 1299),
    (103, 'iPhone 13', 999)
]

insert_product_query = """
    INSERT INTO products (id, product_name, price)
    VALUES (%s, %s, %s);
"""

try:
    cursor.executemany(insert_product_query, product_data)
    conn.commit()  # Save changes
    print("Product data inserted successfully.")
except psycopg2.Error as e:
    print(f"Error inserting product data: {e}")

# Fetch and Display Product Data
try:
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except psycopg2.Error as e:
    print(f"Error fetching product data: {e}")

# Cleanup: Close Cursor and Connection
cursor.close()
conn.close()
print("Database connection closed.")
