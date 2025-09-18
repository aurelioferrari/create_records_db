# Online Store - Customer Import

This repository contains a Python script to import customer data from an Excel file into a SQLite database.

## Repository Structure

- `Clientes.xlsx` : Excel file containing customer data with the following columns:
  1. Name
  2. Email
  3. State
- `import_clientes.py` : Python script that reads the Excel file and inserts the data into the `Clientes` table of the SQLite database.

## Requirements

- Python 3.x
- Python libraries:
  - pandas
  - openpyxl
  - sqlite3 (included in standard Python)

Install the required libraries with:

```bash
pip install pandas openpyxl
Usage

Make sure the file Clientes.xlsx is in the repository at the same path specified in the script.

Run the Python script:

python import_clientes.py


The script will:

Read the customer data from the Excel file (Clientes.xlsx).

Insert each customer into the Clientes table of the SQLite database located at:
C:/Users/lelin/OneDrive/Documents/dbs/loja_online.db

Notes

The script uses a single commit() at the end for better performance.

Make sure the SQLite database is not open in another program when running the script to avoid the database is locked error.

If you want to clear the table before inserting new data, run:

DELETE FROM Clientes;


