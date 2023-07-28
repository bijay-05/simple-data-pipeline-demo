import argparse
from extract_data import get_conn_str,get_data,get_keys
from load_data import get_connection,load_data

# This is our main script that runs the different functions to 
# complete the flow of data from production OLTP database to
# OLAP data warehouse in Snowflake.

def main(source_keys: str, target_keys: str, last_date: str) -> str:
    """
    This is main function which incorporates all the other 
    helper functions from extract and load scripts, and completes 
    the flow of data pipeline.
    """
    database_keys = get_keys(filename=source_keys)
    connection_str = get_conn_str(keys=database_keys)
    extraction_status = get_data(conn_string=connection_str, table_name="sales_table", output_format=0, last_date=last_date)
    print(extraction_status)
    print("\n\n\n")

    target_db_keys = get_keys(filename=target_keys)
    connection_obj = get_connection(connection_keys=target_db_keys)

    if connection_obj is None:
        print("Connection is None")
        return "shit happens !!!"
    else:
        print(type(connection_obj))
    
    loading_status = load_data(connection=connection_obj, last_date=last_date)
    print(loading_status)

    return "Pipeline run completed"





if __name__ == '__main__':

    parser = argparse.ArgumentParser() # the argparse treats all arguments as strings unless specified
    parser.add_argument(
        "--source_keys",
        help="the filename with credentials for connecting to db"
    )

    parser.add_argument(
        "--target_keys",
        help="the filename with credentials for connecting to db"
    )

    parser.add_argument(
        "--lastdate",
        help="date when the pipeline ran last time"
    )

    args = parser.parse_args()

    main(source_keys=args.source_keys, target_keys=args.target_keys, last_date=args.lastdate)
