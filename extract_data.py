from configparser import ConfigParser
import polars as pl

def get_keys(filename='database.ini', section='postgresql'):
    """
    This function takes a file and section (in file)
    as input and returns a dictionary with creds for
    connecting to a database server
    """
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db_keys = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_keys[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db_keys

def get_connection(keys : dict) -> str :
    """
    This function takes a dictionary of values (keys)
    for making connection to a database and returns a
    connection string (for polars.read_database function)
    """
    return f"postgres://{keys[user]}:{keys[password]}@{keys[host]}:{keys[port]}/{keys[database]}"

def get_data(conn_string: str, table_name: str, output_format: int):
    """
    This function takes connection_string, table_name and
    output_format as inputs and outputs the success of the function
    output_format is integer value indicating 0: CSV and 1: PARQUET
    """
    query = "SELECT * FROM public"+table_name
    
    # read the data from database into dataframe
    dataframe = pl.read_database(connection_uri=conn_string, query=query)

    # output the data from database into file
    if output_format == 0:
        dataframe.write_csv(file=f"{table_name}_file.csv", has_header=True)
        return dataframe
    elif output_format == 1:
        dataframe.write_parquet(f"{table_name}_file.parquet")
        return dataframe
    else:
        print("Choose one of the output formats available")

