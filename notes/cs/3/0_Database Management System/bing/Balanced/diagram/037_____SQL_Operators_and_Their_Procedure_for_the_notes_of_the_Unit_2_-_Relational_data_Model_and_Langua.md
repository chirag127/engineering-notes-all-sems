Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Database Management System. Here is the content for the topic of SQL Operators and Their Procedure for the notes of the Unit 2 - Relational data Model and Language.

### SQL Operators and Their Procedure

SQL operators are symbols or keywords that are used to perform certain operations on data in a relational database. SQL operators can be classified into four categories: arithmetic, comparison, logical, and set operators.

- Arithmetic operators are used to perform mathematical calculations on numeric data. The arithmetic operators in SQL are:

  - `+` for addition
  - `-` for subtraction
  - `*` for multiplication
  - `/` for division
  - `%` for modulo (remainder)

  The procedure for using arithmetic operators is to write them between two operands, which can be column names, constants, or expressions. For example, the following query calculates the total salary of each employee by adding the base salary and the bonus:

  ```sql
  SELECT name, salary + bonus AS total_salary
  FROM employee;
  ```

- Comparison operators are used to compare two values and return a boolean result (TRUE, FALSE, or NULL). The comparison operators in SQL are:

  - `=` for equality
  - `<>` or `!=` for inequality
  - `<` for less than
  - `>` for greater than
  - `<=` for less than or equal to
  - `>=` for greater than or equal to
  - `BETWEEN` for checking if a value is within a range
  - `LIKE` for matching a value with a pattern
  - `IN` for checking if a value is among a set of values
  - `IS NULL` for checking if a value is null

  The procedure for using comparison operators is to write them between two operands, which can be column names, constants, or expressions. The operands must be of compatible data types, such as numeric, character, or date. For example, the following query selects the employees who have a salary greater than 5000:

  ```sql
  SELECT name, salary
  FROM employee
  WHERE salary > 5000;
  ```

- Logical operators are used to combine two or more boolean expressions and return a boolean result. The logical operators in SQL are:

  - `AND` for logical conjunction
  - `OR` for logical disjunction
  - `NOT` for logical negation

  The procedure for using logical operators is to write them between two boolean expressions, which can be column names, constants, or expressions. The boolean expressions can be formed by using comparison operators or other logical operators. For example, the following query selects the employees who have a salary between 4000 and 6000 and work in the sales department:

  ```sql
  SELECT name, salary, department
  FROM employee
  WHERE salary BETWEEN 4000 AND 6000
  AND department = 'Sales';
  ```

- Set operators are used to combine two or more result sets and return a single result set. The set operators in SQL are:

  - `UNION` for combining two result sets and removing duplicates
  - `UNION ALL` for combining two result sets and keeping duplicates
  - `INTERSECT` for returning the common rows between two result sets
  - `EXCEPT` or `MINUS` for returning the rows in the first result set that are not in the second result set

  The procedure for using set operators is to write them between two queries, which must have the same number and data type of columns. The queries can be simple or complex, as long as they return compatible result sets. For example, the following query returns the names of the employees who work in either the sales or the marketing department:

  ```sql
  SELECT name
  FROM employee
  WHERE department = 'Sales'
  UNION
  SELECT name
  FROM employee
  WHERE department = 'Marketing';
  ```