### Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

#### Tables – Creation & Alteration

1. **Creating Tables**: The `CREATE TABLE` statement is used to create a new table in a database. The syntax for creating a table is as follows:
```
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
    ...
);
```
2. **Altering Tables**: The `ALTER TABLE` statement is used to add, modify, or delete columns in an existing table. It is also used to add and drop various constraints on an existing table. The syntax for altering a table is as follows:
```
ALTER TABLE table_name
ADD column_name datatype;
```
3. **Modifying Columns**: The `ALTER TABLE` statement can also be used to modify the data type of a column or to change the size of a column. The syntax for modifying a column is as follows:
```
ALTER TABLE table_name
MODIFY COLUMN column_name datatype;
```
4. **Dropping Columns**: The `ALTER TABLE` statement can also be used to drop a column from a table. The syntax for dropping a column is as follows:
```
ALTER TABLE table_name
DROP COLUMN column_name;
```
5. **Adding Constraints**: Constraints can be added to a table to specify rules for the data in the table. The `ALTER TABLE` statement can be used to add constraints to a table. The syntax for adding a constraint is as follows:
```
ALTER TABLE table_name
ADD CONSTRAINT constraint_name
constraint_type (column1, column2, ...);
```
6. **Dropping Constraints**: Constraints can also be dropped from a table using the `ALTER TABLE` statement. The syntax for dropping a constraint is as follows:
```
ALTER TABLE table_name
DROP CONSTRAINT constraint_name;
```