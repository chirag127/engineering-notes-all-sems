### Intersection
Intersection is a set operation that is used to combine the results of two or more SELECT statements. It returns only the rows that are common to the results of all the SELECT statements.

- The syntax for the INTERSECT operator is as follows:
```
SELECT column1, column2, ...
FROM table1
INTERSECT
SELECT column1, column2, ...
FROM table2;
```
- The number and the order of the columns must be the same in all the SELECT statements.
- The data types of the corresponding columns must be compatible.
- The result of the INTERSECT operation is a distinct set of rows that are returned by both SELECT statements.
- If there are duplicate rows in the results of the individual SELECT statements, they are eliminated in the final result set.
- The INTERSECT operator can be used to find common values in two or more tables.
- The INTERSECT operator can be combined with other set operators such as UNION and EXCEPT to form more complex queries.