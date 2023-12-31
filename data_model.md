### Here we will discuss about what is the schema of sales data 
### that we are going to get from the sales database

## SOME KEY CONSIDERATIONS
Let's say a customer purchases more than one item (i.e separate product_id's).
Here we will consider a sale of single kind of product (i.e same product_id) as
a single transaction in the sales_table. There is another products_table, which relates to 
sales_table through `product_id` field. We do have a customers table, for those
who have taken customer membership but non-member customers all have default
`cust_id` 0

What columns does a sales_table need to have ???

- sale_id : PRIMARY KEY, SERIAL, NOT NULL
- date_time: TIMESTAMP, DEFAULT NOW(), NOT NULL
- cust_id: INT , DEFAULT 0 (NON-MEMBER), NOT NULL
- product_id: INT, NOT NULL, FOREIGN KEY (products_table)
- quantity: INT, NOT NULL
- unit_price: FLOAT, NOT NULL
- total_price: FLOAT, NOT NULL

What columns does a products_table need to have ???
- product_id : PRIMARY KEY, NOT NULL, INT, FOREIGN KEY (sales_table)
- product_category : VARCHAR(20), NOT NULL
- product_name : VARCHAR(20), NOT NULL
- supplier_name : VARCHAR(20), NOT NULL

What columns does a customers_table need to have ??
- cust_id : PRIMARY KEY, SERIAL, NOT NULL, FOREIGN KEY (sales_table)
- cust_fname : VARCHAR, NOT NULL
- cust_lname : VARCHAR, NOT NULL
- cust_phone :INT, NOT NULL
- cust_address: VARCHAR, NOT NULL

## Entity relationship diagram
![Entity relation Diagram](https://github.com/bijay-05/simple-data-pipeline-demo/assets/86017045/db20ee03-bc28-4b50-94d6-fc5fa6aa8487)
