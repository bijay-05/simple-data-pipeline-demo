from configparser import ConfigParser


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
    return "postgres://{keys[user]}:{keys[password]}@{keys[host]}:{keys[port]}/{keys[database]}"