### Set-Theoretic Operations for the Notes of the Unit 3 - Relational Database Concepts in the Subject of Basics of Database Management System

Set-theoretic operations are fundamental operations used in relational databases to manipulate and analyze data. These operations are based on the theory of sets and are used to combine, compare, and extract data from different tables. In this section, we will discuss the different set-theoretic operations used in relational databases.

1. Union Operation: 
   - The union operation combines the rows of two tables into a single table.
   - It returns all the distinct rows from both tables.
   - The resulting table will have the same number of columns as the original tables.
   - The syntax for the union operation is: 
     ```
     SELECT column1, column2, ... FROM table1
     UNION
     SELECT column1, column2, ... FROM table2;
     ```
2. Intersection Operation:
   - The intersection operation returns only the common rows between two tables.
   - It returns only the distinct rows that exist in both tables.
   - The resulting table will have the same number of columns as the original tables.
   - The syntax for the intersection operation is:
     ```
     SELECT column1, column2, ... FROM table1
     INTERSECT
     SELECT column1, column2, ... FROM table2;
     ```
3. Difference Operation:
   - The difference operation returns the rows that are in one table but not in the other.
   - It returns only the distinct rows from the first table.
   - The resulting table will have the same number of columns as the original tables.
   - The syntax for the difference operation is:
     ```
     SELECT column1, column2, ... FROM table1
     EXCEPT
     SELECT column1, column2, ... FROM table2;
     ```
4. Cartesian Product Operation:
   - The cartesian product operation returns all possible combinations of rows between two tables.
   - It returns a table with the number of rows equal to the product of the number of rows in both tables.
   - The resulting table will have a number of columns equal to the sum of the number of columns in both tables.
   - The syntax for the cartesian product operation is:
     ```
     SELECT column1, column2, ... FROM table1
     CROSS JOIN table2;
     ```
     
It is important to note that set-theoretic operations can only be performed on tables with the same schema (i.e., the same number of columns and data types). In addition, the results of set-theoretic operations are always new tables, and the original tables remain unchanged. Set-theoretic operations are powerful tools for manipulating data in relational databases and are essential for creating complex queries and reports.