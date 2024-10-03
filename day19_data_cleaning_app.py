# This is a data cleaning application 

"""
Please create a python application that can take datasets and clean the data
- It should ask for datasets path and name
- it should check number of duplicats and remove all the duplicates 
- it should keep a copy of all the duplicates
- it should check for missing values 
- if any column that is numeric it should replace nulls with mean else it should drop that rows
- at end it should save the data as clean data and also return 
- duplicates records, clean_data 
"""

# importing dependencies
import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os
import random

# data_path = 'sales.xlsx'
# data_name = 'jan_sales'


def data_cleaning_master(data_path, data_name):

    print("Thank you for giving the details!")
    
    # random.randint(1, 4)  #generating random number
    
    sec = random.randint(1, 4)
    # print delay message
    print(f"Please wait for {sec}seconds! Checking file path")
    time.sleep(sec)
    
    # checking if the path exists
    if not os.path.exists(data_path):
        print("Incorrect path! Try again with correct path")
        return
    else:
        # checking the file type
        if data_path.endswith('.csv'):
            print('Dataset is csv!')
            data = pd.read_csv(data_path, encoding_errors='ignore')
            
            
        elif data_path.endswith('.xlsx'):
            print('Dataset is excel file!')
            data = pd.read_excel(data_path)
            
        else:
            print("Unkown file type")
            return
            
    # print delay message
    sec = random.randint(1, 4)
    print(f"Please wait for {sec}seconds! Checking total columns and rows")
    time.sleep(sec)
            
    # showing number of records
    print(f"Dataset contain total rows: {data.shape[0]} \n Total Columns: {data.shape[1]}")


    # start cleaning

    # print delay message
    sec = random.randint(1, 4)
    print(f"Please wait for {sec}seconds! Checking total duplicates")
    time.sleep(sec)
    
    # checking duplicates
    duplicates = data.duplicated()
    total_duplicate = data.duplicated().sum()

    print(f"Datasets has total duplicates records :{total_duplicate}")


    # print delay message
    sec = random.randint(1, 4)
    print(f"Please wait for {sec}seconds! Saving total duplicates rows")
    time.sleep(sec)


    # saving the duplicates 
    if total_duplicate > 0:
        deplicate_records = data[duplicates]
        deplicate_records.to_csv(f'{data_name}_duplicates.csv', index=None)

    # deleting duplicates
    df = data.drop_duplicates()


    # print delay message
    sec = random.randint(1, 10)
    print(f"Please wait for {sec}seconds! Checking for missing values")
    time.sleep(sec)

    # find missing values
    total_missing_value = df.isnull().sum().sum()
    missing_value_by_colums = df.isnull().sum()

    print(f"Dataset has Total missing value: {total_missing_value}")
    print(f"Dataset contain missing value by columns \n{missing_value_by_colums}")


    # dealing with missing values
    # fillna -- int and float
    # dropna -- any object

    # print delay message
    sec = random.randint(1, 6)
    print(f"Please wait for {sec}seconds! Cleaning datasets")
    time.sleep(sec)

    columns = df.columns

    for col in columns:
        # filling mean for numeric columns all rows
        if df[col].dtype in (float, int):
            df[col] = df[col].fillna(df[col].mean())
            
        else:
            # dropping all rows with missing records for non number col
            df.dropna(subset=col, inplace=True)
            
        
    # print delay message
    sec = random.randint(1, 5)
    print(f"Please wait for {sec}seconds! Exporting datasets")
    time.sleep(sec)

    # data is cleaned
    print(f"Congrats! Dataset is cleaned! \nNumber of Rows: {df.shape[0]} Number of columns: {df.shape[1]}")

    # saving the clean dataset
    df.to_csv(f'{data_name}_Clean_data.csv', index=None)
    print("Dataset is saved!")

if __name__ == "__main__":
    
    print("Welcome to Data Cleaning Master!")
    # ask path and file name
    data_path = input("Please enter dataset path :")
    data_name = input("Please enter dataset name :")
    
    # calling the function
    data_cleaning_master(data_path, data_name)



