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




if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--key_file",
        help="the filename with credentials for connecting to db"
    )

    parser.add_argument(
        "--section",
        help="the section in filename describing database engine"
    )

    parser.add_argument(
        "--datetime",
        help="get the data of the specified date of the day"
    )

    args = parser.parse_args()

    main(key_file=args.key_file, section=args.section, datetime=args.datetime)
