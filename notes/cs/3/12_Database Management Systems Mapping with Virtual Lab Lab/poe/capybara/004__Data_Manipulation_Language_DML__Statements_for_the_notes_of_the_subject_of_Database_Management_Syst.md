## Data Manipulation Language (DML) Statements

Data Manipulation Language (DML) statements are used to manipulate data in a database. These statements are used to insert, update, delete, and retrieve data from a database.

### Insert Statement

The insert statement is used to insert new data into a table. The syntax for the insert statement is as follows:

```
INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
```

### Update Statement

The update statement is used to modify existing data in a table. The syntax for the update statement is as follows:

```
UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
```

### Delete Statement

The delete statement is used to delete data from a table. The syntax for the delete statement is as follows:

```
DELETE FROM table_name WHERE condition;
```

### Select Statement

The select statement is used to retrieve data from a table. The syntax for the select statement is as follows:

```
SELECT column1, column2, ... FROM table_name WHERE condition;
```

### Joins

Joins are used to combine data from two or more tables. There are different types of joins such as inner join, left join, right join, and full outer join.

### Group By

The group by statement is used to group data based on one or more columns. The syntax for the group by statement is as follows:

```
SELECT column1, column2, ... FROM table_name WHERE condition GROUP BY column1, column2, ...;
```

### Order By

The order by statement is used to sort data in ascending or descending order. The syntax for the order by statement is as follows:

```
SELECT column1, column2, ... FROM table_name WHERE condition ORDER BY column1, column2, ... ASC|DESC;
```

### Aggregate Functions

Aggregate functions are used to perform calculations on a set of values. Some of the commonly used aggregate functions are:

- COUNT
- SUM
- AVG
- MAX
- MIN