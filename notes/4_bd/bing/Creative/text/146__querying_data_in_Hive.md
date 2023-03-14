#### Querying data in Hive

Hive is a data warehouse system that allows users to query and analyze large-scale data using a SQL-like language called HiveQL. HiveQL can be used to perform various operations on data stored in Hive tables, such as:

- Selecting data from one or more tables using the `SELECT` statement
- Filtering data using the `WHERE` clause and various operators and functions
- Joining data from multiple tables using the `JOIN` clause and different types of joins
- Grouping and aggregating data using the `GROUP BY` and `HAVING` clauses and aggregate functions
- Sorting and limiting data using the `ORDER BY` and `LIMIT` clauses
- Creating, altering, and dropping tables using the `CREATE`, `ALTER`, and `DROP` statements
- Loading and exporting data using the `LOAD` and `EXPORT` commands
- Creating and using views, partitions, buckets, and indexes to optimize query performance and data organization

Some examples of HiveQL queries are:

- To select all the columns from a table named `customers`:

```sql
SELECT * FROM customers;
```

- To select only the `name` and `age` columns from the `customers` table and filter the rows where the `age` is greater than 30:

```sql
SELECT name, age FROM customers WHERE age > 30;
```

- To join the `customers` table with another table named `orders` on the `customer_id` column and select the `name`, `order_id`, and `amount` columns:

```sql
SELECT c.name, o.order_id, o.amount FROM customers c JOIN orders o ON c.customer_id = o.customer_id;
```

- To group the rows in the `orders` table by the `customer_id` column and calculate the total amount for each customer:

```sql
SELECT customer_id, SUM(amount) AS total_amount FROM orders GROUP BY customer_id;
```

- To sort the rows in the `customers` table by the `age` column in descending order and limit the result to 10 rows:

```sql
SELECT * FROM customers ORDER BY age DESC LIMIT 10;
```

- To create a new table named `products` with the columns `product_id`, `name`, `price`, and `category`:

```sql
CREATE TABLE products (product_id INT, name STRING, price FLOAT, category STRING);
```

- To load data from a file named `products.csv` into the `products` table:

```sql
LOAD DATA LOCAL INPATH 'products.csv' INTO TABLE products;
```

- To export the data from the `products` table to a file named `products_backup.csv`:

```sql
EXPORT TABLE products TO 'products_backup.csv';
```

- To create a view named `expensive_products` that contains the rows from the `products` table where the `price` is greater than 100:

```sql
CREATE VIEW expensive_products AS SELECT * FROM products WHERE price > 100;
```

- To create a partitioned table named `sales` with the columns `sale_id`, `product_id`, `quantity`, and `date` and partition the data by the `date` column:

```sql
CREATE TABLE sales (sale_id INT, product_id INT, quantity INT) PARTITIONED BY (date STRING);
```

- To create a bucketed table named `customers_bucketed` with the columns `customer_id`, `name`, and `age` and bucket the data by the `customer_id` column into 10 buckets:

```sql
CREATE TABLE customers_bucketed (customer_id INT, name STRING, age INT) CLUSTERED BY (customer_id) INTO 10 BUCKETS;
```

- To create an index named `product_name_index` on the `name` column of the `products` table:

```sql
CREATE INDEX product_name_index ON TABLE products (name);
```