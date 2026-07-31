 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Displaying data from multiple tables for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab.

1. Introduction
- A relational database contains multiple tables that are related to each other through common columns known as foreign keys.
- To retrieve data from multiple tables, we need to use JOIN clauses in SQL.
- The three main types of joins are:
-- Inner join: Returns records that have matching values in both tables
-- Left outer join: Returns all records from the left table, and the matched records from the right table
-- Right outer join: Returns all records from the right table, and the matched records from the left table

2. Syntax of JOIN clause
- The basic syntax of a JOIN clause is:

SELECT columns
FROM table1
INNER JOIN table2
ON table1.column = table2.column;

- We need to specify the type of join, followed by the tables to join and the join condition. The join condition specifies the column(s) for which the tables have a relationship.

3. Examples of different joins
- Here are a few examples to demonstrate the different kinds of joins:

INNER JOIN:
SELECT students.name, courses.name
FROM students
INNER JOIN courses
ON students.course_id = courses.id;

LEFT OUTER JOIN:
SELECT students.name, courses.name
FROM students
LEFT OUTER JOIN courses
ON students.course_id = courses.id;

RIGHT OUTER JOIN:
SELECT students.name, courses.name
FROM students
RIGHT OUTER JOIN courses
ON students.course_id = courses.id;