### Unions

- A union is an SQL operator that combines the result sets of two or more SELECT queries into a single result set.
- A union eliminates any duplicate rows from the result set, unless the ALL option is specified.
- A union requires that the number and data types of the columns in the SELECT queries must be the same or compatible.
- A union can be used to combine data from different tables that have a similar structure or meaning.
- A union can also be used to create a derived table that can be used in a subquery or a join.

#### Syntax of union in SQL

```sql
SELECT column1, column2, ..., columnN FROM table1
UNION [ALL]
SELECT column1, column2, ..., columnN FROM table2
UNION [ALL]
...
SELECT column1, column2, ..., columnN FROM tableN;
```

- The UNION keyword combines the result sets of the SELECT queries and removes any duplicate rows.
- The UNION ALL keyword combines the result sets of the SELECT queries and preserves any duplicate rows.
- The order of the columns in the SELECT queries must be the same.
- The data types of the columns in the SELECT queries must be the same or compatible.

#### Example of union in SQL

Suppose we have two tables: customers and suppliers, with the following structure and data:

```sql
CREATE TABLE customers (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  city VARCHAR(50)
);

INSERT INTO customers VALUES
(1, 'Alice', 'New York'),
(2, 'Bob', 'Los Angeles'),
(3, 'Charlie', 'Chicago'),
(4, 'David', 'Boston');

CREATE TABLE suppliers (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  city VARCHAR(50)
);

INSERT INTO suppliers VALUES
(5, 'Eve', 'New York'),
(6, 'Frank', 'Los Angeles'),
(7, 'Grace', 'Chicago'),
(8, 'Harry', 'Boston');
```

To get the names and cities of all customers and suppliers, we can use the following union query:

```sql
SELECT name, city FROM customers
UNION
SELECT name, city FROM suppliers;
```

The result set is:

| name   | city       |
| ------ | ---------- |
| Alice  | New York   |
| Bob    | Los Angeles|
| Charlie| Chicago    |
| David  | Boston     |
| Eve    | New York   |
| Frank  | Los Angeles|
| Grace  | Chicago    |
| Harry  | Boston     |

Note that the duplicate rows (New York, Los Angeles, Chicago, Boston) are eliminated by the union operator.

To get the names and cities of all customers and suppliers, including the duplicates, we can use the following union all query:

```sql
SELECT name, city FROM customers
UNION ALL
SELECT name, city FROM suppliers;
```

The result set is:

| name   | city       |
| ------ | ---------- |
| Alice  | New York   |
| Bob    | Los Angeles|
| Charlie| Chicago    |
| David  | Boston     |
| Eve    | New York   |
| Frank  | Los Angeles|
| Grace  | Chicago    |
| Harry  | Boston     |
| Eve    | New York   |
| Frank  | Los Angeles|
| Grace  | Chicago    |
| Harry  | Boston     |

Note that the duplicate rows are preserved by the union all operator.