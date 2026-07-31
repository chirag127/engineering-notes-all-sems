### Intersection

- The `INTERSECT` operator in SQL is used to combine two `SELECT` statements, but returns rows only from the first `SELECT` statement that are identical to a row in the second `SELECT` statement.
- The `INTERSECT` operator returns only distinct rows that are common to both queries.
- The number and the order of the columns must be the same in both queries, and the data types must be compatible.
- The basic syntax of the `INTERSECT` operator is as follows:
```
SELECT column1, column2, ...
FROM table1
INTERSECT
SELECT column1, column2, ...
FROM table2;
```
- Here is an example that uses the `INTERSECT` operator to return the names of students who are enrolled in both Math and Science courses:
```
SELECT student_name
FROM math_course
INTERSECT
SELECT student_name
FROM science_course;
```
- The result of the above query will be the names of students who are enrolled in both Math and Science courses.
- The `INTERSECT` operator can be useful when you want to find common data between two tables.
