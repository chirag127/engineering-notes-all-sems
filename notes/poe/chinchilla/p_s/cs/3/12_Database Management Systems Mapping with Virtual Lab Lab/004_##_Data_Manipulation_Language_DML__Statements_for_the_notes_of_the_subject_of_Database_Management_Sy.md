## Data Manipulation Language(DML) Statements

Data Manipulation Language (DML) is a subset of SQL that is used to manipulate data in a relational database. DML statements are used to add, modify, delete, and retrieve data from a database. Some of the commonly used DML statements are:

### INSERT Statement
The INSERT statement is used to add new rows to a table. The syntax for the INSERT statement is as follows:

```sql
INSERT INTO table_name (column1, column2, …) VALUES (value1, value2, …);
```

### UPDATE Statement
The UPDATE statement is used to modify existing data in a table. The syntax for the UPDATE statement is as follows:

```sql
UPDATE table_name SET column1 = value1, column2 = value2, … WHERE condition;
```

### DELETE Statement
The DELETE statement is used to delete existing data from a table. The syntax for the DELETE statement is as follows:

```sql
DELETE FROM table_name WHERE condition;
```

### SELECT Statement
The SELECT statement is used to retrieve data from one or more tables. It can retrieve all columns or specific columns from a table. The syntax for the SELECT statement is as follows:

```sql
SELECT column1, column2, … FROM table_name WHERE condition;
```

### Examples

#### Insert Example:

```sql
INSERT INTO employees (id, name, age, salary) VALUES (1, 'John Doe', 25, 50000);
```

#### Update Example:

```sql
UPDATE employees SET salary = 55000 WHERE id = 1;
```

#### Delete Example:

```sql
DELETE FROM employees WHERE id = 1;
```

#### Select Example:

```sql
SELECT name, age, salary FROM employees WHERE age > 30;
```

### Advantages and Disadvantages

Advantages of using DML statements are:
- They allow for easy manipulation of data in a database.
- They can be used to automate common tasks.
- They provide a simple and intuitive syntax.

Disadvantages of using DML statements are:
- They can be prone to errors if not used correctly.
- They can be time-consuming if used to perform complex tasks.

### Applications

DML statements are used in a wide range of applications, including:
- Data entry and management
- Reporting and analytics
- Data migration and transformation