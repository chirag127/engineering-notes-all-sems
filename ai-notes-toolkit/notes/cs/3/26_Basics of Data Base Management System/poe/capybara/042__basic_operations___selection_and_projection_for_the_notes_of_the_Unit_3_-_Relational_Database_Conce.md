### Basic Operations – Selection and Projection

Relational databases are designed to store and manage large amounts of data in a structured manner. To extract useful information from these databases, we need to perform specific operations. Two of the most common operations used in relational databases are Selection and Projection.

#### Selection
Selection is the process of selecting specific rows from a table based on certain criteria. It is also known as filtering. The criteria used to filter rows are expressed using conditions that are evaluated against each row in the table. The result of the selection operation is a new table that contains only the rows that satisfy the specified conditions.

Selection operation can be performed using the following SQL statement:
```
SELECT * FROM table_name WHERE condition;
```
Where table_name is the name of the table from which we want to select rows, and condition is the criteria used to filter rows. The * symbol is used to specify that we want to select all columns from the table.

#### Projection
Projection is the process of selecting specific columns from a table. It is used to reduce the amount of data retrieved from a table and to focus on specific attributes of interest. The result of the projection operation is a new table that contains only the selected columns.

Projection operation can be performed using the following SQL statement:
```
SELECT column1, column2, ... FROM table_name;
```
Where table_name is the name of the table from which we want to select columns, and column1, column2, ... are the names of the columns that we want to select.

#### Conclusion
Selection and projection are two fundamental operations used in relational databases. They are used to extract specific information from tables based on certain criteria. By mastering these operations, you can effectively query and manage relational databases.