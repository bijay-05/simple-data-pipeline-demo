import snowflake.connector as snow
from snowflake.connector.pandas_tools import write_pandas
import pandas as pd


def get_connection(connection_keys: dict):
    """
    This function takes dictionary of keys as input 
    and returns a connection object to snowflake datawarehouse
    """
    account = connection_keys["account"]
    user = connection_keys["user"]
    password = connection_keys["password"]
    warehouse = connection_keys["warehouse"]
    database = connection_keys["database"]
    table = connection_keys["table"]

    # Establish the connection
    connection = snow.connect(
        user=user,
        password=password,
        account=account,
        database=database
    )

    return connection

def load_data(connection: snow.connect(), last_date:str) -> str:
    """
    This function takes connection object  as 
    input and performs the loading of data into warehouse,
     finally returns the status of function completion
    """

    #read data from CSV (extract_data.py)
    df = pd.read_csv("./sales_table_after_{last_date}_file.csv",delimiter=',', header=0) # header=0 means first line as columns
    
    # get the cursor
    cursor = connection.cursor()
    try:
        cursor.execute("USE DATABASE daily_sales")
        cursor.execute(f"create table IF NOT EXISTS sales_table_after_{last_date}")
        write_pandas(connection,df,f"sales_table_after_{last_date}")
        result = cursor.execute(f"select count(*) from sales_table_after_{last_date}").fetchone()
        print("Number of rows in table: ",result)
    finally:
        connection.close()
    
    return "Data Loading Status: Completed"

    

