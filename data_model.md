### Here we will discuss about what is the schema of sales data 
### that we are going to get from the sales database

## SOME KEY CONSIDERATIONS
Let's say a customer purchases more than one item (i.e separate product_id's).
Here we will consider a sale of single kind of product (i.e same product_id) as
a single transaction in the sales_table. There is another products_table, which relates to 
sales_table through `product_id` field.

What columns does a sales_table need to have ???

- sale_id : PRIMARY KEY, SERIAL, NOT NULL
- date_time: TIMESTAMP, DEFAULT NOW(), NOT NULL
- customer_membership: INT (0 OR 1), DEFAULT 0 (NON-MEMBER), NOT NULL
- product_id: INT, NOT NULL, FOREIGN KEY (products_table)
- QUANTITY: INT, NOT NULL
- UNIT_PRICE: FLOAT, NOT NULL
- TOTAL_PRICE: FLOAT, NOT NULL

What columns does a products_table need to have ???
- product_id : PRIMARY KEY, NOT NULL, INT, FOREIGN KEY (sales_table)
- product_category : VARCHAR, NOT NULL
- product_name : VARCHAR, NOT NULL
- supplier_name : VARCHAR, NOT NULL