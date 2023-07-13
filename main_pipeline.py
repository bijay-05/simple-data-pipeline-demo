import argparse

from extract_data import get_conn_str,get_data,get_keys
from load_data import get_connection

# This is our main script that runs the different functions to 
# complete the flow of data from production OLTP database to
# OLAP data warehouse in Snowflake.

def main(key_file: str, section: str, datetime: str):
    """
    This is main function which incorporates all the other 
    helper functions from extract and load scripts, and completes 
    the flow of data pipeline.
    """
    database_keys = get_keys(filename=key_file, section=section)
    connection_str = get_conn_str(keys=database_keys)
    