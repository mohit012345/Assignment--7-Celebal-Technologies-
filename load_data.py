import os
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from datetime import datetime

# Encode the password correctly to avoid @ symbol breaking the connection string
password = quote_plus("Mohit@123")

# Create connection to SQL Server (Assignment_7 DB)
conn_str = f"mssql+pyodbc://sa:{password}@localhost/Assignment_7?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(conn_str)

# Path to your data lake folder
folder_path = 'D:/Assignment-7-Celebal/data_lake'

try:
    # Truncate all destination tables first
    with engine.begin() as conn:
        conn.execute("TRUNCATE TABLE CUST_MSTR")
        conn.execute("TRUNCATE TABLE master_child")
        conn.execute("TRUNCATE TABLE H_ECOM_Orders")
    print(" Tables truncated successfully.")

    # Read and load each CSV file based on its prefix
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if file.startswith("CUST_MSTR_"):
            df = pd.read_csv(file_path)
            date_str = file.replace("CUST_MSTR_", "").replace(".csv", "")
            date_obj = datetime.strptime(date_str, "%Y%m%d")
            df['Date'] = date_obj.strftime("%Y-%m-%d")
            df.to_sql("CUST_MSTR", engine, if_exists='append', index=False)
            print(f" Loaded: {file} into CUST_MSTR")

        elif file.startswith("master_child_export-"):
            df = pd.read_csv(file_path)
            date_str = file.replace("master_child_export-", "").replace(".csv", "")
            date_obj = datetime.strptime(date_str, "%Y%m%d")
            df['Date'] = date_obj.strftime("%Y-%m-%d")
            df['DateKey'] = int(date_obj.strftime("%Y%m%d"))
            df.to_sql("master_child", engine, if_exists='append', index=False)
            print(f"Loaded: {file} into master_child")

        elif file.startswith("H_ECOM_ORDER"):
            df = pd.read_csv(file_path)
            df.to_sql("H_ECOM_Orders", engine, if_exists='append', index=False)
            print(f" Loaded: {file} into H_ECOM_Orders")

except Exception as e:
    print(f" Error occurred: {e}")
