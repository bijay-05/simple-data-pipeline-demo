# simple-data-pipeline-demo
This project incorporates a simple data pipeline to extract, transform and load the data using python and SQL.
In order to gain a working idea of data pipeline and to simply start the learning, we will try to keep things
 as simple as possible.

We will connect to a secondary postgreSQL database in production which contains daily sales data from a departmental
store's primary database in synchronization. Here we will use a separate python scripts for extracting and loading the 
data. While data is in transition, it is kept in the memory of machine where python script is running and after extraction 
is completed, then it is loaded into object storage such as **AWS S3** 
