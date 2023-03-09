### SQL Operators and Their Procedure

SQL operators are used to perform various operations on data stored in a relational database. These operators are used to manipulate data, filter data, and sort data. In this section, we will discuss some of the most commonly used SQL operators and their procedures.

#### Arithmetic Operators

Arithmetic operators are used to perform mathematical operations on numeric data types. The following table shows the arithmetic operators used in SQL:

| Operator | Description |
| --- | --- |
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| % | Modulus |

Example: 

```sql
SELECT (10 + 5) * 2;
```

#### Comparison Operators

Comparison operators are used to compare two values. The following table shows the comparison operators used in SQL:

| Operator | Description |
| --- | --- |
| = | Equal to |
| <> or != | Not equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal to |
| <= | Less than or equal to |

Example:

```sql
SELECT * FROM customers WHERE age > 18;
```

#### Logical Operators

Logical operators are used to combine two or more conditions. The following table shows the logical operators used in SQL:

| Operator | Description |
| --- | --- |
| AND | Returns true if both conditions are true |
| OR | Returns true if one or both conditions are true |
| NOT | Negates a condition |

Example:

```sql
SELECT * FROM customers WHERE age > 18 AND gender = 'female';
```

#### Bitwise Operators

Bitwise operators are used to perform operations on binary numbers. The following table shows the bitwise operators used in SQL:

| Operator | Description |
| --- | --- |
| & | Bitwise AND |
| \| | Bitwise OR |
| ^ | Bitwise XOR |
| ~ | Bitwise NOT |

Example:

```sql
SELECT * FROM customers WHERE age & 1 = 0;
```

#### Assignment Operators

Assignment operators are used to assign a value to a variable. The following table shows the assignment operators used in SQL:

| Operator | Description |
| --- | --- |
| = | Assigns a value to a variable |
| += | Adds a value to a variable and assigns the result to the variable |
| -= | Subtracts a value from a variable and assigns the result to the variable |
| *= | Multiplies a variable by a value and assigns the result to the variable |
| /= | Divides a variable by a value and assigns the result to the variable |
| %= | Performs modulus operation on a variable and assigns the result to the variable |

Example:

```sql
UPDATE customers SET age = age + 1 WHERE id = 1;
```

In conclusion, SQL operators are the backbone of SQL queries. The correct use of these operators can help you manipulate data in a relational database. Understanding the procedure of SQL operators is essential in mastering SQL.