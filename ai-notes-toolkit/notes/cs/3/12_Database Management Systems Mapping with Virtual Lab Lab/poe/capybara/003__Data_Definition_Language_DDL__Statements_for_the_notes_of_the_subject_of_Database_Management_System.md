## Data Definition Language(DDL) Statements

Data Definition Language (DDL) statements are used to create, modify, and delete database objects such as tables, indexes, and views. These statements are used to define the structure of the database and to control access to the data. The following are the different types of DDL statements used in Database Management Systems:

1. CREATE Statement: The CREATE statement is used to create a new database object. The syntax for creating a table in SQL is:

```sql
CREATE TABLE table_name (
  column1 datatype,
  column2 datatype,
  column3 datatype,
  ....
);
```

2. ALTER Statement: The ALTER statement is used to modify the structure of an existing database object. The syntax for adding a column to an existing table is:

```sql
ALTER TABLE table_name
ADD column_name datatype;
```

3. DROP Statement: The DROP statement is used to delete an existing database object. The syntax for dropping a table is:

```sql
DROP TABLE table_name;
```

4. TRUNCATE Statement: The TRUNCATE statement is used to delete all data from a table. The syntax for truncating a table is:

```sql
TRUNCATE TABLE table_name;
```

5. RENAME Statement: The RENAME statement is used to rename an existing database object. The syntax for renaming a table is:

```sql
RENAME TABLE old_table_name TO new_table_name;
```

6. COMMENT Statement: The COMMENT statement is used to add comments to a database object. The syntax for adding a comment to a table is:

```sql
COMMENT ON TABLE table_name IS 'comment';
```

7. INDEX Statement: The INDEX statement is used to create an index on a table. The syntax for creating an index is:

```sql
CREATE INDEX index_name
ON table_name (column1, column2, ...);
```

8. VIEW Statement: The VIEW statement is used to create a virtual table based on the result of a SELECT statement. The syntax for creating a view is:

```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

In conclusion, DDL statements are essential for creating, modifying, and deleting database objects in a database management system. It is crucial to understand the syntax and usage of DDL statements to effectively manage and control access to data in a database.