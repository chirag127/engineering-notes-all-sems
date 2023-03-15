Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System. Here is the content on SQL operators and their procedure:

### SQL operators and their procedure

SQL operators are symbols or keywords that are used to perform certain operations on data in a SQL statement. SQL operators can be classified into four categories:

- Arithmetic operators: These operators are used to perform mathematical calculations on numeric data. For example, `+` for addition, `-` for subtraction, `*` for multiplication, `/` for division, and `%` for modulo. The syntax for using arithmetic operators is:

```sql
SELECT column_name1 operator column_name2 FROM table_name;
```

- Comparison operators: These operators are used to compare two values and return a boolean result (`TRUE`, `FALSE`, or `NULL`). For example, `=` for equality, `<>` or `!=` for inequality, `<` for less than, `>` for greater than, `<=` for less than or equal to, `>=` for greater than or equal to, `BETWEEN` for range, `IN` for membership, `LIKE` for pattern matching, and `IS NULL` for null value. The syntax for using comparison operators is:

```sql
SELECT column_name FROM table_name WHERE column_name operator value;
```

- Logical operators: These operators are used to combine two or more conditions and return a boolean result. For example, `AND` for conjunction, `OR` for disjunction, `NOT` for negation, and `XOR` for exclusive or. The syntax for using logical operators is:

```sql
SELECT column_name FROM table_name WHERE condition1 operator condition2;
```

- Set operators: These operators are used to combine the results of two or more queries and return a single result set. For example, `UNION` for union, `UNION ALL` for union with duplicates, `INTERSECT` for intersection, and `EXCEPT` or `MINUS` for difference. The syntax for using set operators is:

```sql
SELECT column_name FROM table_name1
operator
SELECT column_name FROM table_name2;
```

The procedure for using SQL operators is as follows:

- Write a valid SQL statement that specifies the columns, tables, and conditions for the data manipulation or retrieval.
- Use the appropriate operators to perform the desired operations on the data.
- Execute the SQL statement and check the result set for accuracy and completeness.