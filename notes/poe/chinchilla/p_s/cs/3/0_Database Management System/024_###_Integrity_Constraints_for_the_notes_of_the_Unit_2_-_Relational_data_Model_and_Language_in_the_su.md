### Integrity Constraints for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

Integrity constraints are a set of rules that are defined for a database table to ensure data accuracy, consistency, and reliability. In this unit, we will learn about the different types of integrity constraints that can be imposed on a relational database to ensure data integrity.

Here are the different types of integrity constraints:

#### 1. Domain Constraints

Domain constraints define the valid values that can be stored in a column of a table. It is used to ensure that only valid data is entered in the database. For example, a domain constraint can be used to ensure that only positive integers are entered in a column.

#### 2. Entity Integrity Constraints

Entity integrity constraints ensure that each row in a table is uniquely identified by a primary key. It is used to ensure that there are no duplicate rows in a table. For example, if a table has a primary key that consists of two columns, the combination of those two columns should be unique for each row.

#### 3. Referential Integrity Constraints

Referential integrity constraints ensure that the relationships between tables are maintained. It is used to ensure that a foreign key in one table references a primary key in another table. For example, if a table has a foreign key that references a primary key in another table, the value in the foreign key column must exist in the primary key column of the other table.

#### 4. Check Constraints

Check constraints are used to ensure that the data entered in a column meets a specific condition. It is used to ensure that the data entered in a column is valid. For example, a check constraint can be used to ensure that the age entered in a column is greater than 18.

#### Advantages of Integrity Constraints

- Ensures data accuracy and consistency.
- Reduces the risk of data entry errors.
- Improves the quality of data in the database.
- Increases the reliability of the database.

#### Disadvantages of Integrity Constraints

- Can increase the complexity of the database design.
- Can affect the performance of the database.
- Can limit the flexibility of the database.

#### Example

Consider a table called "employees" with columns "emp_id", "emp_name", "salary", and "dept_id". The following are some examples of integrity constraints that can be imposed on this table:

- Domain constraint: The "salary" column can only contain positive integers.
- Entity integrity constraint: The "emp_id" column should be the primary key of the table.
- Referential integrity constraint: The "dept_id" column should reference the primary key of the "departments" table.
- Check constraint: The "salary" column should be greater than or equal to the minimum salary for the employee's role.

#### Applications

Integrity constraints are used in various applications like:

- Banking systems
- Healthcare systems
- E-commerce applications
- Inventory management systems

In conclusion, integrity constraints are an important aspect of database design and play a crucial role in maintaining data accuracy and consistency. Understanding the different types of integrity constraints and their applications can help in designing robust and reliable databases.