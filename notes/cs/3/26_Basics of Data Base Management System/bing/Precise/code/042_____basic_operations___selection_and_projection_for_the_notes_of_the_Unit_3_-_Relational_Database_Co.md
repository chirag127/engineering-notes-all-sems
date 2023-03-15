### Basic Operations – Selection and Projection

Selection and projection are two basic operations in the relational database model. These operations are used to manipulate and retrieve data from a relational database.

#### Selection

Selection is the operation of choosing rows from a table based on a given condition. The result of a selection operation is a new table that contains only the rows that satisfy the condition. The condition is specified using a logical expression, which can include comparison operators such as `=`, `<>`, `<`, `>`, `<=`, and `>=`, as well as logical operators such as `AND`, `OR`, and `NOT`.

For example, to select all rows from a table `Employees` where the value of the `Salary` column is greater than 50000, the selection operation can be written as:

```
SELECT * FROM Employees WHERE Salary > 50000;
```

#### Projection

Projection is the operation of choosing columns from a table. The result of a projection operation is a new table that contains only the specified columns. The columns to be included in the result are specified using a comma-separated list of column names.

For example, to select only the `Name` and `Salary` columns from the `Employees` table, the projection operation can be written as:

```
SELECT Name, Salary FROM Employees;
```

Projection can also be combined with selection to retrieve specific columns from rows that satisfy a given condition. For example, to select the `Name` and `Salary` columns from rows in the `Employees` table where the value of the `Salary` column is greater than 50000, the combined selection and projection operation can be written as:

```
SELECT Name, Salary FROM Employees WHERE Salary > 50000;
```

These are the basic operations of selection and projection in the relational database model. They are essential for manipulating and retrieving data from a relational database.