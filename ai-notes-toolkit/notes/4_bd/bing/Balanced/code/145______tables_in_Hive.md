#### Tables in Hive

- Hive is a data warehouse system that allows users to query and analyze large-scale data using SQL-like language called HiveQL.
- Hive supports two types of tables: managed tables and external tables.
- Managed tables are tables that are created and managed by Hive. Hive stores the data for these tables in a default location under the Hive warehouse directory (/user/hive/warehouse by default).
- External tables are tables that are created by Hive but the data is stored outside the Hive warehouse directory. The user has to specify the location of the data when creating an external table. Hive does not move or delete the data for external tables.
- The main difference between managed and external tables is that when a managed table is dropped, Hive deletes both the table metadata and the data. When an external table is dropped, Hive only deletes the table metadata and leaves the data intact.
- To create a managed table, use the CREATE TABLE statement without specifying a location. For example:

```sql
CREATE TABLE students (
  id INT,
  name STRING,
  age INT
);
```

- To create an external table, use the CREATE EXTERNAL TABLE statement and specify a location. For example:

```sql
CREATE EXTERNAL TABLE students (
  id INT,
  name STRING,
  age INT
)
LOCATION '/user/data/students';
```

- To view the details of a table, use the DESCRIBE statement. For example:

```sql
DESCRIBE students;
```

- To view the data in a table, use the SELECT statement. For example:

```sql
SELECT * FROM students;
```

- To insert data into a table, use the INSERT INTO or INSERT OVERWRITE statement. For example:

```sql
INSERT INTO students VALUES (1, 'Alice', 20);
INSERT OVERWRITE students SELECT * FROM another_table;
```

- To delete data from a table, use the DELETE statement. For example:

```sql
DELETE FROM students WHERE id = 1;
```

- To update data in a table, use the UPDATE statement. For example:

```sql
UPDATE students SET name = 'Bob' WHERE id = 2;
```

- To drop a table, use the DROP TABLE statement. For example:

```sql
DROP TABLE students;
```