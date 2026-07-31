# Unions

- A union is an SQL operator that combines the result sets of two or more SELECT queries into a single result set.
- A union eliminates any duplicate rows from the result set, unless the ALL option is specified.
- A union requires that the number and data types of the columns in the SELECT queries must be the same or compatible.
- A union can be used to combine data from different tables that have a similar structure or meaning.
- A union can be useful for performing queries across multiple tables or databases, or for combining data from different sources.

## Syntax of union in SQL

The basic syntax of a union is as follows:

```sql
SELECT column1, column2, ..., columnN FROM table1
UNION [ALL]
SELECT column1, column2, ..., columnN FROM table2;
```

- The UNION keyword is used to combine the result sets of the two SELECT queries.
- The ALL option is optional and can be used to include duplicate rows in the result set.
- The columns in the SELECT queries must have the same number and data types, and they must be in the same order.
- The column names in the result set are taken from the first SELECT query.

## Example of union in SQL

Suppose we have two tables, customers and suppliers, that store the information of the customers and suppliers of a company, respectively. The tables have the following structure and data:

| id | name | city | phone |
|----|------|------|-------|
| 1  | Alice | New York | 111-1111 |
| 2  | Bob | Los Angeles | 222-2222 |
| 3  | Charlie | Chicago | 333-3333 |

| id | name | city | phone |
|----|------|------|-------|
| 1  | David | London | 444-4444 |
| 2  | Eva | Paris | 555-5555 |
| 3  | Frank | Berlin | 666-6666 |

If we want to get the names and cities of all the customers and suppliers, we can use the following union query:

```sql
SELECT name, city FROM customers
UNION
SELECT name, city FROM suppliers;
```

The result set of the union query is:

| name | city |
|------|------|
| Alice | New York |
| Bob | Los Angeles |
| Charlie | Chicago |
| David | London |
| Eva | Paris |
| Frank | Berlin |

Note that the union query has eliminated any duplicate rows from the result set. If we want to include duplicate rows, we can use the ALL option as follows:

```sql
SELECT name, city FROM customers
UNION ALL
SELECT name, city FROM suppliers;
```

The result set of the union all query is:

| name | city |
|------|------|
| Alice | New York |
| Bob | Los Angeles |
| Charlie | Chicago |
| David | London |
| Eva | Paris |
| Frank | Berlin |
| David | London |
| Eva | Paris |
| Frank | Berlin |

Note that the union all query has included the duplicate rows from the second SELECT query in the result set.