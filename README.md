# simple-data-pipeline-demo
This project incorporates a simple data pipeline to extract, transform and load the data using python and SQL.
In order to gain a working idea of data pipeline and to simply start the learning, we will try to keep things
 as simple as possible.

The Source: A PostgreSQL database (`store_db`) is the source of our data pipeline. The database has a `sales_table`
, which keeps record of daily sales at the store. We have two databases ( primary and secondary ) inorder to simulate production
scenario. The secondary database is a read-replica of primary database, with primary function to reduce the load of reading the
data from primary database. Besides this, secondary database also acts as a backup incase the primary goes down.

We will connect to a secondary postgreSQL database in production. Here we will use a separate python scripts for extracting and loading the data. While data is in transition, it is kept in the memory of machine where python script is running & output as CSV file and after extraction is completed, then it is loaded into cloud data warehouse **Snowflake**. Besides this, during extraction of the data we will perform few data checks to ensure data quality before writing data to warehouse.


For extracting the data, we will use `polars.read_database()` function from **Polars**. This function accepts
a string `connection_uri` and an SQL query string. We will filter the data in database through SQL query and 
only request the data since the pipeline ran last time by passing `last_date` argument to main script. And during
loading, we first load data into pandas dataframe, then the `write_pandas` function from `snowflake.connector` module which accepts connection object to snowflake,
 dataframe to be loaded into warehouse and table name as input, copies data into selected warehouse.