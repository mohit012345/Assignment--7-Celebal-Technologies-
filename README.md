# 🚀 Assignment 7 – Automated CSV Ingestion from Data Lake to SQL Server

This project is a Python-based automation solution for ingesting and transforming structured CSV files from a simulated **data lake** environment into an **SQL Server** database using a **truncate-and-load** strategy.

---

## 📚 Objective

To process and load different types of CSV files into their respective SQL Server tables with specific transformation rules based on file naming conventions.

---

## 📂 Input File Types & Processing Rules

All CSV files are stored in the `data_lake/` directory and follow a consistent naming pattern. Below are the details for each file type:

| File Example                          | Description                            | Target Table       | Transformations Applied |
|--------------------------------------|----------------------------------------|--------------------|--------------------------|
| `CUST_MSTR_20191112.csv`             | Customer Master data with date info    | `CUST_MSTR`        | ➕ Add `Date` column     |
| `master_child_export-20191112.csv`   | Master-child relation data             | `master_child`     | ➕ Add `Date`, `DateKey` |
| `H_ECOM_ORDER.csv`                   | E-commerce Orders                      | `H_ECOM_Orders`    | 🚫 No changes            |

---

## 🛠️ Data Transformation Details

### 1️⃣ `CUST_MSTR_<YYYYMMDD>.csv`
- Adds a `Date` column derived from the filename.
- Format: `YYYY-MM-DD` (e.g., `2019-11-12`).
- Loaded into: **`CUST_MSTR`**.

### 2️⃣ `master_child_export-<YYYYMMDD>.csv`
- Adds two columns:
  - `Date` ➝ `YYYY-MM-DD`
  - `DateKey` ➝ `YYYYMMDD`
- Loaded into: **`master_child`**.

### 3️⃣ `H_ECOM_ORDER.csv`
- Loaded **as-is** with no transformation.
- Loaded into: **`H_ECOM_Orders`**.

---

## 🔁 Load Strategy

- **Truncate and Load**:  
  Before each run, all three target tables are truncated to ensure clean, daily-refreshed data loads.

---

## 💻 Technologies Used

- `Python 3.x`
- `pandas`
- `SQLAlchemy`
- `pyodbc`
- `SQL Server`

---

## 🧪 How to Run the Project

### ✅ Prerequisites

- Python 3.x installed
- Required Python packages:
  ```bash
  pip install pandas sqlalchemy pyodbc


🗂️ Project Structure
Assignment-7-Celebal/
│
├── data_lake/
│   ├── CUST_MSTR_20191112.csv
│   ├── master_child_export-20191112.csv
│   └── H_ECOM_ORDER.csv
│
├── load_data.py
└── README.md

👨‍💻 Developed by
Mohit Choudhary
Intern @ Celebal Technologies
🗓️ July 2025


📎 License
This project is submitted as a part of an internship assignment and is intended for educational and demonstration purposes only.
