### Here we will discuss about what is the schema of sales data 
### that we are going to get from the sales database

## SOME KEY CONSIDERATIONS
Let's say a customer purchases more than one item (i.e separate product_id's).
Here we will consider a sale of single kind of product (i.e same product_id) as
a single transaction in the sales_table.

What columns does a sales table need to have ???

- sale_id : PRIMARY KEY, SERIAL, NOT NULL
- date_time: TIMESTAMP, DEFAULT NOW(), NOT NULL
- customer_membership: INT (0 OR 1), DEFAULT 0 (NON-MEMBER), NOT NULL
- product_id: INT, NOT NULL
- QUANTITY: INT, NOT NULL
- UNIT_PRICE: FLOAT, NOT NULL
- TOTAL_PRICE: FLOAT, NOT NULL