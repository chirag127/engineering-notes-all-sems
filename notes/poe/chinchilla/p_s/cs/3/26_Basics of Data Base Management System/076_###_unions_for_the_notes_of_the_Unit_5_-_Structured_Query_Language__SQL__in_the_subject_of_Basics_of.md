### Unions

Unions in SQL are used to combine the result sets of two or more SELECT statements into a single result set. The result set of a UNION operation contains all the rows that are present in each of the SELECT statements.

The syntax for a UNION operation is as follows:

```
SELECT column1, column2, ...
FROM table1
UNION
SELECT column1, column2, ...
FROM table2;
```

Here are some important points to remember about UNION operations:

- The columns in the SELECT statements of all the tables must match in terms of data type and number.
- The columns in the result set are determined by the first SELECT statement.
- The UNION operator eliminates any duplicate rows that might exist in the result set.
- The UNION ALL operator does not eliminate any duplicates and simply combines all rows from all SELECT statements.

#### Advantages of using UNION operations

- Helps to combine data from multiple tables into a single result set.
- Allows for easier analysis of data that is spread across multiple tables.
- Saves time and effort by eliminating the need to manually combine data from multiple tables.

#### Disadvantages of using UNION operations

- Can be slower than other types of JOIN operations due to the need for duplicate elimination.
- Might require additional processing to ensure that the columns in the SELECT statements match.
- Might lead to confusion if the columns in the SELECT statements are not clearly labeled.

#### Example

Let's say we have two tables - `employees` and `contractors` - that contain information about people who work for a company. We want to combine the data from both tables into a single result set. Here's how we can do that using a UNION operation:

```
SELECT name, age, salary
FROM employees
UNION
SELECT name, age, hourly_rate * 40 * 52 as salary
FROM contractors;
```

This will produce a result set that contains the name, age, and salary of all the people who work for the company, regardless of whether they are employees or contractors.

#### Applications of UNION operations

- Combining data from multiple tables that have the same structure.
- Merging data from different sources into a single result set.
- Analyzing data that is spread across multiple tables.