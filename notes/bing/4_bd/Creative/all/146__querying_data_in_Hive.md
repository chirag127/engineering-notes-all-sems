#### Querying data in Hive

- Hive is a data warehouse system that allows users to query and analyze large-scale data using a SQL-like language called HiveQL.
- HiveQL is similar to standard SQL, but it also supports some features that are specific to Hive, such as partitioning, bucketing, windowing, and user-defined functions.
- HiveQL queries are translated into a series of MapReduce jobs that run on a Hadoop cluster and process the data stored in HDFS or other supported file systems.
- Hive supports various data formats, such as text, CSV, JSON, ORC, Parquet, and Avro, and allows users to define custom data formats using SerDes (serializers and deserializers).
- Hive also provides a metastore service that stores the metadata of the tables, partitions, columns, and other schema information in a relational database.
- To query data in Hive, users need to follow these steps:

  1. Connect to the Hive server using a command-line interface (CLI), a graphical user interface (GUI), or an application programming interface (API).
  2. Create and load tables using the `CREATE TABLE` and `LOAD DATA` statements, or use the `CREATE EXTERNAL TABLE` statement to reference existing data files in HDFS or other file systems.
  3. Use the `SHOW`, `DESCRIBE`, and `EXPLAIN` commands to inspect the tables, columns, partitions, and query plans.
  4. Use the `SELECT`, `JOIN`, `GROUP BY`, `ORDER BY`, `LIMIT`, and other clauses to perform various data analysis tasks on the tables.
  5. Use the `INSERT`, `UPDATE`, `DELETE`, and `MERGE` statements to modify the data in the tables, or use the `DROP TABLE` statement to delete the tables.
  6. Use the `CREATE VIEW` and `DROP VIEW` statements to create and delete views, which are logical representations of the data that can be queried as tables.
  7. Use the `CREATE FUNCTION` and `DROP FUNCTION` statements to create and delete user-defined functions, which are custom functions that can be used in HiveQL queries.
  8. Use the `SET` and `RESET` commands to configure various Hive parameters, such as the number of reducers, the compression codec, the output format, and the query timeout.
  9. Use the `ADD JAR`, `ADD FILE`, and `ADD ARCHIVE` commands to add external resources, such as Java libraries, data files, and compressed archives, to the classpath of the Hive session.
  10. Use the `!` command to execute shell commands from the Hive CLI, or use the `SOURCE` command to execute HiveQL commands from a file.

- Some examples of HiveQL queries are:

  - To create a table named `customers` with four columns: `id`, `name`, `age`, and `gender`, and partition it by `gender`:

    ```sql
    CREATE TABLE customers (
      id INT,
      name STRING,
      age INT
    )
    PARTITIONED BY (gender STRING);
    ```

  - To load data from a CSV file named `customers.csv` into the `customers` table:

    ```sql
    LOAD DATA LOCAL INPATH 'customers.csv'
    INTO TABLE customers
    PARTITION (gender);
    ```

  - To select the name and age of the female customers who are older than 30:

    ```sql
    SELECT name, age
    FROM customers
    WHERE gender = 'F' AND age > 30;
    ```

  - To join the `customers` table with another table named `orders` on the `id` column, and group the results by the `name` column, and calculate the total amount of orders for each customer:

    ```sql
    SELECT c.name, SUM(o.amount) AS total
    FROM customers c
    JOIN orders o
    ON c.id = o.customer_id
    GROUP BY c.name;
    ```

  - To create a view named `top_customers` that shows the name and total amount of orders for the top 10 customers by order amount:

    ```sql
    CREATE VIEW top_customers AS
    SELECT name, total
    FROM (
      SELECT c.name, SUM(o.amount) AS total
      FROM customers c
      JOIN orders o
      ON c.id = o.customer_id
      GROUP BY c.name
      ORDER BY total DESC
      LIMIT 10
    ) t;
    ```

  - To create a user-defined function named `reverse` that reverses a string, and use it in a query to reverse the names of the