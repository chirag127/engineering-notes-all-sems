 Here is the content in markdown format for the topic ### tables – creation & alteration for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System:

### Tables – Creation & Alteration

- A table is a collection of related data entries and it consists of columns and rows.
- Columns define the attributes of the data such as name, age, salary, etc. and rows contain the actual data values for each column.
- To create a table in a database, the `CREATE TABLE` statement is used. The syntax is:

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);
```

- Example: To create a table called `employees` with `emp_id`, `name` and `salary` as columns:

```sql
CREATE TABLE employees (
    emp_id INT,
    name VARCHAR(50),
    salary INT
);
```

- To modify an existing table, the `ALTER TABLE` statement is used. It is used to add, delete or modify columns in a table.
- To add a column:

```sql
ALTER TABLE table_name
ADD column_name datatype;
```

- To delete a column:

```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```

- To change the data type of a column:

```sql
ALTER TABLE table_name
MODIFY COLUMN column_name datatype;
```

- Advantages:
    - Tables provide an organized structure to data.
    - Tables establish relationships between data entries which makes data retrieval and manipulation easy.
    - The `CREATE TABLE` and `ALTER TABLE` statements provide flexibility to modify the table structure as per the requirements.
- Disadvantages:
    - If not properly designed, tables can become disorganized and lead to redundancy and inconsistencies in data.
    - Frequent modifications to tables using `ALTER TABLE` can lead to performance issues.
- Applications: Tables are essential components of relational databases and are widely used to store and manage data in databases.

[Detailed diagrams and examples can be added if required.]