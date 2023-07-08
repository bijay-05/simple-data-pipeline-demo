import snowflake.connector
import polars as pl

from extract_data import get_keys

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
    connection = snowflake.connector.connect(
        user=user,
        password=password,
        account=account
        warehouse=warehouse,
        database=database
    )

    return connection

def load_data(connection):
    """
    This function takes connection object to snowflake as 
    input and performs the loading of data into warehouse,
     finally returns the status of function completion
    """

