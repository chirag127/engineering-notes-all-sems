### SQL Data Types and Literals

SQL (Structured Query Language) is a standard language for managing and manipulating relational databases. In SQL, data is stored in tables, and each column in a table has a specific data type. The data type defines the kind of values that can be stored in the column, as well as the operations that can be performed on the data.

Some common SQL data types include:
- **INTEGER**: A whole number, such as 1, 0, or -1.
- **DECIMAL**: A fixed-point number, such as 1.23 or -0.45.
- **FLOAT**: A floating-point number, such as 1.23e4 or -0.45e-6.
- **CHAR**: A fixed-length character string, such as 'A' or 'hello'.
- **VARCHAR**: A variable-length character string, such as 'A' or 'hello'.
- **DATE**: A date value, such as '2022-10-30'.
- **TIME**: A time value, such as '16:13:49'.
- **TIMESTAMP**: A date and time value, such as '2022-10-30 16:13:49'.

A literal is a value that is written exactly as it is meant to be interpreted. In SQL, literals are used to specify values in SQL statements. For example, in the following INSERT statement, the values 'John', 'Doe', and 25 are literals:

```
INSERT INTO customers (first_name, last_name, age)
VALUES ('John', 'Doe', 25);
```

There are different types of literals in SQL, including string literals, numeric literals, date and time literals, and NULL literals. String literals are enclosed in single quotes, numeric literals are not enclosed in quotes, and date and time literals are usually enclosed in single quotes and follow a specific format.
