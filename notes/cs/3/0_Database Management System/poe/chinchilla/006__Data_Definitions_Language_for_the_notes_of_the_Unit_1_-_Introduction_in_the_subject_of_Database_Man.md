### Data Definitions Language

Data Definitions Language (DDL) is a subset of SQL that is used to define and manipulate the structure of a database. It is used to create and modify database objects such as tables, views, indexes, and constraints.

DDL statements are used to describe the structure of the data in a database. These statements are used to create, alter, and drop database objects such as tables, views, and indexes.

#### Types of DDL Statements

DDL statements can be classified into the following categories:

1. Create Statements - These statements are used to create new database objects such as tables, views, indexes, and constraints.

2. Alter Statements - These statements are used to modify the structure of existing database objects. For example, you can use ALTER TABLE statement to add or remove columns from a table.

3. Drop Statements - These statements are used to remove existing database objects. For example, you can use DROP TABLE statement to remove a table from the database.

#### Examples of DDL Statements

Here are some examples of DDL statements:

1. CREATE TABLE - This statement is used to create a new table in the database. For example,

   ```
   CREATE TABLE employees (
       emp_id INT PRIMARY KEY,
       emp_name VARCHAR(50),
       emp_salary DECIMAL(10,2)
   );
   ```

2. ALTER TABLE - This statement is used to modify the structure of an existing table. For example,

   ```
   ALTER TABLE employees
   ADD COLUMN emp_address VARCHAR(100);
   ```

3. DROP TABLE - This statement is used to remove an existing table from the database. For example,

   ```
   DROP TABLE employees;
   ```

#### Conclusion

In conclusion, DDL is an essential part of SQL that is used to define and manipulate the structure of a database. It is used to create, modify, and remove database objects such as tables, views, and indexes. Understanding DDL is crucial for anyone working with databases, as it allows them to create and manage a database effectively.