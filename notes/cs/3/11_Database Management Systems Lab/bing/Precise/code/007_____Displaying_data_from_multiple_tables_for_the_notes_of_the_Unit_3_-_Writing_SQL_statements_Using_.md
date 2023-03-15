### Displaying data from multiple tables

In the subject of Database Management Systems Lab, Unit 3 - Writing SQL statements Using ORACLE /MYSQL, one of the important topics is displaying data from multiple tables.

Here are some key points to remember when displaying data from multiple tables:

1. **JOIN clause**: The JOIN clause is used to combine rows from two or more tables based on a related column between them. There are several types of JOINs, including INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN.

2. **INNER JOIN**: The INNER JOIN keyword selects records that have matching values in both tables. It returns only the rows from both tables where there is a match.

3. **LEFT JOIN**: The LEFT JOIN keyword returns all records from the left table (table1), and the matched records from the right table (table2). The result is NULL from the right side, if there is no match.

4. **RIGHT JOIN**: The RIGHT JOIN keyword returns all records from the right table (table2), and the matched records from the left table (table1). The result is NULL from the left side, when there is no match.

5. **FULL OUTER JOIN**: The FULL OUTER JOIN keyword returns all records when there is a match in either left (table1) or right (table2) table records. It returns NULL for all columns of the table that does not have a matching row.

6. **UNION**: The UNION operator is used to combine the result-set of two or more SELECT statements. It removes duplicate rows between the two SELECT statements. Each SELECT statement within the UNION must have the same number of columns, and the columns must have similar data types.

7. **UNION ALL**: The UNION ALL operator is similar to the UNION operator, but it does not remove duplicate rows between the two SELECT statements.

These are some of the ways to display data from multiple tables in ORACLE /MYSQL. It is important to understand the differences between the different types of JOINs and UNIONs to effectively display data from multiple tables.