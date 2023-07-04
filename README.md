# simple-data-pipeline-demo
This project incorporates a simple data pipeline to extract, transform and load the data using python and SQL.
In order to gain a working idea of data pipeline and to simply start the learning, we will try to keep things
 as simple as possible.

The Source: A PostgreSQL database (sales_database) is the source of our data pipeline. The database has a `sales_table`
, which keeps record of daily sales at the store. We have two databases ( primary and secondary inorder to simulate production
scenario )

We will connect to a secondary postgreSQL database in production. Here we will use a separate python scripts for extracting and loading the 
data. While data is in transition, it is kept in the memory of machine where python script is running & output as CSV file and after extraction 
is completed, then it is loaded into object storage such as **AWS S3** 


For extracting the data, we will use `polars.read_database()` function from **Polars**. This function accepts
a string `connection_uri` and an SQL query string