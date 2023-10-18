import pyodbc
import requests

# Define your SQL Server connection parameters
server = '172.31.151.88'
database = 'DesSy'
username = 'dessyuser'
password = 'PwdDessyU5er@2022'

# Connect to SQL Server
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(connection_string)

# Define the stored procedure name and parameters
stored_proc_name = 'sp_SERVPERF_FirstVisitTime_View'
param1 = '1'
param2 = '2023-07-28'
param3 = '2023-08-29'

# Create a cursor
cursor = conn.cursor()

# Execute the stored procedure
cursor.execute(f"EXEC {stored_proc_name} ?, ?, ?", (param1, param2, param3))

# Fetch and display the results
for row in cursor.fetchall():
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()