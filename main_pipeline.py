import argparse

from extract_data import get_conn_str,get_data,get_keys
from load_data import get_connection,load_data

# This is our main script that runs the different functions to 
# complete the flow of data from production OLTP database to
# OLAP data warehouse in Snowflake.

def main(source_keys: str, target_keys: str, datetime: str):
    """
    This is main function which incorporates all the other 
    helper functions from extract and load scripts, and completes 
    the flow of data pipeline.
    """
    database_keys = get_keys(filename=source_keys)
    connection_str = get_conn_str(keys=database_keys)
    extraction_status = get_data(conn_string=connection_str,table_name="sales_table",datetime=datetime)
    print(extraction_status)
    print("\n\n\n")

    target_db_keys = get_keys(filename=target_keys)
    connection = get_connection(connection_keys=target_db_keys)
    loading_status = load_data(connection=connection)
    print(loading_status)





if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source_keys",
        help="the filename with credentials for connecting to db"
    )

    parser.add_argument(
        "--target_keys",
        help="the filename with credentials for connecting to db"
    )

    parser.add_argument(
        "--datetime",
        help="get the data of the specified date of the day"
    )

    args = parser.parse_args()

    main(source_keys=args.source_keys, target_keys=args.target_keys, datetime=args.datetime)
