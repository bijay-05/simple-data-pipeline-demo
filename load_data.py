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
    schema = connection_keys["schema"]

    # Establish the connection
    try:
        connection_obj = snow.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema,
            client_session_keep_alive=True
        )
    except:
        raise Exception("connection object does not exist")

    return connection_obj

def load_data(connection, last_date:str) -> str:
    """
    This function takes connection object and last_date (as date when
    the pipeline last ran) as input and performs the loading of data into target database,
     finally returns the status of function completion
    """

    #read data from CSV (extract_data.py)
    df = pd.read_csv(f"./sales_table_after_{last_date}_file.csv",delimiter=',', header=0) # header=0 means first line as columns
    
    # get the cursor
    cursor = connection.cursor()
    try:
        cursor.execute("USE DATABASE SALES_ANALYTICS_DWH")
        cursor.execute("USE SCHEMA SALES_ANALYTICS_DWH.SALES")
        cursor.execute("""create table IF NOT EXISTS sales_table(sale_id INT NOT NULL, \
                       date_time TIMESTAMP NOT NULL, cust_id INT NOT NULL, product_id INT NOT NULL, \
                       quantity INT NOT NULL, unit_price NUMBER(4,0) NOT NULL, total_price NUMBER(6,0) NOT NULL)""")

        status, nchunks, nrows,_ = write_pandas(connection, df, "sales_table", quote_identifiers=False) # _ is the output of COPY cmd being executed in database
        print(f"Status of the function: {status}\n number of rows inserted: {nrows}")
    finally:
        connection.close()
    
    return "Data Loading Status: Completed"

    

