### Primary Key

A primary key is a column or a set of columns in a table that uniquely identifies each row in the table. A primary key is used to enforce data integrity and to establish relationships with other tables. A table can have only one primary key, and the values in the primary key column must not be null or duplicated.

Some characteristics of a primary key are:

- It can be composed of one or more columns, depending on the design of the table.
- It must contain unique values for each row in the table. No two rows can have the same primary key value.
- It must not contain null values, as null values cannot be compared for uniqueness.
- It should be chosen from a column or columns that are frequently used to query the table, as primary keys are often used to join tables or to filter data.
- It should be stable, meaning that the values in the primary key column should not change frequently or arbitrarily.

Some examples of primary keys are:

- A student ID number in a table of students.
- A combination of order ID and product ID in a table of order details.
- A social security number in a table of employees.

A primary key can be defined using the PRIMARY KEY constraint in the CREATE TABLE or ALTER TABLE statement. For example, to create a table of customers with a primary key on the customer ID column, the following SQL statement can be used:

```sql
CREATE TABLE customers (
  customer_id INT NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100),
  phone VARCHAR(20),
  PRIMARY KEY (customer_id)
);
```

To create a table of orders with a primary key on the combination of order ID and product ID columns, the following SQL statement can be used:

```sql
CREATE TABLE orders (
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (order_id, product_id)
);
```

A primary key can also be created using a separate CONSTRAINT clause, which allows naming the primary key constraint. For example, to create a table of products with a primary key on the product ID column and name the constraint as pk_products, the following SQL statement can be used:

```sql
CREATE TABLE products (
  product_id INT NOT NULL,
  product_name VARCHAR(100) NOT NULL,
  category VARCHAR(50),
  price DECIMAL(10,2) NOT NULL,
  CONSTRAINT pk_products PRIMARY KEY (product_id)
);
```

A primary key can be modified or dropped using the ALTER TABLE statement. For example, to drop the primary key constraint from the products table, the following SQL statement can be used:

```sql
ALTER TABLE products
DROP CONSTRAINT pk_products;
```

To add a new primary key constraint to the products table on the combination of product ID and category columns, the following SQL statement can be used:

```sql
ALTER TABLE products
ADD CONSTRAINT pk_products PRIMARY KEY (product_id, category);
```

Note that adding or dropping a primary key constraint may affect the existing data and the relationships with other tables, so it should be done with caution and proper testing.