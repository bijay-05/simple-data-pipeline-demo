from snowflake.snowpark import Session
import polars as pl


def get_connection(connection_keys: dict):
    """
    This function takes dictionary of keys as input 
    and returns a connection object to snowflake datawarehouse
    """

    # Establish the connection
    new_session = Session.builder.configs(connection_parameters).create()  

    return new_session

def load_data(session: Session):
    """
    This function takes session object  as 
    input and performs the loading of data into warehouse,
     finally returns the status of function completion
    """
    session.create(df)
    return "Data Loading Status: Completed"

