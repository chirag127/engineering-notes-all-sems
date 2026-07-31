### Tuples

- A tuple is an **ordered list of elements** that can be of different types.
- In a relational database, a tuple is **one record** (one row) that contains all the data for an individual entity .
- A tuple consists of **attribute-value pairs** that represent the values of the fields or attributes (columns) for that record .
- For example, in a database containing client contact information, the fields may be categories such as name, phone number, email address and mailing address, while a tuple for that database could be:

| name | phone number | email address | mailing address |
|------|--------------|---------------|-----------------|
| John | 123-456-7890 | john@example.com | 123 Main Street, New York, NY 10001 |

- A tuple can be identified by a **primary key**, which is a unique value or combination of values that distinguishes it from other tuples in the same table.
- A tuple can also be related to other tuples in different tables by a **foreign key**, which is a value or combination of values that matches the primary key of another table.
- For example, in a database containing orders and products, the orders table may have a foreign key that references the primary key of the products table, indicating which product was ordered by each customer:

| order_id | customer_id | product_id | quantity | price |
|----------|-------------|------------|----------|-------|
| 1 | 101 | 1 | 2 | 20 |
| 2 | 102 | 2 | 1 | 15 |
| 3 | 103 | 3 | 3 | 30 |

| product_id | product_name | product_description |
|------------|--------------|---------------------|
| 1 | Book | A book about databases |
| 2 | Pen | A blue pen |
| 3 | Notebook | A notebook with 100 pages |

- A tuple can be manipulated by various operations, such as **insertion**, **deletion**, **update**, and **selection**.
- Insertion adds a new tuple to a table, deletion removes an existing tuple from a table, update modifies the values of one or more attributes of a tuple, and selection retrieves one or more tuples that satisfy a given condition.
- For example, to insert a new tuple into the orders table, we can use the following SQL statement:

```sql
INSERT INTO orders (order_id, customer_id, product_id, quantity, price) VALUES (4, 104, 1, 1, 10);
```

- To delete a tuple from the orders table, we can use the following SQL statement:

```sql
DELETE FROM orders WHERE order_id = 2;
```

- To update a tuple in the orders table, we can use the following SQL statement:

```sql
UPDATE orders SET quantity = 4, price = 40 WHERE order_id = 3;
```

- To select tuples from the orders table, we can use the following SQL statement:

```sql
SELECT * FROM orders WHERE customer_id = 101;
```

- A tuple is an essential concept in relational databases, as it represents the basic unit of data that can be stored, retrieved, and manipulated by the database system.