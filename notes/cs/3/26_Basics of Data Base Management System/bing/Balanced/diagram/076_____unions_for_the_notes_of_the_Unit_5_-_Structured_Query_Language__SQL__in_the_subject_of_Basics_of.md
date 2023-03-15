### Unions

- A union is an SQL operator that combines the result sets of two or more SELECT queries into a single result set.
- A union removes any duplicate rows from the combined result set, unless the UNION ALL option is used.
- A union requires that the SELECT queries have the same number of columns, the same or compatible data types, and the same order of columns.
- A union can be used to combine data from different tables that have a similar structure, such as different branches of a company or different categories of products.
- A union can also be used to create complex queries that involve multiple conditions, such as finding customers who have ordered products from both online and offline channels.

#### Syntax of union in SQL

```sql
SELECT column_name_1, column_name_2, ..., column_name_n
FROM table_name_1
UNION [ALL]
SELECT column_name_1, column_name_2, ..., column_name_n
FROM table_name_2
UNION [ALL]
...
UNION [ALL]
SELECT column_name_1, column_name_2, ..., column_name_n
FROM table_name_n;
```

- The UNION keyword is used to join the SELECT queries.
- The ALL keyword is optional and can be used to include duplicate rows in the result set.
- The column names in the result set are derived from the first SELECT query, unless an alias is used.

#### Example of union in SQL

Consider the following tables that store the sales data of two branches of a company:

**Branch_A**

| id | product | quantity | price |
|----|---------|----------|-------|
| 1  | A       | 10       | 100   |
| 2  | B       | 20       | 200   |
| 3  | C       | 30       | 300   |

**Branch_B**

| id | product | quantity | price |
|----|---------|----------|-------|
| 4  | A       | 15       | 150   |
| 5  | B       | 25       | 250   |
| 6  | D       | 35       | 350   |

To find the total sales of each product across both branches, we can use the following union query:

```sql
SELECT product, SUM(quantity) AS total_quantity, SUM(price) AS total_price
FROM Branch_A
GROUP BY product
UNION
SELECT product, SUM(quantity) AS total_quantity, SUM(price) AS total_price
FROM Branch_B
GROUP BY product
ORDER BY product;
```

The result set would be:

| product | total_quantity | total_price |
|---------|----------------|-------------|
| A       | 25             | 250         |
| B       | 45             | 450         |
| C       | 30             | 300         |
| D       | 35             | 350         |